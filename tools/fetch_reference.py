#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""単発の参照文献取得: 臨床・行動科学の根拠を OpenAlex から引いて reference/ に保存する。

日次パイプラインとは独立した、手動実行専用のスクリプトである。
  - raw/ と wiki/ には書かない。保存先は reference/ のみ。
  - Tier分類・compile_wiki・launchd の対象外。

取得は 4 つの経路を組み合わせる。キーワード検索を被引用数で並べるだけでは、
「希少性」のように一般語と同じ綴りの研究プログラムで無関係な文献が混入するため。
  1. 定番文献の名指し(LANDMARKS): タイトルで検索し、語の一致率を検証して採用する
  2. 引用ネットワーク展開: 定番の総説の参考文献(refs)と、核となる実証研究を引用する
     高被引用論文(cites、主題語で絞る)、および OpenAlex の related_works
  3. キーワード検索: 関連度順と、被引用数順(古典の救済)の 2 パス
  4. 関連度ゲート: 定番以外の候補は Claude(Opus 5)で主題定義との適合を判定し、
     off_topic は excluded.jsonl に理由付きで残す(黙って捨てない)。
     Gemini は無料枠が 1 日 20 リクエストで足りないため使わない

アブストラクトが OpenAlex に無い文献は Semantic Scholar と Crossref から補い、
それでも無い場合は書誌のみで索引に残す(has_abstract=false)。
保存したファイルは、書いた直後に実在確認する。index.jsonl の file は実在するパスのみ。

使い方:
    python3 tools/fetch_reference.py --dry-run          # 予算と件数の見積りのみ
    python3 tools/fetch_reference.py                    # 全トピックを取り直す(索引を再構築)
    python3 tools/fetch_reference.py --topic sleep      # 1トピックだけ追加・更新
    python3 tools/fetch_reference.py --verify           # 既存 index の実在確認のみ

必要な環境変数(.env から読む): OPENALEX_API_KEY(必須)、ANTHROPIC_API_KEY(ゲートに必要)。
API 応答は reference/.cache/ に保存し、再実行ではクレジットを消費しない。
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime

import anthropic
import httpx

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF_DIR = os.path.join(BASE, "reference")
PAPERS_DIR = os.path.join(REF_DIR, "papers")
INDEX_PATH = os.path.join(REF_DIR, "index.jsonl")
EXCLUDED_PATH = os.path.join(REF_DIR, "excluded.jsonl")
MISSING_PATH = os.path.join(REF_DIR, "missing_landmarks.jsonl")
CACHE_DIR = os.path.join(REF_DIR, ".cache")

OA_WORKS = "https://api.openalex.org/works"
OA_RATE = "https://api.openalex.org/rate-limit"
S2_BASE = "https://api.semanticscholar.org/graph/v1"
CROSSREF = "https://api.crossref.org/works/"
GATE_MODEL = "claude-opus-5"

SELECT = ",".join([
    "id", "doi", "title", "publication_year", "cited_by_count", "type", "is_retracted",
    "authorships", "abstract_inverted_index", "primary_topic", "referenced_works",
    "related_works",
])
SEARCH_COST = 10        # 検索 1 回のクレジット。ID 指定の一括取得は 1
RESERVE_CREDITS = 2000  # 翌朝の日次取得(約1,560)のために残す
MAX_REQUESTS = 600
MIN_ABSTRACT_CHARS = 150
REFS_PER_SEED = 80      # 総説 1 本から辿る参考文献の上限
REFS_MIN_CITED = 30     # 参考文献・関連文献は被引用がこれ未満なら候補にしない
CITES_MIN_CITED = 30
SEARCH_RELEVANCE_N = 15
SEARCH_CITED_N = 10
SEARCH_CITED_MIN = 100
GATE_BATCH = 12

