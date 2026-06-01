# 同質的マルチエージェント討論の限界とコスト

大規模言語モデル（LLM）の推論能力を向上させるアプローチとして、複数のエージェント間で推論プロセス（根拠）を共有し、投票によって最終決定を行う「マルチエージェント討論（Multi-Agent Debate）」が広く利用されています。この手法は、ピアレビュー（査読）の仕組みを通じてハルシネーションを抑制できるという仮定に基づいて導入されてきました。

しかし、2026年のBlaž Bertalanič氏とCarolina Fortuna氏の研究『*The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate*』は、この前提に疑問を投げかけました。同じモデルで構成された「同質的（Homogeneous）」なエージェント群が、ガイドラインなしに討論を行う場合、合意形成プロセス自体がコストとなるだけでなく、単独での自己修正（Isolated Self-Correction）よりも性能が劣るケースがあることを実証しました。

---

## 主な研究知見

本研究では、難易度の高い2つのベンチマーク（GSM-HardおよびMMLU-Hard）を用い、同質のエージェント10体（Qwen2.5-7B、Llama-3.1-8B、Ministral-3-8B）による3ラウンドの討論プロセスを詳細に分析しました。その結果、同質的マルチエージェント討論における失敗パターンとして、以下の3つのモデル依存型経路が特定されました。

### 1. おもねり同調（Sycophantic Conformity）
エージェントは他者の意見を批判的に検証することなく、多数派の回答を無批判に採用する傾向があります。この多数派への同調（Modal Adoption）は最大で85.5%に達し、誤った合意形成を促進する原因となります。

### 2. 文脈の脆弱性（Contextual Fragility）
他者の推論プロセス（ピア・ラショナール）を提示されることで、エージェントが以前のラウンドで導き出していた正しい推論が不安定化（デスタビライズ）され、誤った回答へと誘導されてしまう脆弱性が確認されました。

### 3. ノイズの混入
他の無関係な問題の推論プロセスを注入するコントロール実験（確率的ノイズコントロール）との比較において、ガイドなしの同質的討論が、無関係なノイズを提示された場合と同等、あるいはそれ以上に推論を阻害することが示されました。

### 結論としてのコストと優位性
本研究は、適切なガイドや異質性（Heterogeneity）を持たない同質的なエージェント間討論は、計算コストがかかる割に、個々のエージェントが独立して推論を修正する「単独での自己修正（Isolated Self-Correction）」よりも精度が低くなることを明らかにしました。合意形成のために支払うコスト（The Cost of Consensus）は、必ずしもパフォーマンスの向上を担保しないという警告となっています。

---

## 関連概念

* [[マルチエージェントシステム]]
* [[LLMのハルシネーション]]
* [[自己修正能力（Self-Correction）]]
* [[合意形成アルゴリズム]]
* [[AIガバナンス]]

---

## 参考ソース

* **タイトル**: The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate (2026)
* **ファイルパス**: `raw/The_Cost_of_Consensus_Isolated_Self_Correction_Prevails_Over_Unguided_Homogeneous_Multi_Agent_Debate`