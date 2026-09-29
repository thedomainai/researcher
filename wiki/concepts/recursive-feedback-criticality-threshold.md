# 再帰的フィードバックの臨界閾値と自己増幅

## 概要

システムが自らの出力を入力として循環させるとき、フィードバックの強さと、さらなる進展の難しさの比が臨界値を超えるかどうかで、挙動が質的に分岐する。超えれば改善の効果が周期ごとに複利的に積み上がる自己増幅レジームに入り、下回れば効果は周期ごとに弱まる減衰レジームにとどまる。

この原理は特定の対象に依存しない。AIの研究開発、人間とAIの学習ループ、AI介在環境での認識形成など、出力が次の入力になる構造であれば成立する。AI Nativeな社会設計では、AIが自分自身の開発や人間の認知、組織の意思決定に組み込まれる。そのため、どの循環がどちらのレジームにあるかを把握し、設計上の介入点を見定める必要がある。

## メカニズム

### 構造的原理

対象を入れ替えても成り立つ構造は、次の3要素に整理できる。

1. **循環**:ある周期の出力(能力向上、学習状態の変化、生成物)が、次の周期の入力(研究生産性、学習条件、観察材料)になる。
2. **増幅項**:出力が入力を改善する強さ(フィードバック強度)。
3. **抵抗項**:進展が進むほど次の進展が難しくなる度合い(進展の困難度の増大)。

増幅項と抵抗項の比を再生産数として定義すると、伝染病学の基本再生産数と同じ形の臨界条件が得られる。

- 再生産数 > 1:各周期の効果が次周期に持ち越されて複利的に増える(自己増幅)
- 再生産数 < 1:効果は周期を経るごとに弱まる(減衰)

### 対象を入れ替えた読み方

- **技術(AI R&D)**:AIが次世代AIの開発に使われる場合、能力向上が研究生産性を押し上げる。一方で研究課題は次第に難しくなる。
- **人間**:AI仲介環境では、AIの出力が人間の観察や認知を形づくり、その認知が次のAIへの入力になる。
- **組織・集団**:大規模な人間-AI相互作用の集団挙動には、状態変数で記述できる再現可能な動力学が現れる。

### 臨界は能力水準ではなく構造で決まる

重要なのは、遷移がループの構造に依存し、特定の能力水準で起きるとは限らない点である。そのため、加速が目に見える前に自己増幅レジームへ入ることがあり得る。能力の絶対水準を見るだけでは、臨界への接近を検知できない。

## 理論的背景

### 再帰的再生産数 R_AI(Burtsev, 2026)

このモデルは、AI能力成長率が次の3つに依存すると記述する。

- 基礎的な研究生産性
- 再帰的フィードバック
- 研究進展の困難性の増大

ここから導かれる再帰的再生産数 R_AI は、フィードバックの強さと、さらなる進展が難しくなる速さを比較する量である。R_AI > 1 なら改善の効果が開発周期をまたいで複利的に積み上がり、R_AI < 1 なら効果は周期ごとに弱まる。遷移はAI R&Dのフィードバックループの構造に依存する。

### 第2階サイバネティクスと観察者依存性(Abaker, 2026)

生成AIエコシステムを第2階サイバネティクスの視点から分析した論考である。フォン・フェルスターの観察者依存性、再帰性(リフレクシビティ)、非自明システム、倫理的命令の概念を再検討している。核心的な知見は、AI仲介環境における認識が観察者依存性のために不可避的に変容するというものである。ここでは観察する主体もループの一部であり、観察と構成が互いに再帰的に規定し合う。この論考は人間中心のガバナンス枠組みを提示している。

### 閉ループ人間-AI系の巨視的動力学(Wu et al., 2026)

297,915人の学習者の適応型チュータリング履歴を用い、モデル適合の前に意味的な秩序変数を定義し、ユーザー非重複コホートで検証している。状態には再現可能な盆地状の流れと、状態により異なる準安定的な動態が見られる。4項の条件付きメカニズムは集団のドリフトを r = 0.946 で再現した(学習者ブートストラップ95%信頼区間 0.935–0.955)。閉ループ系の巨視的挙動が、観測可能な状態変数で記述・再現できることを示す実証知見である。

### 知能の組織的閾値(Boko, 2026)

AIを、知能が生物的基質を超え始める組織的閾値として捉える仮説的な解釈である。生物進化が人間の認知を生み、人間の認知が非生物的な認知システムを生み始めたという再帰的な連鎖を、新たな進化的動態の可能性として論じている。著者はこれを確立した科学的結論ではなく仮説として提示している。

## AI Nativeな設計への示唆

1. **能力水準ではなくループ構造を監視する**:臨界は特定の能力水準で起きるとは限らない。フィードバック強度と進展困難度の比に相当する指標を、対象ループごとに定義して追跡する。
2. **状態変数を事前に定義する**:閉ループ系の動力学は、意味的な秩序変数を先に定義して検証することで再現可能になる。運用前に観測すべき変数を決めておく。
3. **増幅させたいループと減衰させたいループを区別する**:学習支援のように増幅が望ましいループもあれば、誤りやバイアスの循環のように抑えたいループもある。いずれも再生産数の観点で設計目標を明示する。
4. **観察者を系の内部に置く**:人間は循環の外にいる中立な観察者ではない。AI仲介環境では認識自体が変容するため、人間中心のガバナンスにこの再帰性を組み込む。
5. **抵抗項を意図的に設計する**:検証や機能分離などの抑制機構は、抵抗項を高めて再生産数を下げる手段として位置づけられる。

## 関連コンセプト

- [[feedback-loops-system-dynamics]] — フィードバックループの一般的な動態理解
- [[multistability-and-tipping-in-coupled-networks]] — 転移点と多安定性の観点からの臨界遷移
- [[dynamic-capability-amplification]] — 能力の増幅という観点
- [[agency-as-recursive-transition-law-update]] — 再帰的な更新としてのエージェンシー
- [[consciousness-and-recursive-self-modeling]] — 再帰的自己モデリング
- [[structural-separation-and-hierarchical-verification]] — 誤差伝播を抑える抵抗項としての構造設計
- [[self-monitoring-feedback-and-adaptive-plasticity]] — 自己監視フィードバック
- [[generative-ai-augmented-feedback]] — 生成AIによるフィードバックの拡張
- [[finite-cognitive-resources-and-load-thresholds]] — 負荷閾値による非線形破綻

## 参考ソース

1. Ahmed Abdallah Abaker (2026)「Generative AI as a recursive observation system: a second-order cybernetic perspective on cognitive autonomy and human-centered governance」
   File: raw/papers/complexity_science/generative-ai-as-a-recursive-observation-system-a-second-order-cybernetic-perspe.md
2. Minlin Wu, Xu Fang, Yicheng Zhang, Chenyu Zhou, Zhiyi Liu (2026)「Reproducible macroscopic dynamics in a closed-loop human-AI learning system」
   File: raw/papers/complexity_science/reproducible-macroscopic-dynamics-in-a-closed-loop-human-ai-learning-system.md
3. Mikhail Burtsev (2026)「Recursive Criticality of AI Self-Improvement」
   File: raw/papers/complexity_science/recursive-criticality-of-ai-self-improvement.md
4. Irfan Boko (2026)「ARTIFICIAL INTELLIGENCE: A THRESHOLD TOWARD UNIVERSAL INTELLIGENCE?」
   File: raw/papers/complexity_science/artificial-intelligence-a-threshold-toward-universal-intelligence.md
