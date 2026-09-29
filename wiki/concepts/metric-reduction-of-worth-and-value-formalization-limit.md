# 価値の指標還元と形式化の限界

## 概要

「価値の指標還元と形式化の限界」とは、身体性・情動・社会的埋め込みに根ざす規範的能力は目的関数へ完全には翻訳できず、測定可能な能力を価値の代理指標として扱う還元そのものが、人間的価値の喪失を招くという不変原理である。

AIアラインメントは通常、「倫理的に許容される出力を得るために、機械の振る舞いをどう仕様化・学習・制約するか」という技術課題として枠づけられる。ソースの一つ(Zwitter)はこの枠づけを根本的に不完全だと論じる。倫理は形式化可能なルール集合や選好順序、最適化目標ではなく、人間の条件から創発する性質だという主張である。

AI Nativeな社会設計では、測定できるものが最適化され、最適化されるものが暗黙の価値尺度になりやすい。したがって、何を指標にし、何を指標にしないか、指標化できない領域を誰がどう担うかが、設計の中心課題になる。

## メカニズム

この原理は、対象を人間・AI・組織・技術のいずれに置き換えても成り立つ構造として整理できる。

1. **代理指標への還元**:価値は直接観測できないため、測定可能な能力・成果が代理指標として採用される。指標が評価や資源配分に結びつくと、代理指標が価値そのものとみなされる(グッドハートの法則)。Belkheiriはこれを「アルゴリズム的人間学的還元」と呼び、測定可能な人間の能力が人間の価値の暗黙の指標へ変換されていく過程を指すとする。
2. **暗黙的規範の形式化不可能性**:規範的能力は身体・情動・脆弱性・社会的埋め込み・目的志向・人格形成といった条件から生じる。これを報酬関数、制約、選好モデル、監督手続きに抽象化する操作は、この根を切り落とす。
3. **階層的義務構造の創発**:規範は単一の最適化対象ではなく、義務の生成、免除条件、優先順位の階層として現れる。Bondの分析は、この構造が形式化の手掛かりであると同時に、単一のスカラー目的では表現しにくい構造であることを示唆する。
4. **構造の一般性**:AIに対する報酬設計、組織における人事評価、技術による人間の位置づけのいずれでも、測定可能性が価値の定義を侵食するという同型の構造が現れる。

## 理論的背景

**Zwitter「The embodied ethics alignment problem of AI」(2026)**:倫理的行為主性は、身体性、情動、脆弱性、社会的埋め込み、目的論的志向、人格の発達的形成から生じる創発特性であるとする。アラインメント研究がそれを報酬関数や制約へ翻訳しようとすることを批判し、この問題を「身体化倫理アラインメント問題(EEAP)」と名づけている。

**Belkheiri「THE NEW BABEL BUILDERS」(2026)**:人間の価値を最適化可能な性能指標に還元すること自体が、人間性喪失の構造的メカニズムだと論じる。人間の尊厳を守るには、この還元を拒否し、規範的行為主性と共有された生の形式に根ざした人間の中心性を再構築する必要があると主張する。

**Bond「Seventy Years of Ground Truth」(2026)**:Dear Abbyの20,034通の手紙(1985–2017)を分析し、相談者が「Do I have to?」を義務、「Am I entitled?」を請求、「Can I refuse?」を自由といった、ホーフェルド的な規範語彙で自然に問題を枠づけることを示した。この分析から、ドメイン固有の道徳規則、意味的ゲートのトリガー、無効化条件を符号化した倫理モジュールの有向非巡回グラフ(EM-DAG)が抽出されている。約束が主要な義務生成要因であるという知見も示される(抜粋は途中で切れており、数値の詳細は本記事では扱わない)。これは形式化の限界を否定するものではなく、形式化できる部分と暗黙に残る部分の境界を経験的に探る足場と位置づけられる。