# ============================================================
# トピック定義
#   definition: 関連度ゲートに渡す主題の定義(含む/除く)
#   queries:    キーワード検索(OpenAlex の title_and_abstract.search 構文)
#   cites_terms: 引用元展開のときに引用側の論文へ課す主題語
#   landmarks:  (タイトル, 役割) 役割は "" / "refs"(参考文献を辿る) / "cites"(引用元を辿る) / "refs,cites"
# ============================================================
TOPICS = {
    "scarcity": {
        "label": "希少性と認知・再現性",
        "definition": (
            "含む: Mullainathan と Shafir の希少性理論(帯域幅、トンネリング、注意の捕捉、借入)。"
            "貧困や金銭的な不足が認知機能・注意・意思決定に与える因果的影響の実証。"
            "その再現性・再分析・方法論批判(Wicherts、O'Donnell、Camerer らの再現)。"
            "消費者行動における希少性マインドセット。貧困と精神的健康の因果(Ridley ら)。"
            "貧困の行動経済学。\n"
            "除く: 天然資源・エネルギー・水・食料など資源経済学や生態学の希少性。"
            "材料科学や物理学。希少性や貧困を背景としてしか扱わない疫学・公衆衛生。"
            "組織のリソース配分一般。"
        ),
        "queries": [
            '"scarcity mindset" OR "psychology of scarcity" OR "scarcity theory" OR "scarcity hypothesis"',
            'scarcity AND poverty AND (cognition OR "cognitive function" OR bandwidth OR attention OR "decision making")',
            'poverty AND ("cognitive function" OR "cognitive load") AND (replication OR reanalysis OR "meta-analysis" OR critique)',
            '"financial scarcity" OR "resource scarcity" AND (cognition OR "decision making" OR "mental health")',
        ],
        "cites_terms": '(scarcity OR poverty OR "cognitive function" OR bandwidth OR "decision making" OR "financial")',
        "landmarks": [
            ("Poverty Impedes Cognitive Function", "refs,cites"),
            ("Some Consequences of Having Too Little", "cites"),
            ("Scarcity: Why Having Too Little Means So Much", ""),
            ("On the psychology of poverty", "refs"),
            ("Scarcity Frames Value", ""),
            ("Money in the Mental Lives of the Poor", ""),
            ("The Psychological Lives of the Poor", ""),
            ("Poverty and economic decision making: a review of scarcity theory", "refs"),
            ("Poverty and Economic Decision-Making: Evidence from Changes in Financial Resources at Payday", ""),
            ("Economic decision-making in poverty depletes behavioral control", ""),
            ("Empirical audit and review and an assessment of evidentiary value in research on the psychological consequences of scarcity", "refs"),
            ("Evaluating the replicability of social science experiments in Nature and Science between 2010 and 2015", ""),
            ("Reducing debt improves psychological functioning and changes decision-making in the poor", ""),
            ("The effects of low socioeconomic status on decision-making processes", ""),
            ("Poverty, depression, and anxiety: Causal evidence and mechanisms", ""),
            ("A self-regulatory model of resource scarcity", ""),
            ("The Effects of Scarcity on Consumer Decision Making", ""),
            ("Do Financial Concerns Make Workers Less Productive?", ""),
            ("Poor and Rational: Decision-Making under Scarcity", ""),
            ("Worries of the poor: The impact of financial burden on the risk attitudes of micro-entrepreneurs", ""),
            ("Comment on “Poverty Impedes Cognitive Function”", ""),
            ("A Behavioral-Economics View of Poverty", ""),
            ("Cognitive Droughts", ""),
            ("Scarcity and cognitive function around payday: A conceptual and empirical analysis", ""),
        ],
    },
    "hedonic": {
        "label": "快楽適応・成功後の幸福",
        "definition": (
            "含む: 快楽適応・快楽の踏み車・セットポイント理論とその修正。"
            "人生の出来事(結婚、失業、障害、宝くじ、昇進、収入増)への適応を追った縦断研究とメタ分析。"
            "収入と幸福の関係(Easterlin paradox、Kahneman と Deaton、Killingsworth)。"
            "感情予測の誤り(impact bias、durability bias、focalism、immune neglect)。"
            "持続的な幸福を保つ介入や理論(Lyubomirsky の hedonic adaptation prevention)。"
            "物質主義・金銭的成功への志向と幸福。\n"
            "除く: 適応の議論を含まない主観的幸福感の尺度開発や国際比較。"
            "身体医学の QOL 研究。消費者満足やブランドの研究。瞑想や感謝介入の効果検証だけのもの。"
        ),
        "queries": [
            '"hedonic adaptation" OR "hedonic treadmill" OR "hedonic relativism"',
            '("set point" OR "set-point") AND ("subjective well-being" OR happiness OR "life satisfaction") AND (adaptation OR "life events")',
            '"affective forecasting" AND ("impact bias" OR "durability bias" OR focalism OR "immune neglect")',
            '(income OR wealth OR "lottery") AND ("emotional well-being" OR happiness OR "life satisfaction") AND (adaptation OR "long-run" OR longitudinal)',
        ],
        "cites_terms": '(adaptation OR "well-being" OR happiness OR "life satisfaction" OR "set point")',
        "landmarks": [
            ("Lottery winners and accident victims: Is happiness relative?", "cites"),
            ("Beyond the hedonic treadmill: Revising the adaptation theory of well-being", "refs,cites"),
            ("Hedonic relativism and planning the good society", ""),
            ("Hedonic adaptation", ""),
            ("Pursuing Happiness: The Architecture of Sustainable Change", "refs"),
            ("Hedonic adaptation to positive and negative experiences", ""),
            ("The challenge of staying happier: Testing the Hedonic Adaptation Prevention model", ""),
            ("Subjective well-being and adaptation to life events: A meta-analysis", "refs"),
            ("Reexamining adaptation and the set point model of happiness: Reactions to changes in marital status", ""),
            ("Adaptation and the set-point model of subjective well-being: Does happiness change after major life events?", ""),
            ("Unemployment alters the set point for life satisfaction", ""),
            ("Personality, life events, and subjective well-being: Toward a dynamic equilibrium model", ""),
            ("Does happiness adapt? A longitudinal study of disability with implications for economists and judges", ""),
            ("High income improves evaluation of life but not emotional well-being", ""),
            ("Experienced well-being rises with income, even above $75,000 per year", ""),
            ("Income and emotional well-being: A conflict resolved", ""),
            ("Does Economic Growth Improve the Human Lot? Some Empirical Evidence", ""),
            ("Economic Growth and Subjective Well-Being: Reassessing the Easterlin Paradox", ""),
            ("Immune neglect: A source of durability bias in affective forecasting", ""),
            ("Affective Forecasting: Knowing What to Want", ""),
            ("Explaining away: A model of affective adaptation", ""),
            ("Focalism: A source of durability bias in affective forecasting", ""),
            ("Would you be happier if you were richer? A focusing illusion", ""),
            ("Money giveth, money taketh away: The dual effect of wealth on happiness", ""),
            ("If money doesn't make you happy, then you probably aren't spending it right", ""),
            ("A dark side of the American dream: Correlates of financial success as a central life aspiration", ""),
            ("Long-Run Effects of Lottery Wealth on Psychological Well-being", ""),
            ("Money and mental wellbeing: A longitudinal study of medium-sized lottery wins", ""),
            ("Subjective well-being: Three decades of progress", ""),
        ],
    },
    "mastery": {
        "label": "熟達・運と実力",
        "definition": (
            "含む: 意図的練習(deliberate practice)による熟達・専門性の獲得と、その効果量をめぐる論争"
            "(Ericsson 対 Macnamara・Hambrick)。才能・練習・遺伝の寄与。直観的専門性が成立する条件。"
            "成功における運とランダム性(Pluchino の talent versus luck、Salganik の人工文化市場、"
            "Matthew effect、hot streak、random impact rule)。生存者バイアスと失敗のアンダーサンプリング。"
            "運と実力の統計的分離(投資運用の luck versus skill、極端な成績の信頼性)。grit と成果。\n"
            "除く: 教育工学の一般的な訓練法、スポーツ生理学、運の哲学的分析(anti-luck epistemology)、"
            "組織のイノベーション一般、帰属理論のうち成功と運の関係を扱わないもの。"
        ),
        "queries": [
            '"deliberate practice" AND (expertise OR "expert performance" OR "meta-analysis")',
            '(luck OR randomness OR chance) AND (success OR "career" OR performance) AND (talent OR skill OR merit)',
            '("survivorship bias" OR "undersampling of failure" OR "regression to the mean") AND (success OR performance OR management)',
            '("Matthew effect" OR "cumulative advantage") AND (success OR career OR science)',
        ],
        "cites_terms": '(practice OR expertise OR expert OR performance OR luck OR skill OR talent OR success)',
        "landmarks": [
            ("The role of deliberate practice in the acquisition of expert performance", "refs,cites"),
            ("Deliberate Practice and Performance in Music, Games, Sports, Education, and Professions: A Meta-Analysis", "refs"),
            ("The Relationship Between Deliberate Practice and Performance in Sports: A Meta-Analysis", ""),
            ("Deliberate practice: Is that all it takes to become an expert?", ""),
            ("Deliberate practice and proposed limits on the effects of practice on the acquisition of expert performance: Why the original definition matters and recommendations for future research", ""),
            ("Deliberate practice and the acquisition and maintenance of expert performance in medicine and related domains", ""),
            ("Expert performance: Its structure and acquisition", ""),
            ("The influence of experience and deliberate practice on the development of superior expert performance", ""),
            ("Perception in chess", ""),
            ("Skill in chess", ""),
            ("Conditions for intuitive expertise: A failure to disagree", ""),
            ("Talent versus luck: the role of randomness in success and failure", "cites"),
            ("Experimental study of inequality and unpredictability in an artificial cultural market", ""),
            ("The Matthew effect in science", ""),
            ("Quantifying the evolution of individual scientific impact", ""),
            ("Hot streaks in artistic, cultural, and scientific careers", ""),
            ("Success and luck in creative careers", ""),
            ("Vicarious learning, undersampling of failure, and the myths of management", ""),
            ("Random walks and sustained competitive advantage", ""),
            ("Top performers are not the most impressive when extreme performance indicates unreliability", ""),
            ("Chance explanations in the management sciences", ""),
            ("Luck versus skill in the cross-section of mutual fund returns", ""),
            ("Survivorship bias in performance studies", ""),
            ("Success and Luck: Good Fortune and the Myth of Meritocracy", ""),
            ("The Success Equation: Untangling Skill and Luck in Business, Sports, and Investing", ""),
            ("Fooled by Randomness: The Hidden Role of Chance in Life and in the Markets", ""),
            ("Peak: Secrets from the New Science of Expertise", ""),
            ("Outliers: The Story of Success", ""),
            ("Grit: Perseverance and passion for long-term goals", ""),
            ("Much ado about grit: A meta-analytic synthesis of the grit literature", ""),
        ],
    },
    "sleep": {
        "label": "睡眠・概日リズム",
        "definition": (
            "含む: 概日リズムとクロノタイプ。睡眠相後退(DSPD/DSWPD)の病態・診断・治療(メラトニン、光療法)。"
            "ソーシャルジェットラグ。睡眠不足・睡眠制限が認知(注意、実行機能)、感情、衝動性、報酬処理に与える影響。"
            "睡眠と気分障害の双方向関係(不眠はうつの予測因子、睡眠減少による躁の誘発、双極性の睡眠障害)。"
            "対人関係・社会リズム療法。\n"
            "除く: 睡眠時無呼吸やむずむず脚など他の睡眠障害だけの研究。臨床含意の無い分子時計の動物研究。"
            "産業安全のみのシフト勤務研究。睡眠薬の薬理だけの研究。"
        ),
        "queries": [
            '"delayed sleep phase" OR "delayed sleep-wake phase"',
            '("social jetlag" OR chronotype OR eveningness) AND (depression OR "mental health" OR "mood")',
            '"sleep deprivation" AND (cognition OR attention OR "executive function" OR "meta-analysis")',
            '("sleep deprivation" OR "sleep loss" OR "sleep restriction") AND (emotion OR mood OR impulsivity OR "reward")',
            'sleep AND bipolar AND (mania OR relapse OR "social rhythm" OR circadian)',
            'insomnia AND depression AND (predictor OR longitudinal OR "meta-analysis")',
        ],
        "cites_terms": '(sleep OR circadian OR chronotype OR insomnia)',
        "landmarks": [
            ("Delayed sleep phase syndrome: A chronobiological disorder with sleep-onset insomnia", "cites"),
            ("Delayed sleep-wake phase disorder", ""),
            ("The etiology of delayed sleep phase disorder", ""),
            ("Delayed sleep phase disorder in youth", ""),
            ("Clinical Practice Guideline for the Treatment of Intrinsic Circadian Rhythm Sleep-Wake Disorders", "refs"),
            ("Circadian Rhythm Sleep Disorders: Part II, Advanced Sleep Phase Disorder, Delayed Sleep Phase Disorder, Free-Running Disorder, and Irregular Sleep-Wake Rhythm", "refs"),
            ("Circadian-Based Therapies for Circadian Rhythm Sleep-Wake Disorders", ""),
            ("The Use of Exogenous Melatonin in Delayed Sleep Phase Disorder: A Meta-analysis", ""),
            ("Social jetlag: Misalignment of biological and social time", "cites"),
            ("Social Jetlag and Obesity", ""),
            ("Life between clocks: Daily temporal patterns of human chronotypes", ""),
            ("Chronotype and Psychiatric Disorders", ""),
            ("Associations between chronotype, morbidity and mortality in the UK Biobank cohort", ""),
            ("A meta-analysis of the impact of short-term sleep deprivation on cognitive variables", "refs"),
            ("The cumulative cost of additional wakefulness: dose-response effects on neurobehavioral functions and sleep physiology from chronic sleep restriction and total sleep deprivation", ""),
            ("Effects of sleep deprivation on cognition", ""),
            ("Sleep deprivation: Impact on cognitive performance", ""),
            ("The sleep-deprived human brain", "refs"),
            ("The human emotional brain without sleep — a prefrontal amygdala disconnect", ""),
            ("Overnight therapy? The role of sleep in emotional brain processing", ""),
            ("The role of sleep in emotional brain function", ""),
            ("The effect of sleep deprivation and restriction on mood, emotion, and emotion regulation: three meta-analyses in one", ""),
            ("Sleep deprivation lowers inhibition and enhances impulsivity to negative stimuli", ""),
            ("Sleep and circadian rhythms in bipolar disorder: Seeking synchrony, harmony, and regulation", "refs"),
            ("Sleep reduction as a final common pathway in the genesis of mania", ""),
            ("Sleep-wake disturbance in interepisode bipolar disorder and high-risk individuals: A systematic review and meta-analysis", ""),
            ("Sleep loss as a trigger of mood episodes in bipolar disorder: individual differences based on diagnostic subtype and gender", ""),
            ("Two-Year Outcomes for Interpersonal and Social Rhythm Therapy in Individuals With Bipolar I Disorder", ""),
            ("Interpersonal and social rhythm therapy: managing the chaos of bipolar disorder", ""),
            ("Insomnia as a predictor of depression: A meta-analytic evaluation of longitudinal epidemiological studies", ""),
            ("Sleep disturbance in bipolar disorder: Therapeutic implications", ""),
        ],
    },
    "bipolar": {
        "label": "双極性障害・薬物療法・副作用",
        "definition": (
            "含む: 双極性障害(I型・II型・スペクトラム)の診断、自然経過、躁・軽躁・混合エピソード、再発。"
            "気分安定薬(リチウム、バルプロ酸、ラモトリギン)の有効性・再発予防・毒性。"
            "抗精神病薬の有効性と副作用(アカシジア、鎮静、体重増加、代謝)。統合失調症対象の副作用データも含む。"
            "双極性への抗うつ薬(躁転リスク、ISBD 報告)。アカシジアの評価尺度・治療・自殺との関連。"
            "治療ガイドライン。\n"
            "除く: 治療含意の無い遺伝子・脳画像研究。小児のみの研究。単極性うつ病だけの薬物研究。"
            "薬物動態の詳細。"
        ),
        "queries": [
            'bipolar AND (mania OR hypomania) AND ("natural history" OR relapse OR recurrence)',
            'bipolar AND (lithium OR valproate OR lamotrigine OR "mood stabilizer") AND ("meta-analysis" OR "systematic review" OR guideline)',
            'antipsychotic AND (akathisia OR sedation OR "adverse effects" OR tolerability) AND ("network meta-analysis" OR "meta-analysis")',
            'bipolar AND antidepressant AND ("manic switch" OR switch OR "task force" OR efficacy)',
            'akathisia AND (treatment OR "rating scale" OR review OR suicid)',
        ],
        "cites_terms": '(bipolar OR mania OR lithium OR antipsychotic OR akathisia)',
        "landmarks": [
            ("Bipolar disorder", "refs"),
            ("Bipolar disorders", ""),
            ("Manic-Depressive Illness: Bipolar Disorders and Recurrent Depression", ""),
            ("The long-term natural history of the weekly symptomatic status of bipolar I disorder", ""),
            ("A prospective investigation of the natural history of the long-term weekly symptomatic status of bipolar II disorder", ""),
            ("Toward a re-definition of subthreshold bipolarity: epidemiology and proposed criteria for bipolar-II, minor bipolar disorders and hypomania", ""),
            ("Lifetime and 12-Month Prevalence of Bipolar Spectrum Disorder in the National Comorbidity Survey Replication", ""),
            ("Bipolar II disorder: epidemiology, diagnosis and management", ""),
            ("Treatment of bipolar disorder", "refs"),
            ("Canadian Network for Mood and Anxiety Treatments (CANMAT) and International Society for Bipolar Disorders (ISBD) 2018 guidelines for the management of patients with bipolar disorder", "refs"),
            ("Comparative efficacy and acceptability of antimanic drugs in acute mania: a multiple-treatments meta-analysis", ""),
            ("Comparative efficacy and acceptability of pharmacological treatments for bipolar depression: a systematic review and network meta-analysis", ""),
            ("Long-term lithium therapy for bipolar disorder: systematic review and meta-analysis of randomized controlled trials", ""),
            ("Lithium plus valproate combination therapy versus monotherapy for relapse prevention in bipolar I disorder (BALANCE): a randomised open-label trial", ""),
            ("Lithium toxicity profile: a systematic review and meta-analysis", ""),
            ("Lithium in the prevention of suicide in mood disorders: updated systematic review and meta-analysis", ""),
            ("Antidepressants for the acute treatment of bipolar depression: a systematic review and meta-analysis", ""),
            ("The International Society for Bipolar Disorders (ISBD) Task Force report on antidepressant use in bipolar disorders", ""),
            ("The risk of switch to mania in patients with bipolar disorder during treatment with an antidepressant alone and in combination with a mood stabilizer", ""),
            ("Effectiveness of adjunctive antidepressant treatment for bipolar depression", ""),
            ("Comparative efficacy and tolerability of 32 oral antipsychotics for the acute treatment of adults with multi-episode schizophrenia: a systematic review and network meta-analysis", "refs"),
            ("Comparative efficacy and tolerability of 15 antipsychotic drugs in schizophrenia: a multiple-treatments meta-analysis", ""),
            ("Comparative effects of 18 antipsychotics on metabolic function in patients with schizophrenia, predictors of metabolic dysregulation, and association with psychopathology: a systematic review and network meta-analysis", ""),
            ("A rating scale for drug-induced akathisia", ""),
            ("Acute antipsychotic-induced akathisia revisited", "refs"),
            ("Revisiting antipsychotic-induced akathisia: Current issues and prospective challenges", "refs"),
            ("Akathisia: an updated review focusing on second-generation antipsychotics", ""),
            ("The clinical challenges of akathisia", ""),
            ("Suicide attempts associated with akathisia", "cites"),
            ("Akathisia and suicidal ideation in first-episode schizophrenia", ""),
            ("A critical review of akathisia, and its possible association with suicidal behaviour", ""),
        ],
    },
    "cognition": {
        "label": "抑うつ・双極性の認知機能障害、自伝的記憶",
        "definition": (
            "含む: うつ病と双極性障害における認知機能障害(実行機能、記憶、注意、処理速度)、寛解期・寛解後の残存障害、"
            "認知と日常機能・就労の関係、認知障害の評価と対処の推奨。"
            "過度に一般的な自伝的記憶(overgeneral autobiographical memory)とその理論(CaR-FA-X、自己記憶システム)、"
            "うつの経過予測因子としての OGM、記憶特異性訓練。\n"
            "除く: 認知症や統合失調症だけの研究。認知行動療法の一般的な効果研究。注意バイアスなど認知バイアス一般。"
            "健常者の記憶研究で臨床含意の無いもの。"
        ),
        "queries": [
            '(depression OR "major depressive disorder") AND ("cognitive impairment" OR "cognitive dysfunction" OR "executive function") AND ("meta-analysis" OR "systematic review")',
            'bipolar AND (euthymic OR remission) AND (neuropsychological OR "cognitive deficits" OR "cognitive impairment")',
            '"overgeneral autobiographical memory" OR "autobiographical memory specificity" OR "reduced autobiographical memory specificity"',
            '"memory specificity training" OR ("autobiographical memory" AND training AND depression)',
        ],
        "cites_terms": '(cognitive OR neuropsychological OR memory OR bipolar OR depression)',
        "landmarks": [
            ("Cognitive impairment in depression: a systematic review and meta-analysis", "refs"),
            ("Major depressive disorder is associated with broad impairments on neuropsychological measures of executive function: A meta-analysis and review", ""),
            ("Cognitive function following a major depressive episode: systematic review and meta-analysis", ""),
            ("A meta-analysis of cognitive deficits in euthymic patients with bipolar disorder", ""),
            ("Neuropsychological functioning in euthymic bipolar disorder: a meta-analysis", ""),
            ("Cognitive endophenotypes of bipolar disorder: A meta-analysis of neuropsychological deficits in euthymic patients and their first-degree relatives", ""),
            ("Neuropsychological Testing of Cognitive Impairment in Euthymic Bipolar Disorder: An Individual Patient Data Meta-Analysis", ""),
            ("Cognitive Function Across Manic or Hypomanic, Depressed, and Euthymic States in Bipolar Disorder", ""),
            ("Meta-analysis of the association between cognitive abilities and everyday functioning in bipolar disorder", ""),
            ("Cognitive dysfunction in bipolar disorder and schizophrenia: a systematic review of meta-analyses", ""),
            ("Assessing and addressing cognitive impairment in bipolar disorder: the International Society for Bipolar Disorders Targeting Cognition Task Force recommendations for clinicians", ""),
            ("Autobiographical memory in suicide attempters", "cites"),
            ("Autobiographical memory specificity and emotional disorder", "refs,cites"),
            ("Overgeneral autobiographical memory as a predictor of the course of depression: A meta-analysis", ""),
            ("Autobiographical memory specificity, psychopathology, depressed mood and the use of the Autobiographical Memory Test: A meta-analysis", ""),
            ("Reduced specificity of autobiographical memory and depression: The role of executive control", ""),
            ("The construction of autobiographical memories in the self-memory system", ""),
            ("Capture and rumination, functional avoidance, and executive control (CaRFAX): Three processes that underlie overgeneral memory", ""),
            ("Reducing depressive symptoms through memory specificity training", ""),
        ],
    },
    "reward": {
        "label": "報酬系・衝動性・嗜癖",
        "definition": (
            "含む: ドーパミンと報酬予測誤差、incentive salience(wanting と liking)、嗜癖の神経回路と脳疾患モデル。"
            "ゲーム障害・ギャンブル障害・強迫的購買の診断基準、疫学、神経基盤。衝動性の精神医学的側面と認知制御。"
            "双極性障害の報酬過敏(behavioral approach system)と気分症状の報酬処理。遅延割引。"
            "ドーパミン作動薬による衝動制御障害。\n"
            "除く: 食欲・肥満だけの研究。薬物依存の薬理療法の詳細。神経科学的な対応の無い機械学習の強化学習。"
            "動物の運動制御。"
        ),
        "queries": [
            'dopamine AND "prediction error" AND reward',
            '("incentive salience" OR "incentive sensitization") AND (dopamine OR addiction)',
            '"gaming disorder" OR "internet gaming disorder"',
            '"gambling disorder" OR "pathological gambling" AND (neurobiology OR dopamine OR impulsivity OR review)',
            '("compulsive buying" OR "buying-shopping disorder" OR "compulsive shopping")',
            '("reward sensitivity" OR "behavioral approach system" OR "reward hypersensitivity") AND (bipolar OR mania)',
        ],
        "cites_terms": '(dopamine OR reward OR addiction OR gambling OR impulsiv OR bipolar OR gaming)',
        "landmarks": [
            ("A Neural Substrate of Prediction and Reward", "cites"),
            ("Predictive Reward Signal of Dopamine Neurons", ""),
            ("Dopamine reward prediction-error signalling: a two-component response", "refs"),
            ("A framework for mesencephalic dopamine systems based on predictive Hebbian learning", ""),
            ("Behavioral Theories and the Neurophysiology of Reward", ""),
            ("What is the role of dopamine in reward: hedonic impact, reward learning, or incentive salience?", ""),
            ("The debate over dopamine's role in reward: the case for incentive salience", ""),
            ("Liking, wanting, and the incentive-sensitization theory of addiction", "refs"),
            ("The neural basis of drug craving: An incentive-sensitization theory of addiction", ""),
            ("Neurocircuitry of Addiction", ""),
            ("Neurobiologic Advances from the Brain Disease Model of Addiction", ""),
            ("Neural systems of reinforcement for drug addiction: from actions to habits to compulsion", ""),
            ("Dopamine in motivational control: rewarding, aversive, and alerting", ""),
            ("Impulsivity, Compulsivity, and Top-Down Cognitive Control", ""),
            ("Psychiatric aspects of impulsivity", ""),
            ("Toward a behavioral economic understanding of drug dependence: delay discounting processes", ""),
            ("The neurobiology of pathological gambling and drug addiction: an overview and new findings", ""),
            ("Decision-making during gambling: an integration of cognitive and psychobiological approaches", ""),
            ("Gambling disorders", "refs"),
            ("Gambling severity predicts midbrain response to near-miss outcomes", ""),
            ("Pathological Choice: The Neuroscience of Gambling and Gambling Addiction", ""),
            ("An international consensus for assessing internet gaming disorder using the new DSM-5 approach", ""),
            ("Internet Gaming Addiction: A Systematic Review of Empirical Research", ""),
            ("Global prevalence of gaming disorder: A systematic review and meta-analysis", "refs"),
            ("A review of compulsive buying disorder", ""),
            ("The prevalence of compulsive buying: a meta-analysis", ""),
            ("A clinical screener for compulsive buying", ""),
            ("Buying-shopping disorder—is there enough evidence to support its inclusion in ICD-11?", ""),
            ("Mania and dysregulation in goal pursuit: A review", "refs"),
            ("The role of the behavioral approach system (BAS) in bipolar spectrum disorders", ""),
            ("Dysregulation of the behavioral approach system (BAS) in bipolar spectrum disorders: Review of theory and evidence", ""),
            ("Reward Processing and Mood-Related Symptoms: An RDoC and Translational Neuroscience Perspective", ""),
            ("Reward processing dysfunction in major depression, bipolar disorder and schizophrenia", ""),
            ("Impulse Control Disorders in Parkinson Disease: A Cross-Sectional Study of 3090 Patients", ""),
            ("Impulsivity and bipolar disorder", ""),
        ],
    },
    "avoidance": {
        "label": "経験の回避・思考抑制・ACT",
        "definition": (
            "含む: 経験の回避と心理的柔軟性(理論、尺度 AAQ、精神病理との関連)。"
            "アクセプタンス&コミットメント・セラピー(モデル、メタ分析、構成要素研究、第三世代論争)。"
            "思考抑制の逆説的効果(Wegner の ironic process)とそのメタ分析、抑制と精神病理。"
            "回避と反すうがうつを維持する機序、行動活性化(回避への対抗)、感情制御方略のメタ分析。\n"
            "除く: 特定の不安障害の曝露療法プロトコルだけの研究。マインドフルネスの生理学や脳画像だけの研究。"
            "慢性疼痛や身体疾患だけを対象にした ACT は supporting に留める。"
        ),
        "queries": [
            '"experiential avoidance" AND (psychopathology OR depression OR anxiety OR review)',
            '"psychological flexibility" OR "psychological inflexibility"',
            '"thought suppression" AND (paradoxical OR rebound OR ironic OR "meta-analysis")',
            '"acceptance and commitment therapy" AND ("meta-analysis" OR "systematic review" OR efficacy)',
            '"behavioral activation" AND depression AND ("meta-analysis" OR "component analysis")',
        ],
        "cites_terms": '(avoidance OR suppression OR acceptance OR flexibility OR rumination OR depression)',
        "landmarks": [
            ("Experiential avoidance and behavioral disorders: A functional dimensional approach to diagnosis and treatment", "refs,cites"),
            ("Acceptance and Commitment Therapy: Model, processes and outcomes", "refs"),
            ("Acceptance and Commitment Therapy: An Experiential Approach to Behavior Change", ""),
            ("Measuring experiential avoidance: A preliminary test of a working model", ""),
            ("Preliminary Psychometric Properties of the Acceptance and Action Questionnaire–II: A Revised Measure of Psychological Inflexibility and Experiential Avoidance", ""),
            ("Psychological flexibility as a fundamental aspect of health", "refs"),
            ("Experiential avoidance as a generalized psychological vulnerability: Comparisons with coping and emotion regulation strategies", ""),
            ("Experiential avoidance as a functional dimensional approach to psychopathology: An empirical review", ""),
            ("Experiential avoidance and bordering psychological constructs as predictors of the onset, relapse and maintenance of anxiety disorders: One or many?", ""),
            ("Paradoxical effects of thought suppression", "cites"),
            ("Ironic processes of mental control", "refs"),
            ("Paradoxical effects of thought suppression: A meta-analysis of controlled studies", ""),
            ("Thought Suppression", ""),
            ("Thought suppression and psychopathology", ""),
            ("Psychopathology and thought suppression: A quantitative review", ""),
            ("Ironic Effects of Thought Suppression: A Meta-Analysis", ""),
            ("A meta-analysis of the efficacy of acceptance and commitment therapy for clinically relevant mental and physical health problems", ""),
            ("The empirical status of acceptance and commitment therapy: A review of meta-analyses", ""),
            ("The efficacy of Acceptance and Commitment Therapy: An updated systematic review and meta-analysis", ""),
            ("The impact of treatment components suggested by the psychological flexibility model: A meta-analysis of laboratory-based component studies", ""),
            ("Acceptance and mindfulness-based therapy: New wave or old hat?", ""),
            ("Emotion-regulation strategies across psychopathology: A meta-analytic review", ""),
            ("Individual differences in two emotion regulation processes: Implications for affect, relationships, and well-being", ""),
            ("A functional analysis of depression", ""),
            ("A component analysis of cognitive-behavioral treatment for depression", ""),
            ("Behavioral activation treatments of depression: A meta-analysis", ""),
            ("Behavioural activation for depression; an update of meta-analysis of effectiveness and sub group analysis", ""),
            ("Avoidance and depression: The construction of the Cognitive–Behavioral Avoidance Scale", ""),
            ("Responses to depression and their effects on the duration of depressive episodes", ""),
            ("Rethinking Rumination", ""),
        ],
    },
    "suicide": {
        "label": "自殺念慮・安全計画",
        "definition": (
            "含む: 受動的・能動的自殺念慮の定義、有病率、予後上の意味。自殺のリスク因子のメタ分析。"
            "自殺の理論(対人関係理論、3ST、IMV モデル)。安全計画介入(Stanley と Brown)とその効果検証、"
            "危機対応計画、簡易接触介入、急性期の介入のメタ分析。自殺予防戦略の系統的レビュー。"
            "双極性障害の自殺リスクとリチウムの予防効果。アカシジアと自殺。評価尺度(C-SSRS、SSI)。"
            "自殺念慮のリアルタイム変動。\n"
            "除く: 特定の国・集団の疫学統計だけの研究。自傷の生物学。自殺報道やメディアの研究。"
            "法医学。"
        ),
        "queries": [
            '"passive suicidal ideation" OR "passive ideation" OR "death wish" AND suicid',
            '"safety planning" AND (suicide OR suicidal OR "crisis response")',
            '"suicidal ideation" AND ("risk factors" OR prediction) AND ("meta-analysis" OR "systematic review")',
            'suicid AND bipolar AND (lithium OR "risk factors" OR "meta-analysis")',
            '(akathisia OR "antipsychotic-induced") AND suicid',
        ],
        "cites_terms": '(suicid OR "safety plan" OR "self-harm")',
        "landmarks": [
            ("Safety Planning Intervention: A Brief Intervention to Mitigate Suicide Risk", "cites"),
            ("Comparison of the Safety Planning Intervention With Follow-up vs Usual Care of Suicidal Patients Treated in the Emergency Department", "refs"),
            ("Safety planning-type interventions for suicide prevention: meta-analysis", ""),
            ("The effectiveness of the safety planning intervention for adults experiencing suicide-related distress: a systematic review", ""),
            ("Effect of crisis response planning vs. contracts for safety on suicide risk in U.S. Army Soldiers: A randomized clinical trial", ""),
            ("Estimating risk for suicide attempt: Are we asking the right questions? Passive suicidal ideation as a marker for suicidal behavior", ""),
            ("Characterizing the phenomenology of passive suicidal ideation: a systematic review and meta-analysis of its prevalence, psychiatric comorbidity, correlates, and comparisons with active suicidal ideation", ""),
            ("Risk Factors for Suicidal Thoughts and Behaviors: A Meta-Analysis of 50 Years of Research", "refs"),
            ("The Three-Step Theory (3ST): A New Theory of Suicide Rooted in the “Ideation-to-Action” Framework", ""),
            ("The interpersonal theory of suicide", ""),
            ("The integrated motivational–volitional model of suicidal behaviour", ""),
            ("Why People Die by Suicide", ""),
            ("Suicide and Suicidal Behavior", ""),
            ("Cross-national prevalence and risk factors for suicidal ideation, plans and attempts", ""),
            ("The Columbia–Suicide Severity Rating Scale: Initial Validity and Internal Consistency Findings From Three Multisite Studies With Adolescents and Adults", ""),
            ("Assessment of suicidal intention: The Scale for Suicide Ideation", ""),
            ("International Society for Bipolar Disorders Task Force on Suicide: meta-analyses and meta-regression of correlates of suicide attempts and suicide deaths in bipolar disorder", ""),
            ("Suicide attempts in bipolar I and bipolar II disorder: a review and meta-analysis of the evidence", ""),
            ("Epidemiology of suicide in bipolar disorders: a systematic review of the literature", ""),
            ("Suicide and attempted suicide in bipolar disorder: a systematic review of risk factors", ""),
            ("Suicidal behaviour in bipolar disorder: risk and prevention", ""),
            ("Decreased risk of suicides and attempts during long-term lithium treatment: a meta-analytic review", ""),
            ("Suicide prevention strategies revisited: 10-year systematic review", "refs"),
            ("Suicide Prevention Strategies: A Systematic Review", ""),
            ("Association of Suicide Prevention Interventions With Subsequent Suicide Attempts, Linkage to Follow-up Care, and Depression Symptoms for Acute Care Settings: A Systematic Review and Meta-analysis", ""),
            ("Letters, green cards, telephone calls and postcards: systematic and meta-analytic review of brief contact interventions for reducing self-harm, suicide attempts and suicide", ""),
            ("Suicide associated with akathisia and depot fluphenazine treatment", ""),
            ("The relationship of akathisia with suicidality and depersonalization among patients with schizophrenia", ""),
            ("Examination of real-time fluctuations in suicidal ideation and its risk factors: Results from two ecological momentary assessment studies", ""),
            ("Risks of all-cause and suicide mortality in mental disorders: a meta-review", ""),
        ],
    },
}

