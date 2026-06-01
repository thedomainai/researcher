# トポロジカル量子誤り訂正

トポロジカル量子誤り訂正（Topological Quantum Error Correction, TQEC）は、大規模かつ実用的な量子コンピュータを実現するための最も有力な量子誤り訂正手法の一つです。

従来の量子システムは、周囲の環境との相互作用によるデコヒーレンス（量子状態の崩壊）に対して極めて脆弱です。トポロジカル量子誤り訂正では、量子情報を単一の物理量子ビットに保存するのではなく、2次元格子などの多体系における非局所的なトポロジカル自由度（系のマクロな幾何学的性質）に分散して符号化します。これにより、局所的なノイズや乱れに対して極めて高い耐性を持つ、堅牢な「トポロジカル量子メモリ」の構築が可能になります。

---

## 理論的背景と詳細

トポロジカル量子誤り訂正の核となる概念と、これまでの研究成果は以下の通りです。

### 1. 表面符号（Surface Codes）とスタビライザー
アレクセイ・キタエフ（Alexei Kitaev）らによって提唱された「表面符号（サーフェス符号）」は、トポロジカル量子誤り訂正の代表的なアプローチです。
* **物理配置**: 物理量子ビットを2次元の格子状（表面）に配置します。
* **スタビライザー測定**: 各量子ビットのサブセット（隣接する複数ビット）に対して局所的な「スタビライザー測定（Stabilizer Measurement）」を繰り返し実行します。これにより、符号化された量子状態を破壊することなく、発生したエラー（反転や位相ズレ）のみを検出・特定します。
* **ホモロジーサイクル**: 符号化された論理量子操作は、表面の非自明なホモロジーサイクル（トポロジカルな閉路）に対応しています。エラーがこのサイクルを横断して繋がらない限り、論理情報は完全に保護されます。

### 2. 高い誤り許容しきい値（Error Threshold）
トポロジカル量子誤り訂正が極めて実用的とされる最大の理由は、その**エラーしきい値の高さ**にあります。
* システムのエラー率が特定の「臨界値（しきい値）」を下回っている場合、格子サイズ（物理量子ビット数）を大きくすることで、論理エラー率をいくらでも任意に小さく抑えることができます。
* 物理ゲート、量子ビット準備、測定、ストレージのすべてにエラーを仮定した現実的な2次元ローカルアーキテクチャモデルにおいて、**約0.75%** という実用的な高しきい値が達成可能であることが示されています。
* この相転移現象は、無秩序（ディスオーダー）を伴う3次元 $Z_2$ 格子ゲージ理論として物理学的に正確にモデル化され、解析されています。

### 3. 論理量子ビットの操作とブレイディング
2次元配列上に構成された論理量子ビットは、物理的に「穴（欠陥）」を作ることで表現されます。
* これらの論理量子ビットは、配列上を物理的に移動（移動経路に沿ったスタビライザーの書き換え）させることができます。
* 論理量子ビット同士を互いに交差・周回させる**ブレイディング（Braid Transformation/編み込み操作）**を行うことで、量子計算に必要な「CNOTゲート（制御NOTゲート）」などの論理2量子ビットゲートをトポロジカルに（幾何学的ノイズに依存しない形で）実行できます。
* 単一量子ビット操作（アダマールゲートや $S$ ゲートなど）と組み合わせることで、ユニバーサルな量子計算が構成されます。

### 4. 超伝導量子回路による実証
トポロジカル量子誤り訂正は理論に留まらず、近年実験的な実証が進んでいます。特に超伝導量子ビットを用いた回路において、スタビライザー測定を繰り返し実行することで、量子状態を繰り返し検出・保存するプロセスが実際に稼働し、その有効性が検証されています。

---

## 関連概念

* [[量子誤り訂正]]
* [[トポロジカル量子メモリ]]
* [[表面符号]]
* [[スタビライザー符号]]
* [[デコヒーレンス]]

---

## 参考ソース

* **Surface codes: Towards practical large-scale quantum computation**  
  Austin G. Fowler, M. Mariantoni, John M. Martinis, A. N. Cleland (2012)  
  *Path: raw/Surface_codes_Towards_practical_large_scale_quantum_computation.md*
* **Topological quantum memory**  
  Eric Dennis, Alexei Kitaev, Andrew Landahl, John Preskill (2002)  
  *Path: raw/Topological_quantum_memory.md*
* **Quantum error correction for quantum memories**  
  Barbara M. Terhal (2015)  
  *Path: raw/Quantum_error_correction_for_quantum_memories.md*
* **State preservation by repetitive error detection in a superconducting quantum circuit**  
  J. Kelly, R. Barends, Austin G. Fowler, A. Megrant, E. Jeffrey (+17) (2015)  
  *Path: raw/State_preservation_by_repetitive_error_detection_in_a_superconducting_quantum_circuit.md*
* **Fault-Tolerant Quantum Computation with High Threshold in Two Dimensions**  
  Robert Raussendorf, Jim Harrington (2007)  
  *Path: raw/Fault_Tolerant_Quantum_Computation_with_High_Threshold_in_Two_Dimensions.md*