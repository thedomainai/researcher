# 規範的枠組み操作による制度捕獲

規範的枠組み操作による制度捕獲とは、権力的アクターが制度の規範的・手続的ルールそのものを書き換えることで、本来は公正な裁定機構であるはずの仕組みを、特定の集団を選別的に保護・免責する手段へ転換するメカニズムである。これは法律の違反ではなく、法律の「ルール自体」を操作する点で従来の腐敗分析と区別される。AI Native な制度設計においては、規範やガバナンス枠組みを事後的に調整できる権限がどこに存在するかを特定しなければ、同様の捕獲が自動化された意思決定システムの中で再演されうるため、この概念は重要である。

## 概要

このメカニズムの核心は、制度的な「ルールの修正権限」そのものを、権力的アクターが自らの利益のために行使することにある。ソースで紹介されているルーマニアの事例では、チェスの「タッチド・ピース(pièce touchée)」規則——駒に触れたら動かさなければならない——が、現実には「J'adoube(調整します)」という宣言によって無効化される様子が比喩として用いられている。つまり、本来は確定的・不可逆的であるはずの手続き上のコミットメントが、権力を持つ者だけに許された「調整」宣言によって事後的に書き換え可能になる。これにより、司法という本来は中立的な裁定機構が、特定のエリート層やトランスセクター的ネットワークのための選別的保護装置へと変質する。

## 理論的背景と知見

ソース論文は、心理社会学・人類学の観点からルーマニアの司法制度における「国家捕獲」と「システム的免責」を分析している。分析の因果連鎖は、社会アノミー(社会的規範の弛緩)→逸脱→社会病理→組織犯罪という、心理人類学および逸脱の社会学の枠組みから導かれている。

具体的な実証事例として、ルーマニア憲法裁判所(CCR)の判決(2018年no.297、2022年no.358)と高等裁判所・司法裁判所(ÎCCJ)の判決(2022年no.67)が検討されている。これらの判決の連鎖が2018年から2022年にかけて「立法的空白」を生み出し、その結果、超時効(ultra-prescription)の遡及適用が可能となり、9,635件を超える高位の腐敗事件で刑事訴追が消滅した。

この論文は「制度的J'adoube」という概念を提起している。これは、政治的エリートとトランスセクター的ネットワークが、憲法裁判所や最高裁判所という最も権威的な規範解釈機関を利用して、規範的枠組みを事後的に「調整」し、自分たちに有利な方向へ再構成するタクティクスを指す。重要なのは、この操作が違法な介入としてではなく、合憲性審査や法解釈統一という正当な司法手続きの体裁をとって実行される点である。これにより、制度捕獲は表面上は手続き的正当性を保ちながら、実質的には選別的免責を固定化する。

## AI Native な設計への示唆

- **規範修正権限の所在を明示し分離する**: ガバナンスルールや評価基準そのものを変更できる権限を、ルールの運用・執行権限から分離し、誰が「J'adoube」に相当する調整宣言を発行できるかを可視化・制限する必要がある。これは [[architectural-locus-of-accountability]] や [[authority-bounding-by-parallel-independent-layers]] の設計原理と接続する。

- **法的・規範的空白の戦略的創出を監視する**: 複数の決定機構(司法・立法に相当する複数のガバナンス層)が時間差を伴って連鎖的に判断を下す場合、その間隙に意図的な空白が生じうる。AI システムのガバナンスでも、複数の監督機関・認証機関の判断タイミングのずれが同様の空白を生む危険があり、[[regulatory-fragmentation-and-institutional-incentive-drift]] や [[temporal-erosion-of-procedural-legitimacy-under-opacity]] の観点から事前に検知する仕組みが要る。

- **遡及適用可能性を制限する**: ルールの事後的な再解釈が過去の行為の免責に使われないよう、規範の遡及効力そのものに構造的な制約を課す設計が望まれる。これは [[pre-irreversibility-authority-and-constraint-embedding]] の考え方と整合する。

- **選別的執行の非対称性を検出する指標を持つ**: 同一ルールが対象の属性(権力の大小)によって異なる強度で執行される場合、免責の固定化が進行している可能性がある。執行ログの属性別分布を継続的に監査する仕組みが、[[structural-reproduction-of-bias-and-power-asymmetry-in-technology]] と同様の論理で必要となる。

- **裁定機構の独立性を手続き的に保証する**: 規範解釈を行う審査体(憲法裁判所相当の機能)が、規範を利用する当事者(政治・行政エリート相当のアクター)から構造的に独立していることを、[[structural-separation-of-verification-from-governed-system]] の原理に基づいて確保する。

## 関連概念

[[architectural-locus-of-accountability]], [[authority-bounding-by-parallel-independent-layers]], [[regulatory-fragmentation-and-institutional-incentive-drift]], [[temporal-erosion-of-procedural-legitimacy-under-opacity]], [[pre-irreversibility-authority-and-constraint-embedding]], [[structural-reproduction-of-bias-and-power-asymmetry-in-technology]], [[structural-separation-of-verification-from-governed-system]]

## 参考ソース

* **タイトル**: The Mechanics of the "Touched Piece" in State Capture: A Psychosociological and Anthropological Analysis of Impunity in White-Collar Crime in Romania (2026)
  **ファイルパス**: `raw/papers/anthropology/the-mechanics-of-the-touched-piece-in-state-capture-a-psychosociological-and-ant.md`

## 追加ソース（2026-11-27）

* **タイトル**: Purpose Capture: How Corporate Purpose Is Controlled by the Very Actors It Was Intended to Constrain (2026)
  **ファイルパス**: `raw/papers/corporate_governance/purpose-capture-how-corporate-purpose-is-controlled-by-the-very-actors-it-was-in.md`