GATE_SYSTEM = (
    "あなたは臨床心理学・精神医学・行動科学の文献レビュアーです。"
    "与えられた主題の定義に対して、各候補文献が根拠として使えるかを判定します。"
    "回答は JSON 配列のみ。JSON 以外は出力しないでください。"
)

GATE_USER = """主題: {label}
{definition}

判定区分:
- core: 主題の中心的な主張・機序・証拠を直接扱う(この主題を語るとき最初に引くべき文献)
- supporting: 主題に関連し、文脈や補強として引用できる
- off_topic: 主題と無関係、または語が別の意味で使われている(例: 資源経済学の scarcity、物理学の tunneling)

候補:
{candidates}

各候補について次の形式で返してください(JSON 配列のみ):
[{{"id": "W...", "verdict": "core|supporting|off_topic", "reason": "20〜40字の理由"}}]"""

STOPWORDS = {
    "a", "an", "the", "of", "and", "in", "on", "for", "to", "with", "its", "is", "vs",
    "versus", "from", "by", "at", "or", "as", "does", "do", "s", "it",
}


# ============================================================
# ユーティリティ
# ============================================================
def load_dotenv(path):
    """`export KEY=VALUE` / `KEY=VALUE` を読む。値は表示しない。"""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[7:].lstrip()
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            if key and key not in os.environ:
                os.environ[key] = value.strip().strip("\"'")


