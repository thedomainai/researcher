# 決定時点への証拠拘束と説明責任の遡及不能性

意思決定の瞬間に証拠と方針バージョンを結合しておかなければ、事後にその因果的説明を復元することは構造的に不可能である。この原理は、行為主体が人間であろうとAIであろうと変わらず、事後救済ではなく事前設計としてガバナンスに組み込まれなければならない。AI Native な組織設計において、説明責任は「後から証明する能力」ではなく「決定時に記録を固定する仕組み」として捉え直す必要がある。

## 概要

AIが自律的に判断・推奨・実行を行う場面が増えるにつれ、失敗やインシデントが発生した際に「なぜその決定がなされたか」を説明する要請が高まっている。しかし説明責任は、決定が下された後にいくら調査を尽くしても再構築できるとは限らない。証拠は決定が下された「その瞬間」の性質であり、その時点で捕捉されなかった証拠は、事後にはもはや存在しない。組織が事後に行えるのは、実際の行動の再構成ではなく、残された断片からの信念の再構成にすぎない。この非対称性——決定時点でしか確保できない証拠と、事後には回復不能な説明責任——が本概念の核心である。

## 理論的背景と知見

この原理を最も明確に定式化しているのが、AI Incident Response Protocol(AIRP)である。AIRPは、signal・classify・contain・escalate・reconstruct・closeの6段階からなるAIインシデント対応・再構成プロトコルとして提示されており、Defensible AI Framework Registryのエントリ(REG-05)として位置づけられる。その中心的要件は、対応チームに対する手順ではなく、プラットフォームに対する設計制約であるとされる点が重要である。すなわち、あるインシデントが説明可能であるのは、その決定がなされた瞬間に、当時有効だった方針バージョンに結合された形で再構成に必要な証拠が存在していた場合に限られる。この要件は事後には満たしようがなく、それゆえにこそ「対応プロトコル」という事後的な文書の中に、事後には手遅れとなる中核条項として現れるという逆説が指摘されている。

Human, AI, and Organizational Performance(HAOP)フレームワークは、この原理を組織的な責任帰属の設計原則として拡張する。HAOPは、適応する人間・自らの表現と制約の中で最適化するAI・両者が機能する条件を規定する組織という3層構造を提示し、「Accountability by Control」という規律——責任を、関連する制御を実際に保持している役割に結びつけ続ける原則——を中核に据える。さらに、意思決定の節目に設計された制御境界(Verification Gates)を設け、根拠(source)・状態(state)・動態(dynamics)の3種のアンカーによって判断の裏付けを形式化する枠組みを提示している。これは、証拠拘束の要件を決定プロセスの構造そのものに組み込むアプローチといえる。

また、既存の人間設計による品質監視・インシデント対応フレームワークにエージェント型AIを後から導入した事例研究では、AI導入以前から存在していたガバナンスモデル・運用定義・品質分類・意思決定境界・人間レビューの責任範囲が前提とされ、AIはあくまでその運用モデルを拡張する存在として位置づけられている。ここでも、証拠の出所境界(source-of-truth boundaries)や分類・証拠ルールの明確化が、後付けではなく事前設計として扱われている点が一貫している。

## AI Native な設計への示唆

- **決定と証拠の同時結合を設計要件とする**: AIエージェントの判断・推奨・実行には、その時点の入力データ・使用モデル・方針バージョンを不可分に記録する仕組みを、機能実装と同時にプラットフォームへ組み込む必要がある。事後のログ整備では代替できない。
- **説明責任を「制御を保持する役割」に固定する**: Accountability by Controlの考え方に従い、責任の所在は決定を下した瞬間にその領域の制御を実際に持っていた主体(人間かAIかを問わず)に紐づけ、後から責任の所在を再解釈できる余地を最小化する。
- **意思決定の節目にVerification Gateを設ける**: 消費的な(consequential)遷移点にあらかじめ検証の関門を設計し、根拠・状態・動態の各アンカーを明示的に固定することで、事後の再構成可能性を担保する。
- **人間とAIの役割分業を事前に定義する**: エージェント型AIを既存の運用体系に導入する際は、証拠取得・分類・報告の自動化範囲と、人間が保持すべき判断・検証の境界を、AI実装に先立って明文化しておく。
- **インシデント対応プロトコルを事前設計の検証手段として運用する**: 六段階の対応プロセス自体を、事後の弁明手続きとしてではなく、決定時点での証拠拘束が機能しているかを継続的に検証する仕組みとして位置づける。

## 関連概念

[[human-oversight-mechanisms]], [[algorithmic-transparency]], [[ai-accountability-attribution]], [[ai-governance-and-risk-management]], [[ai-explainability-decision-making]]

## 参考ソース

* **タイトル**: Evidence-Grounded AI Operations Workflow: Extending a Human-Designed Quality Monitoring Framework with Agentic AI (2026)
  **ファイルパス**: `raw/papers/organization_science/evidence-grounded-ai-operations-workflow-extending-a-human-designed-quality-moni.md`

* **タイトル**: The AI Incident Response Protocol: Six Stages, and the Evidence a Reconstruction Requires (2026)
  **ファイルパス**: `raw/papers/organization_science/the-ai-incident-response-protocol-six-stages-and-the-evidence-a-reconstruction-r.md`

* **タイトル**: Human, AI, and Organizational Performance (HAOP): A Safety Framework for the AI Era (2026)
  **ファイルパス**: `raw/papers/organization_science/human-ai-and-organizational-performance-haop-a-safety-framework-for-the-ai-era.md`
