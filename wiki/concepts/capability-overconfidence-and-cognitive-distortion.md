# 能力過信・感情・経歴不連続性による評価の系統的歪み

## 概要

本概念は、**強力な支援能力は計画の誤謬を増幅し、離散的な感情や経歴の一貫性をめぐる曖昧さは評価者・意思決定者の判断を系統的に歪め、支援ツールは能力を拡張すると同時に利用者を囲い込む**、という一群の構造的原理を指す。Tier 1(不変原理)に位置づけられる。

ソースはいずれも起業・ベンチャー領域の研究である。ただし、扱われている構造は「能力が高まるほど自己評価が楽観に傾く」「感情が判断のヒューリスティックとして働く」「シグナルが曖昧だと承認が遅れる」「支援が依存と制約を生む」という形で抽象化でき、判断主体が人間か AI か組織かを問わず成立する。

AI Nativeな社会設計では、AI が計画立案・評価・意思決定支援の中核を担う。そのため、能力の向上そのものが歪みの源泉になりうること、評価する側(人間・AI)にも系統的な偏りがあること、支援ツールが利用者の選択肢を狭めうることを、設計の前提として組み込む必要がある。

## メカニズム

構造的には、次の4つの経路に整理できる。対象(人間・AI・組織・技術)を入れ替えても成り立つ。

1. **能力による楽観の増幅(計画の誤謬)**
   主体が強力な能力を持つと、自らの計画の実現可能性を過大に見積もりやすくなる。能力の向上は成果を高める一方で、過信を通じて成果を損なう経路も開く。
2. **離散的感情によるヒューリスティック歪曲**
   希望・共感・怒りなど個別の感情が、機会や案件の評価を系統的に動かす。評価対象の中身が同じでも、評価者の感情状態によって結論が変わる。
3. **シグナルの曖昧性による承認遅延**
   経歴や軌跡が不連続だと、評価者は「基本的能力の問題か、意志・コミットメントの不安定性か」を区別できず、不確実性の高い状態に置かれる。その結果、地位や信頼の承認が遅れる。
4. **エンパワーメントと囲い込みの二面性**
   外部の支援ツールは認知能力や意思決定を促進すると同時に、制約や依存を生む。促進と制約は同じ機構の表裏である。

これらは独立ではなく、たとえば支援による自己効力感の上昇が過信につながるように、相互に連鎖する。

## 理論的背景

**AI成熟度と計画の誤謬(ソース1)**
テクノロジー系スタートアップを対象に、AI 成熟度を「両刃の能力」として扱い、計画の誤謬が企業成果に及ぼす影響を論じる。AI 能力への過信が計画の誤謬を増幅し、企業成果を低下させる認知メカニズムが中核であり、この機構は対象を変えても不変とされる。

**離散的感情と評価(ソース2)**
環境に害を及ぼす起業機会の評価に対する、希望・共感・怒りの3つの離散的感情の影響を、304名の学部生を対象とした実験で検証している。線形混合効果モデルと推定周辺平均の対比が用いられた。従来の研究は文脈非特定的な感情効果が中心であり、エコ感情との関連は未解明だった、という問題設定である。

**カテゴリー不安定性とステータス移動(ソース3)**
1980〜2012年の米国 VC 1413社の縦断データを用い、社会認知的に離れた産業カテゴリー間を移動した履歴(category erraticism)が上方のステータス移動を低下させることを示す。鍵は、カテゴリーの幅や距離の大きさではなく、移動の軌跡が一貫しているか否かである。一貫性のなさは、外部の評価者にコミットメントと能力への懸念を生む。この懸念は、ステータスが高い企業や経験の長い企業ほど深刻とされる。より厳しい軌跡の一貫性を期待されるためである。

**エンパワーメント–囲い込みフレームワーク(ソース4)**
生成 AI が起業プロセスの各段階(機会認識とアイデア創出、機会評価とコミットメント、資源の結集、事業の立ち上げと成長)で起業家に与える影響を統合的にレビューし、生成 AI が各段階で両刃の剣として働くことを示す。例として、アイデアの質を高める一方でハルシネーションや学習データのバイアスを持ち込むこと、起業家の自己効力感を高める一方で過信も強めることが挙げられている。