def restore_abstract(inverted):
    """OpenAlex の abstract_inverted_index(単語→位置の配列)を本文に復元する。"""
    if not inverted:
        return ""
    slots = {}
    for word, positions in inverted.items():
        for pos in positions:
            slots[pos] = word
    # 単語に改行コード(\r\n)が混ざる文献がある。ファイル書き出しで変わるため空白を 1 つに正規化する
    return re.sub(r"\s+", " ", " ".join(slots[i] for i in sorted(slots))).strip()


def slugify(text, limit=60):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return (slug[:limit].rstrip("-")) or "untitled"


def title_tokens(text):
    words = re.sub(r"[^a-z0-9 ]", " ", (text or "").lower()).split()
    return {w for w in words if w not in STOPWORDS and len(w) > 1}


def title_overlap(query, candidate):
    """クエリ側の語のうち候補タイトルに含まれる割合(0〜1)。"""
    q = title_tokens(query)
    if not q:
        return 0.0
    return len(q & title_tokens(candidate)) / len(q)


def classify_evidence(work_type, title, abstract):
    """根拠の種類を推定する。語句による近似で確定ではない。"""
    text = ((title or "") + " " + (abstract or "")).lower()
    if "meta-analy" in text or "metaanaly" in text or "meta analy" in text:
        return "meta_analysis"
    if "systematic review" in text or "meta-review" in text:
        return "systematic_review"
    if work_type in ("review",):
        return "review"
    if work_type in ("book", "book-chapter", "monograph"):
        return "book"
    if "randomi" in text and ("trial" in text or "controlled" in text):
        return "rct"
    if "guideline" in text or "task force" in text or "consensus" in text:
        return "guideline"
    return "article"


