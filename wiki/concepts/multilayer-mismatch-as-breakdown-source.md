# 多層的不整合としての協働破綻

## 概要

多層的不整合としての協働破綻とは、人と自動システムの協働が失敗する原因を、単一の欠陥ではなく**複数の層にまたがる整合の欠如**として捉える考え方である。ソース[3]は、自動運転における人間と自動化のブレイクダウン(breakdown)が、ドライバーと自動化が「何ができるか(能力=fitness)」「何を期待するか(期待=expectation)」「何を意図するか(意図=intention)」の食い違いから生じると論じている。

AI Nativeな設計にとって重要なのは、次の点である。AIエージェントが人間の代わりに判断・実行する場面が増えるほど、「性能が高ければ協働はうまくいく」という前提は成り立たなくなる。能力が十分でも、期待が食い違えば過信や不信が生じ、期待が揃っても、複数の主体の意図が衝突すれば自動化は破綻する。そのため、整合は層ごとに設計し、層ごとに測定しなければならない。

## メカニズム

この原理は、ドライバーと車載自動化という具体例を超えて、「主体A」と「主体B」の協働一般に適用できる構造として整理できる。主体は人間・AI・組織・技術のいずれでもよい。

1. **能力層の整合**:各主体が現時点で何をどこまで遂行できるかが、相手・状況と噛み合っているか。ソース[3]は、双方の能力(fitness)を前提に制御を共有する(shared control)ことを重視している。
2. **期待層の整合**:各主体が相手の挙動や限界について持つ予測(心的モデル)が、実際と一致しているか。心的モデルの同期が失われると、能力が足りていても協働は破綻しうる。
3. **意図層の整合**:各主体が目指す目的が両立しているか。主体が複数(たとえば同乗者が複数いる場合)になると、意図は衝突しうるため、調停が必要になる。
4. **層間の欠如による破綻**:破綻はどれか一つの層の不整合でも起こりうるし、層をまたいで生じることもある。ある層だけを最適化しても他の層の不整合は残るため、層ごとの整合を独立に点検する必要がある。
5. **インターフェースによる媒介**:ソース[3]は、Human-Machine Interface and Interaction(HMII)が層をまたぐ不整合の緩和で決定的な役割を果たすとしている。双方向でマルチモーダルな情報の流れが、能力・期待・意図の整合を助けると述べている。

## 理論的背景

### Driver-Automation Alignmentフレームワーク(ソース[3])

van Nes、Ng Boyle、Bengler、Leeによる本フレームワークは、ドライバーと車両自動化の相互作用を、fitness・expectation・intentionに対応する層で記述する。ソースによれば、自動運転におけるヒューマン・オートメーションの破綻は、両者が「できること・期待すること・意図すること」の食い違いに由来することが多い。論文は、こうした不整合の可能性を示すために、六つの運転状況を提示している(詳細は本記事のソース抜粋の範囲外)。

### 測定の層(ソース[1])

Pengらによる、AutomotiveUI 2025でのワークショップの統合報告(work-in-progress)は、自動運転車における快適性と知覚された安全性の測定を扱う。専門家講演は主観的測定、客観・生理的指標、AI駆動モデルを扱い、その後グループ討議が行われた。ソース情報によれば、測定手法の実践は分野内で大きくばらついている。また、自動化の進行に伴って主観・客観・生理測定を組み合わせる必要が生じるものの、それらを統合する仕組みはまだ確立していない。整合を層ごとに測定するには、この統合の問題を避けて通れないことを示唆する。

### 複数ユーザー間の意図衝突(ソース[2])

Belzらの Sim-DSE は、車内の自動化が「できるだけ明示的入力を減らす」方向で構想される一方、複数の同乗者がいると、ユーザーの状態や期待の違いから自動化シナリオが衝突しうる点に取り組む。手法は、専門家ワークショップ(N=5)で関連する車内インタラクションを特定して意思決定空間をモデル化し、エージェント型AIフレームワークで1000通りの順列をシミュレートして、その自動化の根拠(reasoning)を導出するというものである。得られた結果と根拠は、人間による検証に付される。ソースの核心的知見は、衝突が、シミュレーション支援による推論の可視化で部分的に解決できるという点である。

## AI Nativeな設計への示唆

- **層ごとに設計目標を分ける**:能力・期待・意図それぞれについて、整合の設計項目と確認方法を持つ。単一の性能指標で協働の健全性を代表させない。
- **能力の提示と共有制御**:各主体の現在の能力を前提に、制御や役割の分担を決める(ソース[3]の shared control)。
- **心的モデルを同期させるインターフェース**:AIの状態・限界・意図を、双方向かつマルチモーダルに伝える。インターフェースは単なる操作画面ではなく、層間整合の中心的な手段として設計する。
- **意図衝突の調停を前提にする**:主体が複数いる環境では、自動化が一意の正解を持たないと想定し、意思決定空間を明示したうえで、シミュレーションによって根拠を可視化し、人間の検証を組み込む(ソース[2])。
- **多面的な測定**:主観・客観・生理指標を組み合わせつつ、統合方法が未確立であることを認識する。指標の文脈依存性も考慮する(ソース[1])。
- **適用範囲の留意**:本記事のソースはいずれも自動運転(車内)の文脈である。他領域への一般化は構造的な類推であり、実証は別途必要である。

## 関連コンセプト

- [[multilayer-sociotechnical-alignment-and-institutional-pacing]] — 多層の整合を社会技術・制度の水準へ広げた視点
- [[multilayer-interaction-determines-adoption-outcomes]] — 人・プロセス・制度の多層相互作用が成果を決める点で共通する
- [[generation-governance-impedance-mismatch]] — 層間の速度・能力の不整合という別の形
- [[source-attribution-and-reliance-miscalibration]] — 期待層における信頼較正の歪み
- [[prior-attitude-filtered-trust-formation]] — 期待(心的モデル)形成の偏りに関連
- [[assisted-performance-versus-retained-capability]] — 能力層での見かけと実態の乖離
- [[authority-bounding-by-parallel-independent-layers]] — 独立した層による設計上の歯止め
- [[finite-cognitive-resources-and-load-thresholds]] — 人間側の能力(fitness)の限界

## 参考ソース

1. Chen Peng, Pavlo Bazilinskyy, Yueteng Yu, Marieke Martens, Riender Happee (2026). *Experts’ and Community Insights on Measuring Comfort and Perceived Safety in Automated Driving: Synthesis of a Participatory Workshop*. File: `raw/papers/systems_engineering/experts-and-community-insights-on-measuring-comfort-and-perceived-safety-in-auto.md`
2. Jan Henry Belz, Kayoon Kim, Enrico Rukzio, Tobias Große-Puppendahl (2026). *Sim-DSE: Mediating Multi-User Automations in Cars through Simulation-Augmented Decision Space Exploration*. File: `raw/papers/systems_engineering/sim-dse-mediating-multi-user-automations-in-cars-through-simulation-augmented-de.md`
3. Nicole van Nes, Linda Ng Boyle, Klaus Bengler, John D. Lee (2026). *Aligning driver and automation: a layered framework of fitness, expectations, and intentions*. File: `raw/papers/systems_engineering/aligning-driver-and-automation-a-layered-framework-of-fitness-expectations-and-i.md`
