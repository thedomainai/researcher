# アテンション機構の変種（Attention Mechanism Variants）

## 概要

アテンション機構はTransformerアーキテクチャの中核であり、LLMの能力を規定する基盤技術である。近年、効率性・長文脈対応・特定タスクへの適応を目的として、多数の変種が提案されている。

## 主要な設計軸

Sebastian Raschkaの整理によれば、アテンション変種は以下の設計軸で分類できる：

- **スパース性**: どのトークン間の関係を計算するか（全結合 vs. ローカル vs. ストライド）
- **線形化**: ソフトマックスの近似による計算量の削減
- **マルチヘッド構造**: ヘッド数、グループ化（GQA, MQA）
- **位置エンコーディング**: 相対位置（RoPE, ALiBi）vs. 絶対位置
- **KVキャッシュ最適化**: 推論時のメモリ効率化

## AI nativeなシステム設計への示唆

アテンション機構の設計選択は、コンテキストウィンドウの長さ、推論コスト、精度のトレードオフを規定する。AI nativeなシステムでは：

- 長文脈対応 → より多くの情報を一度に処理可能 → エージェントの自律性向上
- 効率的アテンション → 推論コスト低減 → より多くのエージェントの並列運用が可能
- ステアリング可能な表現 → ユーザーの意図に応じた情報の選択的注視

## ステアラブル視覚表現との接点

Steerable Visual Representations（Ruthardt et al.）は、テキストプロンプトで視覚エンコーダのアテンションを操作する手法である。通常のCLIPがテキストと視覚特徴を後段で融合（late fusion）するのに対し、視覚エンコーダの内部層にクロスアテンションでテキストを注入する（early fusion）。これにより、画像内の任意の対象に注意を向けつつ、汎用的な視覚表現の質を維持する。

この「外部からの操舵」という概念は、AI nativeなシステムにおける「人間がAIの注意をどう制御するか」という問題に直結する。

## 関連概念

- [[test-time-compute]] — アテンション機構の上に構築される推論の拡張
- [[coding-agents]] — アテンション機構を持つLLMを活用するエージェント

## 参考ソース

- Sebastian Raschka, "A Visual Guide to Attention Variants in Modern LLMs" — `raw/articles/a-visual-guide-to-attention-variants-in-modern-llms.md`
- Ruthardt et al., "Steerable Visual Representations" — `raw/papers/steerable-visual-representations.md`