def strip_tags(text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text or "")).strip()


# ============================================================
# ディスクキャッシュ付きクライアント
# ============================================================
class Cache:
    def __init__(self, root):
        self.root = root
        os.makedirs(root, exist_ok=True)

    def path(self, namespace, key):
        digest = hashlib.sha1(key.encode("utf-8")).hexdigest()
        d = os.path.join(self.root, namespace)
        os.makedirs(d, exist_ok=True)
        return os.path.join(d, digest + ".json")

    def get(self, namespace, key):
        p = self.path(namespace, key)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                return json.load(f)
        return None

    def put(self, namespace, key, value):
        with open(self.path(namespace, key), "w", encoding="utf-8") as f:
            json.dump(value, f, ensure_ascii=False)


class OpenAlex:
    def __init__(self, key, cache):
        self.cache = cache
        self.requests = 0
        self.credits = 0
        self.http = httpx.Client(timeout=30, headers={"Authorization": "Bearer " + key})

    def rate_limit(self):
        r = self.http.get(OA_RATE)
        r.raise_for_status()
        return r.json()["rate_limit"]

    @staticmethod
    def _key(params):
        return json.dumps(params, sort_keys=True, ensure_ascii=False)

    def cached(self, params):
        return self.cache.get("openalex", self._key(params)) is not None

    def works(self, params):
        params = dict(params)
        params.setdefault("select", SELECT)
        key = self._key(params)
        hit = self.cache.get("openalex", key)
        if hit is not None:
            return hit
        if self.requests >= MAX_REQUESTS:
            raise RuntimeError("1回の上限 %d リクエストに達しました" % MAX_REQUESTS)
        last = None
        for attempt in range(3):
            self.requests += 1
            time.sleep(1.0)
            try:
                r = self.http.get(OA_WORKS, params=params)
                if r.status_code == 200:
                    used = r.headers.get("x-ratelimit-credits-used")
                    self.credits += int(used) if used and used.isdigit() else SEARCH_COST
                    results = r.json().get("results", [])
                    self.cache.put("openalex", key, results)
                    return results
                if r.status_code == 403 and "search" in r.text.lower() and "syntax" in r.text.lower():
                    print("    ! 検索構文エラー: %s" % r.text[:160])
                    return []
                last = "HTTP %s %s" % (r.status_code, r.text[:120])
            except Exception as e:  # ネットワーク障害
                last = str(e)
            time.sleep(5 * (attempt + 1))
        raise RuntimeError("OpenAlex 失敗: %s" % last)

    def by_ids(self, ids, min_cited=0):
        """ID 指定の一括取得(1リクエスト 1 クレジット、50 件まで)。"""
        out = []
        ids = [i.rsplit("/", 1)[-1] for i in ids]
        for i in range(0, len(ids), 50):
            chunk = ids[i:i + 50]
            filt = "openalex_id:" + "|".join(chunk)
            if min_cited:
                filt += ",cited_by_count:>%d" % (min_cited - 1)
            out.extend(self.works({"filter": filt, "per_page": 50}))
        return out


