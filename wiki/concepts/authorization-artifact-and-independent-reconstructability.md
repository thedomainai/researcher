# 認可アーティファクトと独立的再構成可能性

## 概要

認可アーティファクトと独立的再構成可能性とは、自律的な主体が副作用を生む場面において、次の二つの認可を区別し、後者の根拠を事後に第三者が検証できる形で残すという原理である。

- **接続・アクセスの認可**:誰が、どの範囲に接続してよいか。
- **行為・出力の認可**:個々の出力が、その時点で適用される特定のポリシーに適合していたか。

AIエージェントがテキスト生成から、データベースへの書き込み、規制当局への提出、取引の実行といった副作用の生成へ移ると、ガバナンス上の問いが変わる。「エージェントは正しく接続したか」ではなく、「その出力は適用ポリシーの下で認可されており、その認可を独立に再構成できるか」が問われる。

AI Nativeな社会設計にとって、これは信頼の必要条件にあたる。自律的主体が増えるほど、人間が個々の行為を逐一承認することはできなくなる。そのため、信頼は「事後に、当事者ではない第三者が、改ざんされていない根拠に基づいて判断を再現できるか」という構造的な性質に依存することになる。

## メカニズム

この原理は、主体が人間、AI、組織、技術のいずれであっても成り立つ構造として、次の三要素に整理できる。

1. **アクセス認可と行為認可の分離**
   アクセス認可は、身元とスコープの検証である。行為認可は、特定の出力が、そのときに有効だった特定バージョンのポリシーに適合することの証拠である。前者が満たされても後者は自動的には満たされない。両者を機械的に分けて扱うことで、何が何によって認可されたのかが曖昧にならない。

2. **実行前に生成される認可アーティファクト**
   行為認可の証拠は、実行後に取り繕うのではなく、実行前の認可行為の産物として存在する必要がある。これは、特定の判断(verdict)を独立に再構成するのに足りる内容でなければならない。

3. **改ざん耐性と事後検証可能性**
   アーティファクトが当事者自身によって書き換え可能であれば、再構成は独立とは言えない。第三者が、運用主体の説明に頼らず、記録だけから「どのポリシー版の下で、なぜその出力が許されたか」を辿れることが要件となる。

人間の組織に置き換えても同じ構造が確認できる。入館証(アクセス認可)があることと、特定の支払い決裁(行為認可)が規程に沿っていたことは別の問題である。後者は決裁記録という証跡で初めて監査可能になる。

## 理論的背景

**認可境界の定義(ソース1・2)**
Meymanの論文は、規制環境で動作するエージェント型AIの認可境界を定義している。アクセス認可はOAuth 2.1やMCP認証が扱う領域とされる。行為認可は、特定の出力が、事象の時点で適用されるポリシーの特定バージョンに適合するという証拠として位置づけられる。同論文は、MCPゲートウェイのエコシステムが相互運用性、トラフィック管理、運用統制といった現実の課題を解決する一方で、特定の判断を独立に再構成するのに十分な実行前の認可アーティファクトを、必ずしも生成しないと論じる。本記事の中核である、接続認可と行動認可の機械的分離の要請はここに基づく。なお、抜粋は途中で切れており、論文の結論部分の詳細は本記事の根拠には含めていない。

**ガバナンスファーストな設計(ソース3)**
Saadhuらの論文は、規制産業で既存のERPを置き換えにくいという制約のもと、外部統合パターンやガバナンスされたデータプレーン、AIサービス構成要素を組み合わせる参照アーキテクチャを提案している。ここでは、監査可能性、追跡可能性、説明可能性、人間による監督が、後付けのコンプライアンス機能ではなく、横断的なアーキテクチャ特性として扱われる。

**監査可能性を設計目標とする(ソース4)**
GRACEは、規制が自然言語で表現される一方、コンプライアンス論理がスマートコントラクトやトークン標準に埋め込まれるという乖離を扱う。監査可能性を設計目標として運用化するため、知識・オーサリング・ガバナンスの各層と人間参加型のガバナンスを組み合わせた層状アーキテクチャを示している。評価は、構造化された専門家の介入が、ルールレベルでの執行可能性と検証可能性を高める方向を示す、という限定的なものである。

