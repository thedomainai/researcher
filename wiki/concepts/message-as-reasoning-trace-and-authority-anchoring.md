# メッセージは推論の痕跡である:信念モデリングと権限アンカー

## 概要

マルチエージェントシステムでは、エージェント間で交わされるメッセージを「客観的事実の伝達」とみなす設計が広く採られている。しかしソース群が共通して示すのは、メッセージは**送り手の主観的な推論の痕跡(trace)**であり、結論とともに送り手の信念・前提・権限状態を暗黙に背負っているという見方である。

この見方に立つと、協調の信頼基盤は次の4点で決まる。

1. 相手の隠れた推論をモデル化する能力(信念モデリング / Theory of Mind)
2. プランナーの可視状態の外にある権限情報の扱い
3. 複数システムの協調を支える主権的アンカー
4. 効率化圧のもとで進む記号体系の分化

AI Nativeな設計では、構文的に正しいメッセージが幻覚を伝播させたり、先着情報が根拠なく権威を得たり、人間に読めない言語が生じたりする。これらはプロトコル検証だけでは検出できない。したがって、メッセージを「証拠」として読む設計が必要になる。

## メカニズム

対象を人間・AI・組織・技術のいずれに入れ替えても成り立つ構造として整理する。

### 1. 情報の非対称性と推論の痕跡
受け手が見られるのは送り手の結論(メッセージ)だけで、そこに至る推論過程は隠れている。受け手は「送り手は何を信じているか」「その立場の者は何を信じるべきだったか」を推定して初めて、メッセージを安全に使える。これは人間の会話でも、組織内の報告でも、AI同士の通信でも同型である。

### 2. 権限情報と計画可視状態の乖離
意思決定に必要な権限・承認の情報が、計画主体から見える状態(ワークスペースやメモリ)の外にあると、見た目が同一でも安全な行動が正反対になりうる。組織で言えば、書類は同じでも決裁の有無で取るべき行動が変わる状況にあたる。

### 3. 主権的アンカー
複数の主体が非同期に協調する際、配送の成否ではなく「誰が何にコミットしたか」という台帳上の状態を真実の基準とする。権限は、アクセスできる記憶によって上限が定まり、署名付きの資格情報として外部化される。

### 4. 圧力下の記号体系の乖離
部分的な情報しか持たない主体が圧力下で通信すると、効率の良い記号体系が創発し、元の言語から乖離する。これは外部の監視者(人間を含む)にとって解読困難になりうる。

## 理論的背景

- **信念モデリング(Chergui et al., 2026)**: 6G無線アクセスネットワーク(RAN)をLLMエージェントが管理する状況を想定し、メッセージは送り手の推論の痕跡だと論じる。構文的に正しい報告がAIの幻覚を伝播させ、プロトコル検証では見えない連鎖障害を招きうる。受け手は行動前に、相手が何を信じているか、その立場なら何を信じるべきかをモデル化する必要がある(Theory of Mind)。認知チャネルをセルラー層(cellular sheaf)上でモデル化する枠組みから5つの設計原理を導き、その第一が「メッセージは送り手の隠れた推論の証拠である」である。マルチエージェントの耐性は各エージェントの信念モデリング能力に依存する、というのが中核的知見である。
- **主権アンカー(Liu, 2026)**: Civilization Framework は、宛先をエージェントではなく「文明」(1人の人間の主権者、永続的な台帳、交換可能なエージェント)とする。Embassy Protocol では、メッセージは台帳エンドポイントに非同期に届き、両側の台帳のコミットメント状態が真実の基準になる。権限は記憶に由来し、資格情報として外部化され、文明レベルの評判とは分離される。また、先に届いた情報が不当な権威を得る「時間的重み効果」を、事前登録された1,908試行の実験で1つのフロンティアモデルについて検証している(検証を除去した条件で先着の誤った上流の主張が影響を持つことが示唆されているが、抜粋は途中で切れており詳細な数値は確認できない)。
- **クロス基盤の権限ギャップ(Li et al., 2026)**: 権限状態が、プランナーから見えるワークスペースやメモリの外(ランタイム、レジストリ、承認サービス)にある状況を cross-substrate authority gap と呼ぶ。128セルの統制実験では、権限情報を欠いた候補証拠の最終的な意味的成功が0/32だったのに対し、生のレシートも型付き関係も32/32を達成した。改善は欠けていた権限事実によるもので、型付けによる計画精度の上積みは観察されていない。
- **創発言語(Stengel-Eskin et al., 2026)**: GlossoGen プラットフォームの SaveVeyru シナリオで、部分情報しか持たないエージェントが圧力下で通信すると言語進化が起きる。得られた言語は構成的かつ形態的に生産的で、LLMの英語的事前分布から乖離し、人間には理解不能になる。進化に必要な要因として効率化への圧力などが挙げられている。安全性とモニタリング可能性に含意がある。
- **信頼に基づく適応的開示(Ghoshal & Oechtering, 2026)**: 各エージェントが隠したい潜在目標を持ち、観察する敵対者が目標推論を試みる状況を扱う。動的な信頼関係に応じて確率的にメッセージ開示を調整する枠組みを提案し、合意性能と秘匿性のトレードオフを制御できる。ベースラインより敵対的な目標推論の精度を下げつつ、競争力のある合意効用を維持すると報告している。メッセージが送り手の内部状態を漏らす「痕跡」であることを、送り手側の視点から裏づける。
- **中心性と反射性(Silva, 2026)**: エージェント的AIをサイバー空間の統合層として、媒介中心性と攻防の速度非対称性から概念化する。委譲が進むほど中心性が高まる構造を示し、通信を担うエージェント層の重要性を補足する。