class AbstractFallback:
    """OpenAlex にアブストラクトが無いときの補完。Semantic Scholar → Crossref の順。"""

    def __init__(self, cache):
        self.cache = cache
        self.http = httpx.Client(
            timeout=30,
            headers={"User-Agent": "researcher-reference-fetch (mailto:nakabayashi@thedomainai.com)"},
        )

    def _get(self, namespace, url, params=None):
        key = url + "?" + json.dumps(params or {}, sort_keys=True)
        hit = self.cache.get(namespace, key)
        if hit is not None:
            return hit
        for attempt in range(4):
            time.sleep(1.2)
            try:
                r = self.http.get(url, params=params)
            except Exception:
                r = None
            if r is not None and r.status_code == 200:
                data = r.json()
                self.cache.put(namespace, key, data)
                return data
            if r is not None and r.status_code == 404:
                self.cache.put(namespace, key, {})
                return {}
            time.sleep(5 * (attempt + 1))
        return {}

    def s2_batch(self, dois):
        """Semantic Scholar の一括取得(1リクエストで最大 400 件)。{doi: (abstract, source)} を返す。
        1 件ずつ呼ぶと無認証の制限で 1 件/分まで落ちるため、必ずこちらを使う。"""
        out = {}
        for i in range(0, len(dois), 200):
            chunk = dois[i:i + 200]
            key = "batch:" + json.dumps(chunk)
            data = self.cache.get("s2batch", key)
            if data is None:
                for attempt in range(6):
                    time.sleep(3)
                    try:
                        r = self.http.post(
                            S2_BASE + "/paper/batch",
                            params={"fields": "externalIds,abstract,tldr"},
                            json={"ids": ["DOI:" + d for d in chunk]},
                        )
                    except Exception:
                        r = None
                    if r is not None and r.status_code == 200:
                        data = r.json()
                        self.cache.put("s2batch", key, data)
                        break
                    time.sleep(15 * (attempt + 1))
            for d, item in zip(chunk, data or []):
                if not item:
                    continue
                if item.get("abstract"):
                    out[d] = (item["abstract"], "semantic_scholar")
                elif (item.get("tldr") or {}).get("text"):
                    out[d] = (item["tldr"]["text"], "semantic_scholar_tldr")
            print("    S2 一括 %d/%d(補完 %d 件)" % (min(i + 200, len(dois)), len(dois), len(out)), flush=True)
        return out

    def crossref(self, doi):
        cr = self._get("crossref", CROSSREF + doi)
        msg = (cr or {}).get("message") or {}
        return strip_tags(msg["abstract"]) if msg.get("abstract") else ""

    def fetch(self, doi, title):
        """(abstract, source) を返す。見つからなければ ("", "")。"""
        doi_bare = re.sub(r"^https?://doi.org/", "", doi or "")
        if doi_bare:
            data = self._get("s2", S2_BASE + "/paper/DOI:" + doi_bare, {"fields": "title,abstract,tldr"})
            if data.get("abstract"):
                return data["abstract"], "semantic_scholar"
            if (data.get("tldr") or {}).get("text"):
                return data["tldr"]["text"], "semantic_scholar_tldr"
            cr = self._get("crossref", CROSSREF + doi_bare)
            msg = cr.get("message") or {}
            if msg.get("abstract"):
                return strip_tags(msg["abstract"]), "crossref"
        if title:
            data = self._get("s2", S2_BASE + "/paper/search", {"query": title, "limit": 1, "fields": "title,abstract,tldr"})
            for p in data.get("data", []) or []:
                if title_overlap(title, p.get("title", "")) >= 0.8:
                    if p.get("abstract"):
                        return p["abstract"], "semantic_scholar"
                    if (p.get("tldr") or {}).get("text"):
                        return p["tldr"]["text"], "semantic_scholar_tldr"
        return "", ""


class Gate:
    """Claude による関連度判定。判定はキャッシュし、同じ (topic, id) は再判定しない。"""

    def __init__(self, cache, model=GATE_MODEL, offline=False):
        self.cache = cache
        self.model = model
        self.offline = offline
        self.calls = 0
        self.tokens_in = 0
        self.tokens_out = 0
        # ANTHROPIC_API_KEY は環境から読まれる。429 と 5xx は SDK が再試行する。
        self.client = anthropic.Anthropic(max_retries=4, timeout=180.0)

    def _llm(self, system, user):
        self.calls += 1
        r = self.client.beta.messages.create(
            model=self.model,
            max_tokens=4096,
            betas=["server-side-fallback-2026-07-01"],
            extra_body={"fallbacks": "default"},
            output_config={"effort": "low"},
            system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": user}],
        )
        self.tokens_in += r.usage.input_tokens
        self.tokens_out += r.usage.output_tokens
        if r.stop_reason == "refusal":
            raise RuntimeError("Claude が判定を拒否した")
        return "".join(b.text for b in r.content if b.type == "text")

    def judge(self, topic, cfg, candidates):
        """candidates: [{id,title,year,type,abstract}] → {id: {verdict, reason}}"""
        out = {}
        todo = []
        for c in candidates:
            hit = self.cache.get("gate", topic + "|" + c["id"])
            if hit:
                out[c["id"]] = hit
            else:
                todo.append(c)
        if self.offline:
            for c in todo:
                out[c["id"]] = {"verdict": "unjudged", "reason": "未判定(オフライン)"}
            return out
        for i in range(0, len(todo), GATE_BATCH):
            batch = todo[i:i + GATE_BATCH]
            lines = []
            for c in batch:
                lines.append("- id: %s | %s (%s, %s)\n  %s" % (
                    c["id"], c["title"], c.get("year"), c.get("type"),
                    (c.get("abstract") or "(アブストラクト無し。タイトルで判定)")[:700],
                ))
            prompt = GATE_USER.format(label=cfg["label"], definition=cfg["definition"], candidates="\n".join(lines))
            parsed = None
            for _ in range(2):
                try:
                    raw = self._llm(GATE_SYSTEM, prompt).strip()
                    if raw.startswith("```"):
                        raw = raw.split("\n", 1)[1]
                        raw = raw.rsplit("```", 1)[0]
                    m = re.search(r"\[.*\]", raw, re.S)
                    parsed = json.loads(m.group(0) if m else raw)
                    break
                except Exception as e:
                    print("    ! ゲート応答の解析失敗: %s" % e)
            if not isinstance(parsed, list):
                for c in batch:
                    out[c["id"]] = {"verdict": "unjudged", "reason": "LLM 応答を解析できなかった"}
                continue
            got = {str(x.get("id", "")).rsplit("/", 1)[-1]: x for x in parsed if isinstance(x, dict)}
            for c in batch:
                x = got.get(c["id"])
                verdict = (x or {}).get("verdict", "unjudged")
                if verdict not in ("core", "supporting", "off_topic"):
                    verdict = "unjudged"
                res = {"verdict": verdict, "reason": (x or {}).get("reason", "")[:120]}
                self.cache.put("gate", topic + "|" + c["id"], res)
                out[c["id"]] = res
            print("    ゲート %d/%d" % (min(i + GATE_BATCH, len(todo)), len(todo)), flush=True)
        return out


# ============================================================
# 候補の組み立て
# ============================================================
def work_to_candidate(work):
    oa_id = work["id"].rsplit("/", 1)[-1]
    authors = [(a.get("author") or {}).get("display_name", "") for a in (work.get("authorships") or [])]
    authors = [a for a in authors if a]
    topic = work.get("primary_topic") or {}
    return {
        "openalex_id": oa_id,
        "doi": work.get("doi"),
        "title": (work.get("title") or "").replace("\n", " ").strip(),
        "authors": authors[:8] + (["et al."] if len(authors) > 8 else []),
        "year": work.get("publication_year"),
        "cited_by_count": work.get("cited_by_count") or 0,
        "paper_type": work.get("type"),
        "is_retracted": bool(work.get("is_retracted")),
        "abstract": restore_abstract(work.get("abstract_inverted_index")),
        "abstract_source": "openalex" if work.get("abstract_inverted_index") else "",
        "oa_topic": topic.get("display_name"),
        "oa_field": ((topic.get("field") or {}).get("display_name")),
        "referenced_works": work.get("referenced_works") or [],
        "related_works": work.get("related_works") or [],
    }


def find_landmark(oa, title):
    """タイトル検索 → 語の一致率 0.75 以上の候補から、一致率→被引用数で選ぶ。"""
    q = re.sub(r"[^A-Za-z0-9 ]+", " ", title)
    q = re.sub(r"\s+", " ", q).strip()
    def pick(query_text, params, threshold):
        results = oa.works(params)
        best, best_key = None, None
        for w in results:
            ov = title_overlap(query_text, w.get("title") or "")
            if ov < threshold:
                continue
            key = (round(ov, 2), w.get("cited_by_count") or 0)
            if best_key is None or key > best_key:
                best, best_key = w, key
        return best

    found = pick(title, {"filter": "title.search:%s" % q, "per_page": 8, "sort": "relevance_score:desc"}, 0.75)
    if found is not None:
        return found
    # 救済: 長いタイトルや副題の表記ゆれで外れる場合に備え、先頭 7 語で検索し直す。
    # 一致率はその 7 語に対して 0.9 以上を要求する(誤採用を避ける)。
    head = " ".join(q.split()[:7])
    if len(q.split()) > 7:
        return pick(head, {"filter": "title.search:%s" % head, "per_page": 15, "sort": "cited_by_count:desc"}, 0.9)
    return None


