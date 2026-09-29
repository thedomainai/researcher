# 複数の正当性ロジックの競合が規定する自律システム受容

## 概要

組織や社会には、専門職論理、価値ビジョン、規範といった複数の正当性の基準が併存している。AIや自律システムが導入されると、これらの基準がそれぞれ異なる観点から技術を評価する。その結果、受容の程度や統治枠組みが収束するか分裂するかは、技術の性能よりも、どの正当性ロジックが優位に立つかに左右される。

この構造は、対象が変わっても成り立つ。医療現場の臨床家、国家間の軍事AI統治、サービスデザインの学問規律のいずれでも、価値基盤の違いが制度上の対立を生む。

AI Nativeな社会設計にとって重要なのは、次の点である。

- 受容や統治の失敗を、技術の未成熟や情報不足だけの問題として扱わない。
- 併存する正当性ロジックを前提として設計する。
- 競合を隠さず、調整の対象として制度に組み込む。

## メカニズム

以下の三つの構造は、評価する主体を人間、組織、国家に入れ替えても成立する。

### 1. 制度論理の競合

同じ技術でも、参照する論理によって「価値がある」「危険だ」という評価は分かれる。同一組織内でも職種ごとに論理が異なるため、受容態度は一様にならない。受容は個人の態度の総和ではなく、論理どうしの力関係として現れる。

### 2. 価値ビジョンの分岐による制度分裂

各主体は、自らが目指す「良い生」のビジョンに沿ってAI政策を組み立てる。ビジョンが社会の深い基盤に根ざしている場合、その差は交渉で簡単には埋まらず、統治枠組みの分裂として持続する。解消できるのは、ビジョン自体が収束する局面に限られる。

### 3. 規範の再生産と脱規律化

既存の規律や専門分野は、自らの規範を再生産する。この再生産は、想定外の主体や別様の可能性を周縁化する。逆に、規律を意図的にほどく「脱規律化」は複数性を開く。ただし、これは規範が固定化していることを前提にした対抗手段でもある。

三つは相互に作用する。規範の再生産が論理の競合を固定し、競合が価値ビジョンの分岐へ拡大する。

## 理論的背景

### 専門職論理とAI実装(ソース1)

Rizziらは、イタリアで心理療法士40名と一般医(GP)8名の計48名の臨床家を対象に、職種別に4つのフォーカスグループを実施した。参加者は、LLMで強化した心理教育チャットボットのデジタルプロトタイプに実際に触れた。研究は、臨床家の受容と、臨床実践への価値の認識がAIの統合を左右するという前提に立つ。核心的知見は、組織内の複数の専門職論理がAI実装に対する受容態度の競合因として働くというものである。

### 「良い生」のビジョンと統治の分裂(ソース4)

ZhangとBodeは、Flockhartの「良い生のビジョン」概念を用いて、軍事領域のAI統治がなぜ分裂し続けるのかを分析した。

- 米国には、Big Tech、MAGA、リベラルの3つのビジョンがある。
- 中国には、技術ナショナリズムと人間中心の2つのビジョンがある。
- 米国のリベラルと中国の人間中心のビジョンの間には、一定の収束の可能性がある。
- 中国の技術ナショナリズムと、米国のBig TechおよびMAGAのビジョンとの間には、深い緊張が残る。

ビジョンは社会の深い基盤に根ざすため、制度対立は、ビジョンが収束する場面でのみ解消できると整理されている。

### 規律による規範の再生産と脱規律化(ソース3)

Vinkらは、サービスデザインが現状維持を再生産し、他者を支配的な社会的期待へ正常化してきたと批判する。ノルウェーの病院ベースのメンタルヘルスサービスとの7週間の実験的な協働に基づき、クィア理論を用いた枠組みを提示した。この枠組みは、規律を遊び、乱すことで生じる失敗に注目する。そのうえで、習熟に抵抗する「学び直し、やり直し、忘却」という開かれた方向を示す。

### 補助的な文脈(ソース2、5、6)

