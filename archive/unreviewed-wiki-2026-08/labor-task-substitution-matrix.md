# 労働タスク代替マトリクス

## 概要

**労働タスク代替マトリクス（Labor-Task Substitution Matrix）** は、職種をより細粒度のタスク束として分解し、AI等の技術がそれぞれのタスクに対して「代替」「補完」「新規創出」のいずれの経路を辿るかを体系的に評価する労働経済学的分析フレームワークです。

従来の職業単位での失業予測とは異なり、このマトリクスは**職務内のタスク粒度で技術的影響を評価する**ことで、より精密で実行可能な組織設計が可能になります。AI Native社会では、職種そのものの消滅よりも、職務内容の急速な再構成が課題となるため、このフレームワークは組織の適応戦略を立てる上で不可欠です。

## 理論的背景

### タスク指向アプローチの台頭

従来、労働経済学は「職業（occupation）」を単位として自動化の影響を分析していました。しかし、**Autor, Levy, Murnane (2001)** の『The Skill Content of Recent Technological Change』は、職業内部のタスク構成に目を向けることの重要性を実証的に示しました。同じ「会計職」でも、ルーチン的な計算タスクと判断的な分析タスクが混在しており、技術はこれらに異なる影響をもたらすということです。

### 代替・補完・新規創出の三層構造

**Acemoğlu & Restrepo (2019)** の『Automation and New Tasks: How Technology Displaces and Reinstates Labor』は、自動化技術の労働への効果を三つのカテゴリーに整理しました：

1. **代替（Displacement）**: AIが従来の人間労働を完全に置き換えるタスク。例えば、定型データ入力、単純な分類作業など。

2. **補完（Complementarity）**: AIが人間の生産性を向上させるタスク。医師による診断にAI診断支援が加わることで、診断精度と処理速度が同時に向上する場合。

3. **新規創出（Task Reinstatement）**: 技術進展によって新たに出現するタスク。生成AIの登場により「プロンプト・エンジニアリング」「AIアウトプット品質検証」といった職務が新規に創出されました。

### マトリクス構造の実装

労働タスク代替マトリクスは、次のような二次元構造を持ちます：

| タスク | 認知負荷 | 自動化難度 | AI対応経路 | 必要な人間役割 |
|--------|--------|---------|----------|------------|
| 定型分析 | 低 | 低 | 代替 | なし or 監視 |
| 複雑判断 | 高 | 高 | 補完 | 最終意思決定 |
| 創造的企画 | 高 | 高 | 新規創出+補完 | 領域専門家+AI指揮 |
| 対人交渉 | 中 | 中 | 補完 | プロセス所有者 |

この構造により、組織は職務内のすべてのタスクについて、AIをどのように配置すべきかを明示的に検討できます。

## AI Nativeな設計への示唆

### 1. タスク再配置の戦略設計

AI Native組織では、職種ごとの「廃止 or 温存」という二者択一ではなく、**タスク粒度での再配置戦略**を策定すべきです。例えば、営業職の場合：

- **代替タスク**: 見込み客データベース管理、初期接触メール作成
- **補完タスク**: 提案資料の根拠データ生成、顧客ニーズ分析支援
- **新規創出タスク**: AIレコメンドの妥当性判定、顧客信頼構築でのAI活用企画

このマトリクスに基づいて人的配置を設計すると、組織全体のスキル要件が明確になります。

### 2. [[bounded-rationality-augmentation|限定的合理性の拡張]] との連携

労働タスク代替マトリクスは、個々の意思決定者がAIによってどの程度の認知負荷軽減を得られるかを予測するツールとなります。高度な判断タスクはAIの補完により、ヒューマンエラーが減り、意思決定の質が向上します。

### 3. [[mixed-initiative-orchestration|混合主導的オーケストレーション]] の実装基盤

タスクの「代替」「補完」「新規創出」の分類は、人間とAIがどのように協働すべきかを設計する際の出発点です。補完タスクでは、AIが推奨案を提示し人間が最終判定する「ループ」が有効です。

### 4. スキル再開発の的確な対象設定

代替タスクに従事していた労働者には、新規創出タスクやAI監視タスクへの転職支援が必要です。マトリクスにより「どのスキルセットが将来必要か」が事前に可視化できるため、効率的な教育投資が可能になります。

### 5. [[techno-institutional-transition-analysis|技術制度移行分析]] との統合

マトリクス分析は技術的な可能性だけでなく、制度的制約も考慮すべきです。法規制により「AIが最終決定を下すことは許可されない医療診断」のようなタスクは、永続的に「補完」のみに止まります。組織は制度環境を前提にマトリクスを設計する必要があります。

## 関連コンセプト

- [[agentic-era-task-decomposition|エージェンティック時代のタスク分解]]: AI時代に職務をタスク単位で再定義するアプローチ
- [[mixed-initiative-orchestration|混合主導的オーケストレーション]]: 人間とAIの協働設計
- [[bounded-rationality-augmentation|限定的合理性の拡張]]: 認知支援としてのAI活用
- [[dynamic-capability-regeneration|動的能力の再生成]]: 組織スキルの持続的な進化
- [[sociotechnical-coevolution|社会技術的共進化]]: 技術と組織の相互適応

## 参考ソース

- Autor, D., Levy, F., & Murnane, R. J. (2001). "The Skill Content of Recent Technological Change: An Empirical Exploration" (raw/papers/economics/the-skill-content-of-recent-technological-change-an-empirical-exploration.md)

- Acemoğlu, D., & Restrepo, P. (2019). "Automation and New Tasks: How Technology Displaces and Reinstates Labor" (raw/papers/economics/automation-and-new-tasks-how-technology-displaces-and-reinstates-labor.md)

- Acemoglu, D., & Restrepo, P. (2018). "Artificial Intelligence, Automation, and Work" (raw/papers/economics/artificial-intelligence-automation-and-work.md)

- Dwivedi, Y. K., Hughes, L., Ismagilova, E., Aarts, G., & Coombs, C. (2019). "Artificial Intelligence (AI): Multidisciplinary perspectives on emerging challenges, opportunities, and agenda for research, practice and policy" (raw/papers/economics/artificial-intelligence-ai-multidisciplinary-perspectives-on-emerging-challenges.md)