def collect_topic(topic, cfg, oa):
    """4 経路で候補を集める。戻り値: {oa_id: candidate(with channels, landmark)}, missing landmarks"""
    cands = {}
    missing = []

    def add(work, channel, landmark=False):
        c = work_to_candidate(work)
        if not c["title"] or c["is_retracted"]:
            return None
        cur = cands.get(c["openalex_id"])
        if cur is None:
            c["channels"] = [channel]
            c["landmark"] = landmark
            cands[c["openalex_id"]] = c
            return c
        if channel not in cur["channels"]:
            cur["channels"].append(channel)
        cur["landmark"] = cur["landmark"] or landmark
        return cur

    # 1. 定番文献
    seeds_refs, seeds_cites, seeds_related = [], [], []
    for title, role in cfg["landmarks"]:
        w = find_landmark(oa, title)
        if w is None:
            missing.append({"topic": topic, "title": title})
            print("    - 見つからず: %s" % title[:80])
            continue
        c = add(w, "landmark", landmark=True)
        if c is None:
            continue
        if "refs" in role:
            seeds_refs.append(c)
        if "cites" in role:
            seeds_cites.append(c)
        if role:
            seeds_related.append(c)
    print("  定番 %d/%d 件" % (len(cfg["landmarks"]) - len(missing), len(cfg["landmarks"])))

    # 2. 引用ネットワーク展開
    ref_ids = []
    for s in seeds_refs:
        ref_ids.extend(s["referenced_works"][:REFS_PER_SEED])
    ref_ids = [i for i in dict.fromkeys(ref_ids) if i.rsplit("/", 1)[-1] not in cands]
    n_refs = 0
    for w in oa.by_ids(ref_ids, min_cited=REFS_MIN_CITED):
        if add(w, "refs"):
            n_refs += 1
    n_cites = 0
    for s in seeds_cites:
        filt = "cites:%s,title_and_abstract.search:%s,cited_by_count:>%d" % (
            s["openalex_id"], cfg["cites_terms"], CITES_MIN_CITED - 1)
        for w in oa.works({"filter": filt, "sort": "cited_by_count:desc", "per_page": 50}):
            if add(w, "cites:" + s["openalex_id"]):
                n_cites += 1
    rel_ids = []
    for s in seeds_related:
        rel_ids.extend(s["related_works"])
    rel_ids = [i for i in dict.fromkeys(rel_ids) if i.rsplit("/", 1)[-1] not in cands]
    n_rel = 0
    for w in oa.by_ids(rel_ids, min_cited=REFS_MIN_CITED):
        if add(w, "related"):
            n_rel += 1
    print("  展開 参考文献 %d / 引用元 %d / 関連 %d 件" % (n_refs, n_cites, n_rel))

    # 3. キーワード検索(関連度順 + 被引用順)
    n_search = 0
    for query in cfg["queries"]:
        base = "title_and_abstract.search:%s,type:review|article|book|book-chapter" % query
        for w in oa.works({"filter": base, "sort": "relevance_score:desc", "per_page": SEARCH_RELEVANCE_N}):
            if add(w, "search"):
                n_search += 1
        for w in oa.works({"filter": base + ",cited_by_count:>%d" % (SEARCH_CITED_MIN - 1),
                           "sort": "cited_by_count:desc", "per_page": SEARCH_CITED_N}):
            if add(w, "search_cited"):
                n_search += 1
    print("  検索 %d 件" % n_search)
    return cands, missing


# ============================================================
# 保存
# ============================================================
def load_index():
    entries = {}
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    e = json.loads(line)
                    entries[e["openalex_id"]] = e
    return entries


def write_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.replace(tmp, path)


def render_markdown(e):
    authors = ", ".join(e["authors"]) or "(unknown)"
    rel = "; ".join("%s: %s" % (t, e["relevance"][t]["verdict"]) for t in e["topics"])
    lines = [
        "---",
        "title: %s" % json.dumps(e["title"], ensure_ascii=False),
        "authors: %s" % json.dumps(e["authors"], ensure_ascii=False),
        "year: %s" % (e["year"] if e["year"] else "null"),
        "cited_by_count: %d" % e["cited_by_count"],
        "doi: %s" % json.dumps(e["doi"]),
        "openalex_id: %s" % e["openalex_id"],
        "paper_type: %s" % e["paper_type"],
        "evidence_kind: %s" % e["evidence_kind"],
        "topics: %s" % json.dumps(e["topics"], ensure_ascii=False),
        "landmark: %s" % ("true" if e["landmark"] else "false"),
        "abstract_source: %s" % json.dumps(e["abstract_source"]),
        "---",
        "",
        "# %s" % e["title"],
        "",
        "**Authors**: %s | **Year**: %s | **Cited by**: %d | **Kind**: %s | **Relevance**: %s"
        % (authors, e["year"], e["cited_by_count"], e["evidence_kind"], rel),
        "",
        "## Abstract",
        "",
        e["abstract"] if e["has_abstract"] else "(アブストラクトは OpenAlex・Semantic Scholar・Crossref のいずれにも無い。書誌のみ)",
        "",
    ]
    return "\n".join(lines)


def verify_entries(entries):
    missing, mismatch = [], []
    for e in entries.values():
        path = os.path.join(BASE, e["file"])
        if not os.path.isfile(path):
            missing.append(e["file"])
            continue
        with open(path, encoding="utf-8") as f:
            body = f.read()
        if e["openalex_id"] not in body or (e["has_abstract"] and e["abstract"][:80] not in body):
            mismatch.append(e["file"])
    return missing, mismatch