**周辺的な論考**:Sharmaは、道徳的行為能力や意識といった人間の独自性に基づく地位づけを、現在の人間中心的制度に依拠する消滅しうる制約として扱う。Aladiらは、道具的合理性の支配とAIの進展の中で「人間とは何か」という問いを哲学の中心に戻す必要を論じる。Tabirlioğluは、ボーヴォワールの他者性の概念を通じ、制度的・技術的家父長制における他者化と自由の抑圧の分析を示す。これらは、ある存在を外的基準で規定し還元する構造への批判という点で、本原理と接続する。

## AI Nativeな設計への示唆

- **指標の限定的使用**:指標は価値の代理であって価値そのものではないことを設計上明示し、単一指標による評価・報酬・資源配分を避ける。
- **形式化可能部分と不可能部分の分離**:Bondのような経験的知見で義務・免除・優先順位の構造を明示化できる部分は形式化し、残余は人間の判断に留保する。
- **人間の規範的行為主性の保護**:人間の中心性を、性能ではなく規範的行為主性と共有された生の形式に置く(Belkheiri)。人間の価値を生産性や能力比較で定義する設計は避ける。
- **アラインメントの再定義**:倫理を目的関数の問題としてのみ扱わず、身体・情動・社会的埋め込みを含む条件の問題として扱う(Zwitter)。
- **人間による監督の限界の自覚**:監督手続き自体も形式化の一種であり、暗黙的規範を完全には捕捉できないことを前提にする。

## 関連コンセプト

- [[ethical-value-alignment-systems]] — 倫理的価値整合を技術的に扱う枠組みと、その限界の対比
- [[architecture-level-value-preservation-and-social-harness]] — 指標化できない価値をアーキテクチャ層で保存する発想
- [[heterogeneous-value-pluralism-and-immediacy-risk-tradeoff]] — 異質な価値を単一尺度に還元できない問題
- [[repeated-reliance-erodes-judgment-capacity]] — 依存による判断能力の侵食
- [[intelligence-as-externalizable-relational-capacity]] — 能力の外部化と人間の位置づけ
- [[ai-and-labor-value]] — 測定可能な能力と価値の関係
- [[llm-capabilities-and-limits]] — 大規模言語モデルの能力と限界
- [[decomposition-information-retention-limit]] — 分解・形式化に伴う情報損失の限界

## 参考ソース

- Andrew Bond (2026)「Seventy Years of Ground Truth: The Dear Abby Corpus as an Empirical Foundation for AI Ethics」 — `raw/papers/philosophy/seventy-years-of-ground-truth-the-dear-abby-corpus-as-an-empirical-foundation-fo.md`
- Andrej Zwitter (2026)「The embodied ethics alignment problem of AI」 — `raw/papers/philosophy/the-embodied-ethics-alignment-problem-of-ai.md`
- Nadji Belkheiri (2026)「THE NEW BABEL BUILDERS Artificial Intelligence and the Crisis of Human Centrality」 — `raw/papers/philosophy/the-new-babel-builders-artificial-intelligence-and-the-crisis-of-human-centralit.md`
- Arjun Sharma (2026)「ARTIFICIAL INTELLIGENCE, CONSCIOUSNESS AND MORAL AGENCY: RETHINKING HUMAN UNIQUENESS IN THE DIGITAL AGE」 — `raw/papers/philosophy/artificial-intelligence-consciousness-and-moral-agency-rethinking-human-uniquene.md`
- Salem Hussein Aladi, Sunyah Sulaman Alezabi (2026)「Philosophy and the Question of the Human Being: A Critical and Knowledge-Generating Approach」 — `raw/papers/philosophy/philosophy-and-the-question-of-the-human-being-a-critical-and-knowledge-generati.md`
- İrem Tabirlioğlu (2026)「Simone de Beauvoir's Concept of Otherness and Contemporary Gender Politics: An Existential Feminist Perspective」 — `raw/papers/philosophy/simone-de-beauvoirs-concept-of-otherness-and-contemporary-gender-politics-an-exi.md`
