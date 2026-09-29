# システム境界に帰属する能力と合成知能

## 概要

システム境界に帰属する能力と合成知能とは、知能や能力を単一の構成要素(1つのモデル、1人の人間、1つのツール)の属性としてではなく、複製された下位ユニット、ツール、記憶、人間が結合した**システム全体の性質**として捉える原理である。能力は、複数ユニットの合意形成と統合の過程から創発する。

この原理は Tier 1(不変原理)に位置づけられる。ソースでは、大脳皮質の柱状ユニット、人間と複数の生成AIからなるチーム、AI技術スタックを組み上げる組織など、対象の異なる文脈で同じ構造が記述されている。

AI Nativeな設計にとって重要なのは、「どのモデルが賢いか」という問いから「どの結合系がどのような能力を持つか」という問いへ、設計の単位を移す点にある。能力を評価・設計・統治する際の分析単位が変わるため、アーキテクチャ、組織設計、責任の置き方が連動して変わる。

## メカニズム

以下は、対象(神経組織、人間、AI、組織、技術)を入れ替えても成り立つ構造的原理として整理したものである。

1. **ユニットの複製と役割分化**
   同種の汎用ユニットが複製され、それぞれが部分的な知覚・モデルを持つ。AIチームでは、複数の汎用モデルが役割を分けて配置される。
2. **合意形成による創発**
   個々のユニットの出力は単独では部分的である。ユニット間の結合を通じて合意に至ることで、システムとしての判断や認識が成立する。
3. **結合系への能力の帰属**
   能力は個々の構成要素ではなく、人間、複数モデル、外部記憶、ツール、環境フィードバックの結合配置に帰属する。分析単位は「結合された配置」である。
4. **経路依存的な統合**
   結合は履歴に依存して形成される。暗黙の協調スキルや永続的な記録が蓄積され、同じ構成要素でも統合の経路が異なれば能力も異なる。
5. **環境との閉ループ**
   観察、表現、行動を経て独立した環境に戻る閉ループが、システムの能力を検証し更新する。
6. **判断権の所在**
   結合系のなかで判断の最終的な主権をどの層が持つかを明示する。ソース[5]は、人間が主権層にとどまる「判断を放棄しない拡張」を原則としている。

この記述装置は、個人、組織、人間とAIの混成チームのいずれにも同様に適用できるとされる。

## 理論的背景

### 皮質の複製ユニットと合意形成(ソース[1])

Hawkins、Leadholm、Clayによる Thousand Brains Theory 2.0 は、Mountcastleの仮説を出発点とする。哺乳類の知能の基盤は、汎用計算ユニットである皮質コラムの複製にあるという仮説である。Thousand Brains Theory では、各コラムが感覚運動システムであり、複数の動きにわたる感覚入力を統合して物体の構造化モデルを学習するとされる。従来の研究は、コラム内部の計算と、長距離結合による素早い合意形成に焦点を当ててきた。本論文は、階層的なフィードフォワード/フィードバック結合や視床を経由する結合といった、従来の理論が扱わなかった長距離結合の拡張を目的としている。知能が単一ユニットではなく、複製・階層化されたサブシステムの合意から創発するという構図が示されている。

### 分散認知としての生成AI協働(ソース[2])

Anisらは、分散認知の枠組みで、生成AIを用いた協働を「人、AIツール、共有された成果物にまたがる情報作業」と概念化した。学生を対象にしたフォーカスグループの主題分析では、学生が生成AIをアイデア出し、統合、推敲、言い換えにおける創造的・認知的パートナーとして戦略的に用いていることが示された。あわせて、チームの規範や教員の期待が、検証、説明責任、AI出力への許容される依存のあり方を形づくるとされる。分散した情報処理では、検証と説明責任が結合系の質を左右する。

### 知能を「組み上げる」設計(ソース[3])

Frenchのパネル提案は、組織がAIを採用する対象から設計する対象へと移りつつあると論じる。モデル、データ、ワークフローが相互接続されたシステムになるにつれ、課題は個別ツールの利用から知能の合成(composing intelligence)へ移る。そのための役割として AI Architect が提示される。セキュリティ脆弱性、誤用、ガバナンスといった、高度に統合された環境で生じるリスクも論点に含まれる。

### コンピテンシー構成としての組織変化(ソース[4])