**補助的な知見(ソース5〜7)**
- ソース5:起業教育は起業自己効力感の上昇と関連し、自己効力感が学習と行動意図をつなぐ媒介役を果たす。
- ソース6:心理的資本が機会認識を介して起業意図に関わる。内部資源から認識、選択へという抽象的な媒介過程が示される。
- ソース7:知識へのアクセス困難性は不変の制約であり、共感はユーザー知識を解釈・翻訳する認識論的な橋渡しとして位置づけられる。

## AI Nativeな設計への示唆

- **能力向上と較正を対にする**:AI 支援で能力が上がる場面では、計画の見積もりを外部基準や過去実績と照合する仕組みを組み込み、過信の増幅を抑える。
- **感情に依存しない評価経路を用意する**:評価者の感情状態が結論を動かすことを前提に、評価基準の構造化、複数評価者の併用、感情の影響を検知する仕組みを設ける。
- **軌跡の意味を明示するシグナル設計**:経歴の不連続が能力の欠如か意図的な転換かを評価者が判別できるよう、移動の理由や一貫性を伝える情報を付与し、承認遅延を減らす。
- **囲い込みを設計時に点検する**:支援ツールの各段階で、促進効果と制約効果を対にして評価する。ハルシネーションやデータ由来の偏りへの検証手段を利用者側に残す。
- **評価する側も監査対象にする**:人間の評価者だけでなく、AI 評価者にも同様の歪みが生じうると想定し、継続的に検査する。

## 関連コンセプト

- [[capability-externalization-dual-effects]] — 能力外部化の二面性と非定常環境での再適応
- [[bias-compounding-across-interacting-distortion-sources]] — 複数の歪み源の相互作用による偏りの累積・増幅
- [[effort-opacity-and-disclosure-signal-erosion]] — 努力の不可視化と評価シグナルの劣化
- [[affect-and-fairness-in-automated-code-review]] — 自動コードレビューにおける感情と公平性の影響
- [[cognitive-biases-in-ai]] — AIにおける認知バイアス
- [[cognitive-bias-detection]] — 認知バイアス検出
- [[automation-complacency-and-cognitive-atrophy]] — オートメーション・コンプレースンシーと認知機能の退化リスク
- [[ai-cognitive-augmentation]] — AIによる認知拡張
- [[capability-outpacing-control-gap]] — 能力拡大が制御を上回るギャップ
- [[ai-and-organizational-evaluation-in-llm-products]] — LLM製品におけるAIと組織評価

## 参考ソース

1. AI maturity as a double-edged capability: planning fallacy and firm performance in technology startups(Mohammadreza Parsanejad ほか、2026)— `raw/papers/entrepreneurship/ai-maturity-as-a-double-edged-capability-planning-fallacy-and-firm-performance-i.md`
2. The impact of emotions on the evaluation of environmentally damaging entrepreneurial opportunities: an experimental study(Marko Kolaković ほか、2026)— `raw/papers/entrepreneurship/the-impact-of-emotions-on-the-evaluation-of-environmentally-damaging-entrepreneu.md`
3. Drifting to the top? The effects of category erraticism on status mobility in the U.S. venture capital industry(Danyang Li, Michael C. Jensen、2026)— `raw/papers/entrepreneurship/drifting-to-the-top-the-effects-of-category-erraticism-on-status-mobility-in-the.md`
4. Generative AI Use in Entrepreneurship: An Integrative Review and an Empowerment–Entrapment Framework(Jackson G. Lu ほか、2026)— `raw/papers/entrepreneurship/generative-ai-use-in-entrepreneurship-an-integrative-review-and-an-empowermenten.md`
5. Unpacking the link between entrepreneurial education and intention: A moderated mediation model of self-efficacy and university entrepreneurial climate(Julio Segundo ほか、2026)— `raw/papers/entrepreneurship/unpacking-the-link-between-entrepreneurial-education-and-intention-a-moderated-m.md`
6. How does psychological capital shape entrepreneurial intention? The mediating role of opportunity recognition(Sheng Huang ほか、2026)— `raw/papers/entrepreneurship/how-does-psychological-capital-shape-entrepreneurial-intention-the-mediating-rol.md`
7. From Empathy to Impact: Examining Opportunity Recognition for Impactful, Socially Relevant Entrepreneurship(Moses Faleafaga、2026)— `raw/papers/entrepreneurship/from-empathy-to-impact-examining-opportunity-recognition-for-impactful-socially-.md`