# ============================================================
# メイン
# ============================================================
def main():
    parser = argparse.ArgumentParser(description="臨床・行動科学の参照文献を単発で取得する")
    parser.add_argument("--topic", help="トピックを1つに限定 (%s)" % ", ".join(TOPICS))
    parser.add_argument("--dry-run", action="store_true", help="予算と見積りのみ表示し、取得しない")
    parser.add_argument("--verify", action="store_true", help="既存 index の実在確認のみ")
    parser.add_argument("--no-gate", action="store_true", help="API を呼ばない。キャッシュ済みの判定だけを使い、残りは unjudged にする")
    parser.add_argument("--dump-candidates", action="store_true", help="候補を集めて未判定分を reference/.cache/pending_<topic>.jsonl に書き出すだけ(判定はしない)")
    parser.add_argument("--gate-model", default=GATE_MODEL, help="ゲートに使うモデル(既定: %s)" % GATE_MODEL)
    parser.add_argument("--apply-judgments", metavar="JSONL", help="外部(セッション内レビュー等)の判定を取り込む。行: {topic,id,verdict,reason}")
    args = parser.parse_args()

    if args.apply_judgments:
        cache = Cache(CACHE_DIR)
        n = 0
        with open(args.apply_judgments, encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                j = json.loads(line)
                if j["verdict"] not in ("core", "supporting", "off_topic"):
                    raise SystemExit("不正な verdict: %s" % line)
                cache.put("gate", j["topic"] + "|" + j["id"], {"verdict": j["verdict"], "reason": j.get("reason", "")[:120]})
                n += 1
        print("判定 %d 件を取り込みました" % n)
        return 0

    if args.verify:
        entries = load_index()
        missing, mismatch = verify_entries(entries)
        print("index %d 件 / 欠落 %d / 内容不一致 %d" % (len(entries), len(missing), len(mismatch)))
        for p in missing + mismatch:
            print("  NG:", p)
        return 1 if (missing or mismatch) else 0

    if args.topic and args.topic not in TOPICS:
        print("不明なトピック: %s (%s)" % (args.topic, ", ".join(TOPICS)))
        return 2
    topics = {args.topic: TOPICS[args.topic]} if args.topic else TOPICS

    load_dotenv(os.path.join(BASE, ".env"))
    oa_key = os.environ.get("OPENALEX_API_KEY", "")
    if not oa_key:
        print("OPENALEX_API_KEY が設定されていません。")
        return 1
    if not os.environ.get("ANTHROPIC_API_KEY") and not (args.no_gate or args.dump_candidates):
        print("ANTHROPIC_API_KEY が無いため関連度ゲートを使えません。--no-gate で続行できます。")
        return 1

    cache = Cache(CACHE_DIR)
    oa = OpenAlex(oa_key, cache)
    gate = Gate(cache, model=args.gate_model, offline=(args.no_gate or args.dump_candidates))
    fallback = AbstractFallback(cache)

    # 予算の見積り(キャッシュ済みの検索は数えない)
    uncached_search = 0
    for cfg in topics.values():
        for title, _ in cfg["landmarks"]:
            q = re.sub(r"\s+", " ", re.sub(r"[^A-Za-z0-9 ]+", " ", title)).strip()
            p = {"filter": "title.search:%s" % q, "per_page": 8, "sort": "relevance_score:desc", "select": SELECT}
            uncached_search += 0 if oa.cached(p) else 1
        uncached_search += sum("cites" in role for _, role in cfg["landmarks"])
        uncached_search += 2 * len(cfg["queries"])
    est_credits = uncached_search * SEARCH_COST + 200
    limits = oa.rate_limit()
    remaining = limits["credits_remaining"]
    print("見積り: 検索 約%d 回 → 約%d クレジット | 残り %d | 予約 %d | 前払い残 %s ドル"
          % (uncached_search, est_credits, remaining, RESERVE_CREDITS, limits["prepaid_remaining_usd"]))
    if est_credits > remaining - RESERVE_CREDITS:
        print("無料枠の残り(予約分を除く)を超えるため中止します。課金は発生させません。")
        return 1
    if args.dry_run:
        return 0

    # 索引の準備。全トピック実行なら作り直す。
    if args.topic:
        entries = load_index()
        for e in entries.values():
            e.setdefault("relevance", {})
            e.setdefault("channels", {})
            e.setdefault("landmark", False)
    else:
        entries = {}
        if os.path.isdir(PAPERS_DIR):
            import shutil
            shutil.rmtree(PAPERS_DIR)
    excluded = []
    all_missing = []
    stats = {}

    for topic, cfg in topics.items():
        print("\n[%s] %s" % (topic, cfg["label"]))
        cands, missing = collect_topic(topic, cfg, oa)
        all_missing.extend(missing)

        # 関連度ゲート(定番は判定しない)
        to_judge = [
            {"id": c["openalex_id"], "title": c["title"], "year": c["year"], "type": c["paper_type"], "abstract": c["abstract"]}
            for c in cands.values() if not c["landmark"]
        ]
        if args.dump_candidates:
            pending = [
                dict(c, channels=cands[c["id"]]["channels"], cited=cands[c["id"]]["cited_by_count"],
                     field=cands[c["id"]]["oa_field"], oa_topic=cands[c["id"]]["oa_topic"])
                for c in to_judge if not cache.get("gate", topic + "|" + c["id"])
            ]
            write_jsonl(os.path.join(CACHE_DIR, "pending_%s.jsonl" % topic), pending)
            print("  未判定 %d 件を書き出し(判定済み %d 件)" % (len(pending), len(to_judge) - len(pending)))
            continue
        verdicts = gate.judge(topic, cfg, to_judge)
        kept = {"core": 0, "supporting": 0, "unjudged": 0}
        dropped = 0
        for oa_id, c in cands.items():
            if c["landmark"]:
                rel = {"verdict": "core", "reason": "定番文献(名指しで取得)"}
            else:
                rel = verdicts.get(oa_id, {"verdict": "unjudged", "reason": "ゲート未使用"})
            if rel["verdict"] == "off_topic":
                dropped += 1
                excluded.append({
                    "topic": topic, "openalex_id": oa_id, "title": c["title"], "year": c["year"],
                    "cited_by_count": c["cited_by_count"], "channels": c["channels"], "reason": rel["reason"],
                })
                continue
            kept[rel["verdict"]] += 1
            e = entries.get(oa_id)
            if e is None:
                e = {
                    "openalex_id": oa_id, "doi": c["doi"], "title": c["title"], "authors": c["authors"],
                    "year": c["year"], "cited_by_count": c["cited_by_count"], "paper_type": c["paper_type"],
                    "evidence_kind": classify_evidence(c["paper_type"], c["title"], c["abstract"]),
                    "abstract": c["abstract"], "abstract_source": c["abstract_source"],
                    "has_abstract": len(c["abstract"]) >= MIN_ABSTRACT_CHARS,
                    "oa_topic": c["oa_topic"], "oa_field": c["oa_field"],
                    "topics": [], "channels": {}, "relevance": {}, "landmark": False,
                    "file": "", "file_verified": False, "fetched_at": datetime.now().strftime("%Y-%m-%d"),
                }
                entries[oa_id] = e
            if topic not in e["topics"]:
                e["topics"].append(topic)
            e["channels"][topic] = c["channels"]
            e["relevance"][topic] = rel
            e["landmark"] = e["landmark"] or c["landmark"]
        stats[topic] = {"candidates": len(cands), "kept": kept, "off_topic": dropped, "missing_landmarks": len(missing)}
        print("  候補 %d → 採用 core %d / supporting %d / unjudged %d、除外 %d"
              % (len(cands), kept["core"], kept["supporting"], kept["unjudged"], dropped))

    if args.dump_candidates:
        print("\n候補の書き出しのみ。OpenAlex リクエスト %d 回 / 約 %d クレジット" % (oa.requests, oa.credits))
        write_jsonl(MISSING_PATH, all_missing)
        return 0

    # アブストラクトの補完
    need = [e for e in entries.values() if not e["has_abstract"]]
    print("\nアブストラクト補完: 対象 %d 件" % len(need), flush=True)
    filled = {"semantic_scholar": 0, "semantic_scholar_tldr": 0, "crossref": 0}

    def bare(doi):
        return re.sub(r"^https?://doi.org/", "", doi or "")

    def apply_text(e, text, source):
        e["abstract"], e["abstract_source"], e["has_abstract"] = re.sub(r"\s+", " ", text).strip(), source, True
        e["evidence_kind"] = classify_evidence(e["paper_type"], e["title"], text)
        filled[source] += 1

    # 1) Semantic Scholar の一括取得(DOI のある文献)
    with_doi = [e for e in need if bare(e["doi"])]
    s2 = fallback.s2_batch(sorted({bare(e["doi"]) for e in with_doi})) if with_doi else {}
    for e in with_doi:
        hit = s2.get(bare(e["doi"]))
        if hit and (len(hit[0]) >= MIN_ABSTRACT_CHARS or hit[1] == "semantic_scholar_tldr"):
            apply_text(e, hit[0], hit[1])
    # 2) 残りは Crossref(1 件ずつ・約 1 秒)
    rest = [e for e in need if not e["has_abstract"] and bare(e["doi"])]
    print("  S2 補完後の残り %d 件 → Crossref" % len(rest), flush=True)
    for n, e in enumerate(rest, 1):
        text = fallback.crossref(bare(e["doi"]))
        if len(text) >= MIN_ABSTRACT_CHARS:
            apply_text(e, text, "crossref")
        if n % 100 == 0:
            print("    Crossref %d/%d" % (n, len(rest)), flush=True)
    print("  補完: S2 %d / S2 tldr %d / Crossref %d、書誌のみ %d 件"
          % (filled["semantic_scholar"], filled["semantic_scholar_tldr"], filled["crossref"],
             sum(1 for e in entries.values() if not e["has_abstract"])))

    # ファイル書き出し(主トピック = topics の先頭)と実在確認
    for e in entries.values():
        primary = e["topics"][0]
        e["file"] = os.path.join("reference", "papers", primary, "%s-%s.md" % (slugify(e["title"]), e["openalex_id"].lower()))
        path = os.path.join(BASE, e["file"])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_markdown(e))
        e["file_verified"] = os.path.isfile(path) and os.path.getsize(path) > 0
    entries = {k: v for k, v in entries.items() if v["file_verified"]}

    order = list(TOPICS)
    write_jsonl(INDEX_PATH, sorted(entries.values(), key=lambda x: (order.index(x["topics"][0]), not x["landmark"], -x["cited_by_count"])))
    if args.topic:
        # 1 トピックだけの再実行では、他トピックの除外記録を残す
        old = []
        if os.path.exists(EXCLUDED_PATH):
            with open(EXCLUDED_PATH, encoding="utf-8") as f:
                old = [json.loads(l) for l in f if l.strip() and json.loads(l).get("topic") != args.topic]
        excluded = old + excluded
        old_m = []
        if os.path.exists(MISSING_PATH):
            with open(MISSING_PATH, encoding="utf-8") as f:
                old_m = [json.loads(l) for l in f if l.strip() and json.loads(l).get("topic") != args.topic]
        all_missing = old_m + all_missing
    write_jsonl(EXCLUDED_PATH, excluded)
    write_jsonl(MISSING_PATH, all_missing)
    missing, mismatch = verify_entries(entries)

    print("\n" + "=" * 60)
    print("取得結果(トピック別: 候補 → core / supporting / unjudged、除外、定番の欠落)")
    for topic, s in stats.items():
        k = s["kept"]
        n_topic = sum(1 for e in entries.values() if topic in e["topics"])
        print("  %-10s 候補 %3d → 採用 %3d (core %3d / sup %3d / unj %2d) 除外 %3d 定番欠落 %d"
              % (topic, s["candidates"], n_topic, k["core"], k["supporting"], k["unjudged"], s["off_topic"], s["missing_landmarks"]))
    n_abs = sum(1 for e in entries.values() if e["has_abstract"])
    print("index 合計 %d 件(アブストラクト有 %d / 書誌のみ %d)、除外 %d 件、定番の欠落 %d 件"
          % (len(entries), n_abs, len(entries) - n_abs, len(excluded), len(all_missing)))
    print("OpenAlex リクエスト %d 回 / 約 %d クレジット | ゲート %s 呼び出し %d 回(入力 %d / 出力 %d トークン)"
          % (oa.requests, oa.credits, gate.model, gate.calls, gate.tokens_in, gate.tokens_out))
    print("実在確認: 欠落 %d / 内容不一致 %d" % (len(missing), len(mismatch)))
    print("=" * 60)
    return 1 if (missing or mismatch) else 0


if __name__ == "__main__":
    sys.exit(main())