**責任帰属の課題(ソース5)**
インドの課税を扱う論文は、自律AIエージェントが交渉や取引を人間の同時的介入なしに完了させる状況で、課税の枠組みが識別可能な法人格の存在を前提とすることの困難を指摘している。行為の根拠と主体を辿れる記録がなければ、責任の帰属も課税も成立しにくいという点で、本原理の必要性を裏側から示す。

## AI Nativeな設計への示唆

- **二層の認可設計**:接続時の認証・スコープ検証と、出力ごとのポリシー適合の認可を、別々のコンポーネントとして設計する。ゲートウェイを通過したことを、行為が認可された証拠とみなさない。
- **実行前のアーティファクト生成**:副作用を伴う操作の前に、適用ポリシーのバージョン、判断内容、対象の出力を結びつけた記録を生成する。
- **ポリシーのバージョン管理**:事象時点で有効だったポリシー版を特定できるようにする。後から最新規則で解釈し直せる設計は避ける。
- **改ざん耐性と独立検証**:記録は運用主体から独立して検証できる形で保持する。検証に運用者の説明を必要としないことを基準にする。
- **監査可能性を横断特性として組み込む**:追跡可能性や人間による監督を後付けせず、アーキテクチャの初期から構成要素とする。既存システムを置き換えられない場合は、外部統合の形で実現する。
- **責任の錨としての記録**:法的主体や課税上の帰属が未整備な領域では、認可アーティファクトが行為と責任主体を結びつける実務上の手がかりになる。

## 関連コンセプト

- [[runtime-authorization-control-points]] — 実行時の認可と制御点の設計。行為認可を実行前にどこで生成するかに直結する。
- [[multi-layer-independent-control-and-institutional-durability]] — 複数の独立した制御層。アクセス認可と行為認可の分離を制度耐久性の観点から補強する。
- [[plural-independent-checks-against-singular-power]] — 独立した複数の判断者による牽制。第三者による再構成の考え方と通じる。
- [[discretion-relocation-to-design-parameters]] — 裁量が設計パラメータへ移ることで、説明責任が追跡しにくくなる問題。
- [[legal-wrapper-as-coordination-and-liability-anchor]] — 法的実体を責任の錨とする発想。認可記録が果たす役割と対比できる。
- [[sociotechnical-embeddedness-and-legitimacy-driven-adoption]] — 検証可能性が社会的な正当性と導入を支える側面。

## 参考ソース

1. What MCP and AI Gateways Do Not Establish for Regulated Agentic AI — Edward Meyman, 2026
   `raw/papers/law/what-mcp-and-ai-gateways-do-not-establish-for-regulated-agentic-ai.md`
2. The Authorization Boundary: What MCP and AI Gateways Do Not Establish for Regulated Agentic AI — Edward Meyman, 2026
   `raw/papers/law/the-authorization-boundary-what-mcp-and-ai-gateways-do-not-establish-for-regulat.md`
3. Modernizing Procurement and Financial Controls Without Replacing Legacy ERP: A Governance-First AI Architecture — Vijaya Bhaskar Reddy Saadhu, 2026
   `raw/papers/law/modernizing-procurement-and-financial-controls-without-replacing-legacy-erp-a-go.md`
4. GRACE: An AI-Augmented Compliance Information System for Real-World Asset Tokenization — Ming Hin Chung, Treza Bawm Win, Hao Zhong, 2026
   `raw/papers/law/grace-an-ai-augmented-compliance-information-system-for-real-world-asset-tokeniz.md`
5. The Taxation of AI Agents: Can India Tax Autonomous AI-Commerce Without Recognising the AI as a Taxable Person? — Aditya Mishra, Nikhil Kumar Jha, Akshat Mishra, 2026
   `raw/papers/law/the-taxation-of-ai-agents-can-india-tax-autonomous-ai-commerce-without-recognisi.md`