- ホテル業のチャットボット導入に関する概念研究(ソース2)は、顧客満足の向上とともに、雇用代替、データプライバシー、機械的共感の欠如という課題を挙げる。そして、人間と機械の二重のサービス枠組みが必要だと結論する。サービス品質と雇用維持という異なる価値の両立が課題になっている。
- Chengの研究(ソース5)は、AIが国家間のインフラや戦略的相互作用を再編し、分断されたガバナンス体制を生むと論じる。
- 銀行AI転換の準備度指数(ソース6)は、金融包摂と政府のAI能力を統合して国家の準備度を測る。制度的な前提条件の違いが、国ごとの受容の差になりうることを示す。

なお、ソース2、5、6は本概念を直接扱うものではなく、関連する文脈としての位置づけにとどまる。

## AI Nativeな設計への示唆

1. **論理の棚卸しを導入前に行う。** 影響を受ける職種、組織、国家がどのような正当性基準を持つかを明示する。受容を単一の「使いやすさ」指標だけで見積もらない。
2. **評価を職種別に分けて設計する。** ソース1のように、職種ごとに技術と接触する場を用意し、論理の違いを可視化する。平均化した満足度で見えなくなる対立を残す。
3. **収束できる層と、できない層を区別する。** 価値ビジョンに根ざした対立は、技術的な調整では解消しにくい。収束の余地が見込める部分から合意を積み上げ、残る分裂は、共存できる仕組みとして設計する。
4. **役割分化を前提にする。** 人間と機械の役割分担を明確にし、複数の価値を同時に守る。
5. **自らの規範の再生産を疑う。** 設計の規律や専門分野が、特定の規範を無自覚に固定していないかを点検し、必要に応じて脱規律化の手法で別の可能性を開く。

## 関連コンセプト

- [[paradox-management-of-competing-legitimacy-logics]] — 競合する正当性ロジックを解消せず、逆説として管理する視点
- [[digital-transformation-tensions]] — 部門間・組織間の対立という組織内の現れ方
- [[technology-acceptance-and-ai-resilience]] — 技術受容とレジリエンスの関係
- [[technology-acceptance-model-and-ease-of-use]] — 使いやすさを軸にした受容モデル。論理の競合とは対照的な単一指標的視点
- [[psychological-climate-and-fairness-mediated-acceptance]] — 公正認知を介した受容
- [[laws-and-ethical-principles]] — 軍事AI統治における法と倫理の原則
- [[scale-invariant-tradeoffs-in-autonomous-systems]] — 規模を変えても現れるトレードオフの構造

## 参考ソース

1. Silvia Rizzi, Stefano Fait, Mattia Franzin, Leonardo Sanna (2026). *How professional logics shape AI implementation in mental healthcare: a qualitative study of an LLM-enhanced chatbot*. File: raw/papers/marketing/how-professional-logics-shape-ai-implementation-in-mental-healthcare-a-qualitati.md
2. Ph.D Research Scholar Ms. R. Keerthana (2026). *Opportunities and Challenges of Technology Adoption in Customer Service in the Hotel Industry - A Conceptual Study*. File: raw/papers/marketing/opportunities-and-challenges-of-technology-adoption-in-customer-service-in-the-h.md
3. Josina Vink, Daphne Chan, Enrique Encinas, Shreya Bhattacharya (2026). *Undisciplining service design: Towards a grammar of possibility*. File: raw/papers/marketing/undisciplining-service-design-towards-a-grammar-of-possibility.md
4. Qiaochu Zhang, Ingvild Bode (2026). *Governing AI in the military domain in a multi-order world: China, the US, and visions of the "good life"*. File: raw/papers/neuroscience/governing-ai-in-the-military-domain-in-a-multi-order-world-china-the-us-and-visi.md
5. Eric C. K. Cheng (2026). *Artificial Intelligence and the Transformation of Global Order: Toward Algorithmic International Relations*. File: raw/papers/neuroscience/artificial-intelligence-and-the-transformation-of-global-order-toward-algorithmi.md
6. Sevinj Abbasova, Tetiana Vasylieva, Mehriban Aliyeva, Leyla Huseynova, Emiliya Ahmadova (2026). *National readiness for the transformation of digital banking from mobile applications to AI-driven services: A cross-country composite index*. File: raw/papers/marketing/national-readiness-for-the-transformation-of-digital-banking-from-mobile-applica.md
