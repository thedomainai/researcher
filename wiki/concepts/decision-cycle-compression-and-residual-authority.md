# 意思決定サイクルの圧縮と残余権限の設計

## 概要

意思決定サイクルの圧縮と残余権限の設計とは、自動化が判断に使える時間を縮めて誤認リスクを生む一方で、その誤りを「消えないもの」として前提に置き、権限の所在まで明示的に設計するという不変原理である。

自動化は感知力と処理速度を高める。しかし不確実性は消えるのではなく、別の場所へ移る。判断の猶予が短くなるほど、人間もシステムも出力を吟味せずに受け入れやすくなる。したがってAI Nativeな社会設計では、次の3点を最初から設計対象に含める必要がある。

- どの作業を計算に委ねてよいか
- どの判断を人間の規範的判断に残すか
- 残存する誤差を誰が、どんな根拠で、どんな異議申立ての余地を持って扱うか

## メカニズム

この原理は、判断主体が人間・AI・組織・技術のいずれであっても成立する構造として、次の4つに整理できる。

### 1. 時間圧縮による誤認
感知と処理が高速化すると、観測から行動までのサイクルが短くなる。センサー融合は状況認識を強化するが、同時に自動化バイアス、不透明性、操作可能性、サイクルの圧縮が重なり、誤認とエスカレーションのリスクが増す。不確実性は除去されず、再配分される。

### 2. 計算可能な作業と規範判断の境界
作業には、検索、算術、文書の要約、異常検知、限定的な分類のように、構造化されて計算に適するものがある。一方、実質の評価、目的、証拠、比例性、公正性、公的権限の理由づけられた行使は規範判断であり、形式的にもっともらしい出力があっても、それだけで正当な結論にはならない。

### 3. 残存誤差の明示的ガバナンス
近似には必ず誤差が残る。そこで、どの誤差が残り、どれを許容してよく、誰がそれに基づいて行動できるかを明示する。この記録は2種類ある。
- **残余台帳**: 物理、因果、人間状態、遅延、転移、エネルギーの各次元で、行動に関わる残りを記録する。
- **権限台帳**: 誰が残余の証拠を介入に変換するのか、その根拠、不確実性、異議申立ての機会を記録する。

### 4. 個人自律と集団利益のトレードオフ
継続的な計測や自動介入は、集団の利益(保護・即応性)と個人の自律性の間にあるジレンマを、技術を通じて自動的に実行してしまう。このトレードオフは技術が解消するものではなく、設計時に明示すべき対象である。

## 理論的背景

**租税分野の規範的・法理的整理**(Stefani, 2026)は、AIが有用な領域と、人間の規範判断が必要な領域の境界を論じる。法理論、比較の濫用防止法理、移転価格ガイダンス、大規模言語モデルの実証研究、AIガバナンス枠組みを踏まえ、構造化された検索や算術などにはAIの価値を認める。他方、経済的実質や比例性、公正性の評価を要する場面では、形式的にもっともらしい出力は法的に正当化された結論を保証しないと論じる。

**東地中海の地政学分析**(Poyiadjis, 2026)は、構造的現実主義、地域安全保障複合体理論、限定合理性を統合し、「アルゴリズム的地政学」を提示する。海洋監視、重要インフラ防護、サイバー帰属、危機管理を検討し、AIは不確実性を除去せず再配分すると結論づける。対策として、人間による監督、不確実性の報告、安全な監査証跡、強靭なインフラ、より強いインシデント管理を挙げる。

**残余ガバナンス**(Sun, 2026)は、介入するAI(臨床意思決定支援、人間と機械のチーミング、ロボティクス、自動引き継ぎプロトコルなど)が、不確実性下でタイミング・注意・権限を動かすことに着目する。責任ある身体化AIには、残る近似誤差と行動主体の明示が必要だと論じ、残余台帳と権限台帳を提案する。限定合理性、能動的推論、安全な強化学習の議論を、権限の扱いにまで拡張するものである。

