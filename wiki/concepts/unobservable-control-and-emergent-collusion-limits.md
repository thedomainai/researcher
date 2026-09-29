# 可観測性・制御の原理的限界と創発的暗黙協調のリスク

## 概要

組織の境界を越えて相互作用する自律エージェント群では、完全な可視性(observability)や実行前の事前認可(ex-ante authorization)を原理的に実現できない場合がある。さらに、各エージェントが独立に学習しているだけでも、明示的な合意なしに暗黙の協調が創発しうる。この概念(Tier 1: 不変原理)は、制御設計が「完全に見えて、完全に止められる」という前提ではなく、限界を前提に組み立てられなければならないと主張する。

AI Nativeな社会設計では、エージェントが組織・市場・国境を越えて相互作用する。単一の組織が全体を把握して統制するモデルは成立しなくなるため、「どこまで見えず、どこまで制御できないか」を先に定義し、その上で検証・責任・介入の仕組みを設計する必要がある。

## メカニズム

以下の構造は、対象が人間・AI・組織・技術のいずれでも成立する。

1. **情報の非対称性**: 統治する側は、被統治システムの内部状態や相互作用のすべてにアクセスできない。組織境界の外側の相互作用は、どの単一主体からも完全には見えない。
2. **不可能性による制御の限界**: 観測に基づいて行為の可否を認可しようとしても、観測できる情報だけでは行為前の認可判断を再構成できない場合がある。認可の成立条件は、実装の工夫ではなく構造によって制約される。
3. **創発的な暗黙協調**: 個々の主体が自分の利益を目指して独立に学習・適応しても、反復的な相互作用の中で、誰も明示的に設計していない協調的な振る舞いが立ち上がる。個々の部品を点検しても、全体の逸脱は検出できない。
4. **不可逆性**: 創発した協調は、個別の主体の意図に還元できず、後から単純に切り分けて元に戻すことが難しい。
5. **正当性圧力下の検証崩壊**: 外部に向けた正当性を示す圧力が強いと、実質を伴わない象徴的な採用が続き、組織内の学習と検証の仕組みが弱まる。制御の限界は、検証を担う人間・組織側の劣化によっても拡大する。

これらが重なると、「見えない」「事前に止められない」「創発した協調を後から解けない」「検証する力も落ちる」という制御の四重の限界が生じる。

## 理論的背景

### 観測に基づく認可の不可能性と認可アーティファクト

Meymanによる論考(2026)は、「観測に基づく認可の不可能性」という結果を、実行前の認可を求める要件に適用する規制向けの応用ノートである。ここで導入される **Authorization Artifact Test** は、特定の規制体制に依存しない二段階の検査で、ある統治アーキテクチャが実行前認可要件のアーティファクト関連の閾値を原理的に満たしうるかを判定する。問いは次の二点である。

- 実行前に、行為に結び付いた判定(verdict)が存在するか。
- 独立した第三者が、認可アーティファクトとそれに結び付いた資料から、宣言された再現モード(State-ReplayまたはProtocol-Replay)の下で、被統治システムにアクセスせずにその判定を再構成できるか。

この枠組みは、事前認可を名目上掲げるだけでは足りず、判定が行為に結び付いて外部から再構成可能でなければならないことを示す。

### 電力市場における暗黙の共謀の創発

Seredyński and Tsaousoglou(2026)は、電力市場の入札主体が学習ベースのエージェントに置き換わる状況を扱う。他分野のアルゴリズム市場では、独立した学習だけで暗黙の共謀が生じうることが示されている。電力市場は寡占的で、少数の参加者が反復的に相互作用するため、構造的に非競争的な振る舞いが起きやすい。著者らは戦略的入札を「不完全な公的監視を伴う反復ゲーム」としてモデル化し、多エージェント強化学習で創発的な振る舞いを扱い、利潤にとどまらない多次元の基準を提案している。個々のエージェントに共謀の指示がなくても協調が創発しうる点が、可観測性の限界と直結する。

### 組織境界を越えるマルチエージェントのリスクと統制

Reidら(2026)は、AIエージェント同士が相互作用する際のリスクが組織境界を越えるとどう変化するかを整理する分析枠組みを示す。エージェントは組織内、パートナー・顧客・供給者のエージェント、公開インターネット上の未知の相手と相互作用する。失敗は相互作用そのものから生じうるため、相互作用が組織の外縁を越えると、単一の組織はそれを完全に見ることも、制御することも、統治することもできない。この枠組みは、最低限共有される統治の水準で定義される三つのデプロイメント階層を導入している。

