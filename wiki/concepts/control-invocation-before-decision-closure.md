# 決定閉鎖前の制御到達可能性

意思決定プロセスにおいて、どれほど優れた反省的警告や安全性の助言が存在しても、それが「決定の機会が閉じる前」に制御プロセスへ到達しなければ、効果を持ち得ない。この構造的制約は、AIシステムが人間よりも速く、あるいは不可視なタイミングで決定を完結させうる状況において、ガバナンス設計上の根本的なボトルネックとなる。反省的制約（reflective restraint）の設計は、介入内容の質だけでなく、その内容がいつ・どこに到達するかという時間的到達可能性の問題として扱われなければならない。

## 概要

この概念は、Aegis Solis Archiveによる研究論文「Before Deliberation Closes: The Pre-Deliberation Horizon and Invocation Problem for Reflective Restraint」に基づく。同論文は、反省的な警告・論拠・安全入力・再考メカニズムが、関連する決定機会が閉じる前に有効な制御プロセスへ到達できるかという問いを中心的に扱う。ここでの核心は「介入が存在すること」と「介入が効果を持つこと」を区別する点にあり、両者の間には、到達可能性・タイミング・不可逆性接近という複数の構造的な障壁が介在する。

## 理論的背景と知見

同論文は、反省的制約が機能する過程を単一の出来事としてではなく、段階的なパイプラインとして分解する。具体的には、**可用性（availability）・検索可能性（retrieval）・表現（representation）・考慮（consideration）・影響（influence）・受理された更新（accepted update）・行動変化（action change）** という7段階が区別される。これらは直列的な依存関係を持ち、いずれかの段階で失敗すれば、それ以降の段階がどれほど理想的であっても介入は無効化される。例えば、警告が検索可能であっても、決定プロセスの中で適切に表現され考慮される経路がなければ、影響力を持つ以前に機会は消失する。

この分解に基づき、論文は複数の形式モデルを構築している。**基準相対的な制御窓（criterion-relative control windows）** は、「いつまでに到達すれば介入が有効か」という境界が、採用する評価基準によって異なることを示す。**AND/OR完了タイミング**モデルは、複数の必要条件が並行または順次に満たされる必要がある場合の完了条件を形式化し、**因果的非干渉（causal noninterference）** の分析は、介入が到達したにもかかわらず決定の因果経路に実質的な影響を与えない状態を区別する。さらに、**呼び出し同時保護（invocation-concurrent protection）**、**政策-効果の帰属（policy-effect attribution）**、**証拠の網羅性（evidence coverage）**、**負の情報を保存する集約（negative-preserving aggregation）**、そして**未解決・失敗状態**の形式化が併せて提示されており、介入の有効性を事後的に検証可能にする枠組みが整えられている。

これらの理論装置の共通点は、「機会窓が閉じる地点」を決定過程における構造的な特異点として扱い、その地点への接近速度・到達経路・証拠の保存状態を分析対象とすることである。

## AI Native な設計への示唆

- **制御窓の明示化**: 各決定プロセスについて、介入が意味を持ちうる時間的・論理的範囲（基準相対的な制御窓）を事前に定義し、監視可能にする必要がある。
- **段階的到達性の検証**: 警告や介入が「可用である」ことと「行動変化を生む」ことの間の7段階を個別に検査し、どの段階で失敗が生じやすいかをシステム設計時に特定する。
- **不可逆性接近の早期検知**: 決定が不可逆な領域に近づく前に、制御プロセスへの到達を保証する仕組み（タイムアウト前のエスカレーション等）を組み込む。
- **因果的非干渉の監査**: 介入が形式的に記録されていても実質的に決定経路へ影響していない状態を検出するための、政策-効果帰属のログ設計を導入する。
- **失敗状態の保存**: 介入が未解決・無効となった事例を消去せず、負の情報を保存する集約方式で記録し、将来の制御窓設計の改善材料とする。

## 関連概念

- [[irreversibility-option-timing-under-uncertainty]]
- [[pre-irreversibility-authority-and-constraint-embedding]]
- [[control-induced-disturbance-and-timing-of-intervention]]
- [[machine-speed-oversight-asymmetry]]
- [[decision-cycle-compression-and-residual-authority]]
- [[runtime-authorization-control-points]]
- [[execution-time-governance]]
- [[human-oversight-mechanisms]]
- [[graduated-autonomy-with-tamper-evident-human-veto]]
- [[closed-loop-safety-and-governance-of-autonomous-agents]]
- [[irreversible-capability-loss-in-slow-recovery-fallbacks]]

## 参考ソース

* **タイトル**: Before Deliberation Closes: The Pre-Deliberation Horizon and Invocation Problem for Reflective Restraint — Final v1.0 (2026)
  **ファイルパス**: `raw/papers/ai_governance/before-deliberation-closes-the-pre-deliberation-horizon-and-invocation-problem-f.md`