**軍における個人健康モニタリングの倫理**(Bovens, 2026)は、オランダ軍を事例に、継続的に健康データを集めるシステムが、健康保護、負傷予防、負傷者検知、即応性を支える可能性を示す。同時に、個人・組織・社会への広い帰結に関する倫理的問いを提起する。倫理的認識と批判的省察を育てることで、道徳的な盲点を見つけ、責任ある判断を支えることを目指す。

**若者の慢性疼痛向けデジタルヘルス**(Bidargaddi ら, 2026)は、共同設計とシステム統合を、相互作用する単一の設計要件として扱うべきだとする。ここから、複数の要件が絡み合う条件下では、要件を切り離して個別最適化できないという示唆が得られる。

## AI Nativeな設計への示唆

1. **タスクを境界で分類する**: 検索、算術、要約、異常検知、限定分類は自動化の候補とする。実質、比例性、公正性の評価は人間に残す。
2. **残余を台帳化する**: 誤差の種類、許容範囲、行動可能な主体を、事後ではなく設計時に記録する。
3. **権限を明示する**: 出力を介入へ変換する権限者、根拠、不確実性の提示、異議申立ての機会を定める。
4. **時間を設計する**: 圧縮された判断サイクルでは、不確実性の報告と人間の監督点を組み込み、出力が自動的に受け入れられることを防ぐ。
5. **監査可能にする**: 安全な監査証跡を保持し、事後検証と異議申立てを可能にする。
6. **自律と集団利益の緊張を可視化する**: 継続モニタリングでは、倫理的省察の場を制度に組み込む。
7. **統合を前提に共同設計する**: 利害関係者の多様性と制度間の整合性を、単一の要件として扱う。

## 関連コンセプト

- [[ai-decision-authority-restructuring]] — 意思決定権限の再構成
- [[decision-node-decomposition-and-bounded-relocation]] — 意思決定ノードの分解と限定合理性の再配置
- [[execution-time-governance]] — 実行時ガバナンスと権限委譲設計
- [[evidence-bearing-decision-traceability]] — 証拠を伴う意思決定の追跡可能性
- [[reliance-calibration-between-aversion-and-overtrust]] — 依存度のキャリブレーション
- [[decision-event-governance]] — 意思決定イベントを単位とするガバナンス
- [[bounded-rationality-and-behavioral-economics]] — 限定合理性と意思決定モデル
- [[finite-cognitive-resources-and-load-thresholds]] — 有限資源と負荷閾値

## 参考ソース

- Edvin Stefani (2026) "Substance, Form, and Machines: AI Assistance and Human Normative Judgment in Taxation" — `raw/papers/behavioral_economics/substance-form-and-machines-ai-assistance-and-human-normative-judgment-in-taxati.md`
- Konstantinos Poyiadjis (2026) "Algorithmic Geopolitics in the Eastern Mediterranean" — `raw/papers/behavioral_economics/algorithmic-geopolitics-in-the-eastern-mediterranean.md`
- Davy Bovens (2026) "Fostering reflection on the ethical dimension of personal health monitoring in the armed forces" — `raw/papers/behavioral_economics/fostering-reflection-on-the-ethical-dimension-of-personal-health-monitoring-in-t.md`
- Chia-Wei Sun (2026) "Residual governance for responsible embodied AI: authority, contestability, and cognitive sovereignty" — `raw/papers/behavioral_economics/residual-governance-for-responsible-embodied-ai-authority-contestability-and-cog.md`
- Niranjan Bidargaddi, Tammie R. Foster, Andrew M Briggs, Samantha Rowbotham, Helen Slater (2026) "Codesign and system integration as interacting demands in digital health for youth experiencing chronic pain." — `raw/papers/behavioral_economics/codesign-and-system-integration-as-interacting-demands-in-digital-health-for-you.md`