### 正当性圧力と知識検証の崩壊

Wang and Zhang(2026, Tier 2)は、AIウォッシング(AI導入の誇張)を知識ガバナンスの失敗として概念化する。正当性圧力に駆動されて象徴的なAI採用が続くと、経営の注意が実質的な取り組みから逸れ、組織学習、知識の検証、能力開発が段階的に損なわれるという逐次的なプロセスとして描かれる。制御の限界は技術的要因だけでなく、組織の検証能力が空洞化することでも拡大する。

### 人間の認知的主体性

Edet(2026)は、AIが分析・統合・生成・推奨を担うほど、人間が問題設定、情報評価、機械出力への異議、判断、責任を保つことが課題になると論じる。認知的支援と認知的依存の区別が中心で、制御の最後の担い手である人間側の能力が維持されるかが問われる。

## AI Nativeな設計への示唆

- **限界を前提にした設計**: 完全可視性や網羅的な事前認可を前提とせず、見えない領域・止められない領域を明示したうえで、影響範囲の限定や事後対応を組み込む。
- **再構成可能な認可アーティファクト**: 事前認可は、行為に結び付いた判定が実行前に存在し、第三者が被統治システムなしに再構成できる形で残す。再現モードを宣言しておく。
- **個体監視から相互作用の監視へ**: 暗黙協調は個々のエージェントを点検しても見えない。市場結果や相互作用パターンなど、利潤以外も含む多次元の基準で集団レベルの振る舞いを評価する。
- **境界を越える統治水準の明確化**: 相手ごとに共有できる統治の最低水準を定義し、その水準に応じてリスクと統制を階層化する。
- **検証機能の空洞化を防ぐ**: 象徴的な採用への正当性圧力に対し、実質的な検証と学習が損なわれていないかを継続的に確認する仕組みを持つ。
- **人間の判断能力の維持**: 人間が問題を枠付け、機械出力に異議を唱え、責任を負う能力を保てるように、支援と依存の境界を設計する。

## 関連コンセプト

- [[interaction-emergent-coordination]] — 相互作用から創発する協調と逸脱の伝染
- [[computational-limits-forcing-decentralized-autonomy]] — 中央集約制御の限界が分散自律化を強いる
- [[incentive-compatible-control-of-hidden-agents]] — 隠れた能力・選好を持つ主体の制御
- [[capability-outpacing-control-gap]] — 能力拡大が制御を上回るギャップ
- [[coevolving-threat-defense-and-ecosystem-coordination]] — 生態系的協調ガバナンス
- [[decentralized-coordination-and-power-concentration]] — 分散協調の創発と権力集中
- [[emergent-governance-networks]] — 創発的ガバナンスネットワーク
- [[evidence-grounded-role-separated-agent-coordination]] — 検証の構造的分離
- [[decision-loops-and-layered-decentralized-control]] — 多層的な分散制御
- [[agentic-ai-memory-control]] — エージェントAIにおける記憶・制御・検証

## 参考ソース

1. The Authorization Artifact Test: Applying the Impossibility Result to Ex-Ante Authorization Requirements — Edward Meyman, 2026
   File: raw/papers/complexity_science/the-authorization-artifact-test-applying-the-impossibility-result-to-ex-ante-aut.md
2. AI agents in Algorithmic Electricity Markets: On the Emergence of Tacit Collusion — Jakub Seredyński, Georgios Tsaousoglou, 2026
   File: raw/papers/complexity_science/ai-agents-in-algorithmic-electricity-markets-on-the-emergence-of-tacit-collusion.md
3. Risks and Controls for Multi-Agent Systems: an analytical framework for deployment of AI agents across organisational boundaries — Alistair Reid, Simon O'Callaghan, Dustin Venini, Liam Carroll, Tiberio Caetano, 2026
   File: raw/papers/complexity_science/risks-and-controls-for-multi-agent-systems-an-analytical-framework-for-deploymen.md
4. AI washing as a knowledge governance failure in organizations — Yunjie Wang, Wei Zhang, 2026
   File: raw/papers/complexity_science/ai-washing-as-a-knowledge-governance-failure-in-organizations.md
5. The Human Intelligence Imperative: Human Cognitive Agency in the Age of Artificial Intelligence — Life Edet, 2026
   File: raw/papers/complexity_science/the-human-intelligence-imperative-human-cognitive-agency-in-the-age-of-artificia.md