Jabłońskiは、AI統合による組織変化を診断するコンピテンシーベースの枠組みを提案する。AI対応組織モデルの4段階類型を拡張し、各段階が技術指標とは独立に、従業員コンピテンシーの構成によって識別できると論じる。5段階の評価手順と12のコンピテンシー領域にわたる分類マトリクスが提示され、垂直方向の整合性ギャップと刷新の方向的非対称性がモデル間の移行を説明する。組織能力が技術の導入量ではなく、人の能力構成との結合配置によって定まるという含意がある。

### 結合認知体の枠組み(ソース[5])

Ehstandのアーカイブは、永続的な人間-人工認知チームを記述する研究枠組みを扱う。分析単位は、人間のオペレーター、複数の汎用モデル、外部記憶、ツール、環境フィードバックからなる結合配置であり、能力はこのシステム境界の性質として扱われる。暗黙の協調スキル、経路依存的な統合、永続的記録、モデルの役割分化、そして環境に戻る閉ループが記述要素である。なお同資料は限定公開のアーカイブであり、抜粋から確認できるのは枠組みの概要に限られる。

## AI Nativeな設計への示唆

- **評価単位を結合系にする**:個別モデルのベンチマークだけでなく、人、モデル群、記憶、ツール、環境を含めた配置全体で能力を評価する。
- **役割分化と合意の仕組みを設計する**:モデルに異なる役割を与え、出力を統合・照合する合意プロセスを明示的に組み込む。
- **記録と履歴を資産として扱う**:統合は経路依存的なので、永続的な記録や外部記憶を設計要素として維持する。
- **判断権の所在を明示する**:人間が主権層にとどまる構成を基本とし、拡張が判断の放棄にならないようにする。
- **検証と説明責任を結合系に組み込む**:分散した情報処理では、検証の規範と責任の所在を、チームや組織のレベルで定める。
- **統合能力を育成する**:AI Architect のような統合役割や、コンピテンシー構成の診断によって、ツールの導入量ではなく統合の質を管理する。
- **統合に伴うリスクを統治対象にする**:高度に統合された環境で生じるセキュリティやガバナンスの課題を、設計段階から扱う。

## 関連コンセプト

- [[adaptive-intelligence-emergence]] — 適応知能創発
- [[adaptive-intelligence-orchestration]] — 適応的知能オーケストレーション
- [[artificial-swarm-intelligence]] — 人工群知能
- [[bounded-diversity-adaptive-feedback-collectives]] — 限定的多様性と適応的フィードバックによる集合知
- [[capability-profile-based-task-allocation]] — 能力プロファイルに基づく役割分担と協働設計
- [[capability-realization-organizational-bottleneck]] — 組織的統合能力が価値を決めるボトルネック
- [[capability-contingent-absorption-and-progressive-layering]] — 組織能力依存の吸収と段階的レイヤリング
- [[bidirectional-human-machine-coupling-and-autonomy-boundary]] — 人間-機械の双方向結合と自律性・同意の境界設計
- [[capability-externalization-dual-effects]] — 能力外部化の二面性

## 参考ソース

1. The Thousand Brains Theory 2.0: An Extension for the Long-Range Connections of the Neocortical Heterarchy — Jeff Hawkins, Niels Leadholm, Viviane Clay (2026)
   File: raw/papers/operations_research/the-thousand-brains-theory-20-an-extension-for-the-long-range-connections-of-the.md
2. The New Normal? Collaborative Information Behavior with Generative AI — Sumra Anis, Shuyuan Mary Ho, Akerke Kuanysh, Subhasree Sengupta (2026)
   File: raw/papers/organization_science/the-new-normal-collaborative-information-behavior-with-generative-ai.md
3. The New AI Architect: Composing Intelligence Through AI Technology Stacks — Aaron M. French (2026)
   File: raw/papers/organization_science/the-new-ai-architect-composing-intelligence-through-ai-technology-stacks.md
4. AI-driven organizational change: a competency-based framework for classifying AI integration trajectories — Marek Jabłoński (2026)
   File: raw/papers/organization_science/ai-driven-organizational-change-a-competency-based-framework-for-classifying-ai-.md
5. Coupled Human-Artificial Team Cognition: A Restricted Methodological Archive (2026-08) — Andreas Ehstand (2026)
   File: raw/papers/organization_science/coupled-human-artificial-team-cognition-a-restricted-methodological-archive-2026.md