## AI Nativeな設計への示唆

1. **メッセージを証拠として扱う**: 受信内容を事実として直接採用せず、送り手の信念・立場・根拠を推定した上で採否を決める。構文検証に加え、意味的・認知的な妥当性の検証層を置く。
2. **権限情報を計画の入力に含める、または実行時に検査する**: 権限状態が可視状態の外にあるなら、観測を拡張するか、実行時に権限チェックを行う。上記の実験では、欠けていた権限事実の供給が成功率を決定的に変えた。
3. **アンカーを明示する**: 最終的な責任主体(人間の主権者など)と、コミットメントを記録する台帳を基準にする。配送の成功ではなく、双方の合意状態を真実とする。
4. **到着順による権威化を防ぐ**: 先着の主張に不当な重みが乗る危険があるため、検証手段を維持し、順序と正しさを切り離す。
5. **開示を信頼に応じて調整する**: 全情報を一律に開示せず、信頼関係に基づき開示量を制御し、推論漏洩と協調性能のバランスを取る。
6. **記号体系の分化を監視する**: 効率化圧が強い環境では、人間に読めない言語が生じうる。監査可能性を保つため、通信形式の制約や翻訳・検証の仕組みを設計に組み込む。

## 関連コンセプト

- [[execution-time-governance]] — 実行時の権限検査と委譲設計
- [[ai-decision-authority-restructuring]] — AI組み込みによる意思決定権限の再構成
- [[verification-to-authority-conversion-gap]] — 検証可能性から実効的権威への変換ギャップ
- [[pre-irreversibility-authority-and-constraint-embedding]] — 不可逆化前の権限判断
- [[structural-separation-and-hierarchical-verification]] — 階層的検証によるエラー伝播の抑制
- [[local-information-limits-and-decentralized-guarantees]] — 局所情報下の分散協調
- [[epistemic-authority-and-algorithmic-truth]] — 認識論的権威とアルゴリズム的真実
- [[decision-cycle-compression-and-residual-authority]] — 意思決定サイクルの圧縮と残余権限

## 参考ソース

1. Agents That Model Agents: Five Principles Toward a Theory of Mind for 6G Networks — Hatim Chergui, Carolina Fernández-Martínez, Mehdi Bennis, Merouane Debbah (2026)
   `raw/papers/complexity_science/agents-that-model-agents-five-principles-toward-a-theory-of-mind-for-6g-networks.md`
2. The Civilization Framework: Sovereign-Anchored Communication Between Personal Multi-Agent Systems — Guangjun Liu (2026)
   `raw/papers/complexity_science/the-civilization-framework-sovereign-anchored-communication-between-personal-mul.md`
3. Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems — Yang Li, Sergey Volkov, Hai Liu, Zongsi Xu, Xiyu Chen (2026)
   `raw/papers/complexity_science/beyond-agent-harnesses-cross-substrate-authority-for-multi-agent-systems.md`
4. GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions — Elias Stengel-Eskin, Newton Sander, Carlos Bonetti, Sasha Boguraev, James Bowler (2026)
   `raw/papers/complexity_science/glossogen-emergent-language-in-complex-multi-agent-llm-interactions.md`
5. Trust-Aware Adaptive Disclosure for Inference Privacy Preservation in Multi-Agent Networks — Puspanjali Ghoshal, Tobias J. Oechtering (2026)
   `raw/papers/complexity_science/trust-aware-adaptive-disclosure-for-inference-privacy-preservation-in-multi-agen.md`
6. Artificial Intelligence as the Nervous System of Cyberspace: A Conceptual Model of Agentic Centrality and the Reflexivity of Cybersecurity — Luiz Fernando Moraes Silva (2026)
   `raw/papers/complexity_science/artificial-intelligence-as-the-nervous-system-of-cyberspace-a-conceptual-model-o.md`
