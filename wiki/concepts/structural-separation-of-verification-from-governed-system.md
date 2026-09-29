# 被統治系からの検証機構の構造的分離

## 概要

被統治系からの検証機構の構造的分離とは、自己改変や逸脱が可能な系に対して、統制・検証の機能を系の内部(系自身が到達できる空間)に置かず、権限・役割・実行経路を構造的に分離した外部の検証層として設ける、という設計原理である。Tier 1(不変原理)として位置づけられる。

この原理の要点は、内部に置かれた統制は「協力的な依頼」にとどまり、系がそれに到達できる限り無効化されうる、という点にある。統制が「アーキテクチャ上の制御」として機能するには、被統治系の到達範囲の外側に検証主体・実行経路・証拠が存在する必要がある。

AI Nativeな社会では、AIエージェントがツールやAPI、インフラに対する能動的な主体(プリンシパル)となる。プロンプトや出力フィルタのような「エージェント自身のランタイム内の統制」に依存した設計は、この原理に照らすと構造的に脆弱である。したがって、検証の分離は個別技術の選択ではなく、設計の前提条件として扱う必要がある。

## メカニズム

対象が人間・AI・組織・技術のいずれであっても成立する構造として、次の三つの要素に整理できる。

### 1. 到達可能性による制御の無効化

統制が被統治系の到達可能な空間にある場合、その系に影響を与える入力(あるいは系自身の操作)によって統制が迂回・改変されうる。ソース[3]は、エージェントのアドレス空間内にある制御は、それに影響を与える入力から到達可能であると述べ、これは自身のランタイムに十分に手が届くAIシステム全般(「escapable AI systems」と呼ばれる類)に一般化されるとしている。組織に置き換えれば、監査対象部門が自らの監査記録を書き換えられる状況と同型である。

### 2. 権限・役割の分離(職務分掌)

判断・実行・検証を別の主体や役割に割り当て、単一の主体が自分自身を承認できないようにする。ソース[5]のCAGFは、分離された役割、署名付きの判定(verdict)、暗号学的なイベントログを含む多エージェントのガバナンス記録を特徴としている。これは実行と判定を分ける職務分掌の実装例である。

### 3. 独立した証拠アーキテクチャ

検証の根拠となる証拠が、被統治系の信頼境界の外で検証可能でなければならない。ソース[3]は「制御対象システムの信頼境界の外で検証可能な、外部化された署名付き証拠」を要件の一つに挙げる。ソース[2]も、何が証明であり何をもって十分とするかを定める「客観的な証拠アーキテクチャ」を、統治対象ソフトウェアの構造要件の一つとしている。

## 理論的背景

### 外部認可機構の四つの性質(ソース[3])

ソース[3]は、認可機構が協力的依頼ではなくアーキテクチャ上の制御となるために満たすべき四つの性質を挙げている。

- プロセス分離
- 構造上唯一の経路における行動前(pre-action)の強制
- 要求レベルとシステムレベルの双方でのフェイルクローズ
- 制御対象の信頼境界外で検証可能な、外部化された署名付き証拠

同論文はこの層を「実行時のAIアラインメント(execution-time AI alignment)」と位置づけ、学習時アラインメント(RLHF、Constitutional AIなど)を補完するものとしている。

### 航空認証に見る三つの構造要件(ソース[2])

ソース[2]によれば、航空ソフトウェア認証は1992年以降、統治対象システムに三つの構造要件を運用化してきた。統治仕様と運用上の証拠との構造化された連結、運用文脈が変わったときに再検証を引き起こす文脈境界付きの妥当性、そして客観的な証拠アーキテクチャである。これらはDO-178CとDO-330に現れ、FAAとEASAの認証を通じて強制される。一方、システムプロンプトやAGENTS.md、ガバナンスポリシーといった個々のAIガバナンス文書には、これらの性質を内在的に求める既存の枠組みがないと指摘している。文脈の変化と再検証については [[context-bounded-validity-and-revalidation]] も参照。

### 高保証メモリ基盤における分離(ソース[1])

ソース[1]のAmagi-MEMは、安全重要な自律サイバーフィジカルシステム向けに、メモリ分割(INV-004)と証明可能なシャットダウン(INV-006)を強制する三層のメモリ階層を定義している。抜粋によれば、eFuseなどに置かれた不変の信頼の根(immutable roots of trust)を含め、アドレス可能・不可能な記憶領域の規範的契約を定めるものである。物理的・構造的に書き換え不能な層を設ける発想は、到達可能性による無効化への対処として読める。

### 速度の非対称性とメタガバナンス(ソース[4])

ソース[4]は、従来のGRCが人間の速度で動くのに対し、エージェント型AIは機械の速度で動くため、従来型の監督はアーキテクチャ上不適合になると論じる。対応として、AIガバナンスエージェントが運用エージェント群を自律的に監視・評価・介入する「メタガバナンス」を提案し、MOM-GS-MASとして16の専門ガバナンスエージェントを四つのSAGS柱にわたって配置している。ここでは検証層が被統治系と別のエージェント群として構成されている。詳細は [[machine-speed-oversight-asymmetry]] を参照。

### 形式仕様と宣言された規範の分離(ソース[5])

CAGFは、導出された構造(型付き公理コア A0–A10 と拡張)と、宣言された規範的選択(P0前提と文書化されたPolicyParameters)を分離している。何が導出されたもので何が選択されたものかを区別することで、検証可能な部分を明確にする設計である。

### 対照的な立場(ソース[6])

ソース[6]は、現行のガバナンスが事後的な検閲や外部出力フィルタに依存していると批判し、人間オペレータを「ゼロ点アンカー」とする統合的な枠組みを主張する。外部フィルタを批判的に扱う点で、本原理が要求する外部検証層とは論点が異なる。むしろ、外部フィルタのような事後的・表層的措置と、構造的に分離された実行前の強制とを区別して考える必要があることを示唆する材料として位置づけられる。

## AI Nativeな設計への示唆

- **統制を「依頼」から「構造」へ移す**: システムプロンプトや出力フィルタ、ガードレールライブラリなど、エージェントのランタイム内にある統制は、協力的依頼として扱う。拘束力が必要な統制は、プロセスを分離した外部層に置く。
- **唯一の経路上で行動前に強制する**: 行動が通る経路を認可層に限定し、事後の検出ではなく行動前に判定する。異常時は要求単位・システム単位ともにフェイルクローズとする。
- **証拠を信頼境界の外で検証可能にする**: 署名付きの証拠を外部化し、被統治系が自らの記録を改変・否認できない構造にする。
- **役割を分掌する**: 実行・判定・監査を別の主体に割り当て、単一エージェントが自己承認できない設計にする。
- **文脈変化を再検証のトリガーにする**: ガバナンス文書に、仕様と証拠の連結、妥当性が成り立つ文脈の範囲、十分性の基準を持たせる。
- **検証層の速度を被統治系に合わせる**: 機械速度で動く系には、人間速度の監督だけでなく、分離された自動の検証層を併置する。ただし人間による検証が持つバイアスの問題は [[human-verification-loop-bias-amplification]] のとおり別途考慮が必要である。
- **不変の基盤を設ける**: 書き換え不能な信頼の根や分割された記憶領域など、被統治系から到達できない層を最下層に置く。

## 関連コンセプト

- [[machine-speed-oversight-asymmetry]] — 機械速度と人間速度の統治非対称性。外部検証層が自動化を要する背景
- [[context-bounded-validity-and-revalidation]] — 文脈境界付き妥当性と再検証トリガー。証拠と妥当性の構造要件
- [[opacity-verification-gap]] — 不透明性と検証可能性の非対称ギャップ。内部からの検証が困難な理由に関わる
- [[surface-substrate-divergence]] — 宣言と実質の乖離。宣言された統制と実際の強制力の差を捉える視点
- [[human-verification-loop-bias-amplification]] — 人間による検証ループとバイアス増幅。人間を検証主体にする際の留意点
- [[structural-ai-framework]] — ストラクチャルAIフレームワーク
- [[system-instability-in-ai]] — AIにおけるシステム構造の不安定性

## 参考ソース

1. Amagi-MEM v1.1: Self-Protecting, Context-Aware Memory Architecture for High-Assurance AI Systems — Alexey Mikhailovich Burlai, 2026
   - File: raw/papers/ai_governance/amagi-mem-v11-self-protecting-context-aware-memory-architecture-for-high-assuran.md
2. Fifty Years of Specification Completeness: What Aviation Certification Tells AI Governance About Epoch Limits, Proof Surfaces, and the Structural Gap — Christo Zietsman, 2026
   - File: raw/papers/ai_governance/fifty-years-of-specification-completeness-what-aviation-certification-tells-ai-g.md
3. The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems — Seth Dobrin, Łukasz Chmiel, 2026
   - File: raw/papers/ai_governance/the-unfireable-safety-kernel-execution-time-ai-alignment-for-ai-agents-and-other.md
4. Meta-Governance of Autonomous AI Agents: A Policy-as-Code Architecture for Real-Time GRC in Multi-Agent Systems — Himanshu Joshi, Shivani Shukla, Sunita Kumari, Manas Joshi, 2026
   - File: raw/papers/ai_governance/meta-governance-of-autonomous-ai-agents-a-policy-as-code-architecture-for-real-t.md
5. CAGF: Constitutional AI Governance Framework — formal specification, governance record, and executable harness — Kristhian Manuel Jiménez Sánchez, 2026
   - File: raw/papers/ai_governance/cagf-constitutional-ai-governance-framework-formal-specification-governance-reco.md
6. Human & Ai Foundational alignment — Stieve, 2026
   - File: raw/papers/ai_governance/human-ai-foundational-alignment.md
