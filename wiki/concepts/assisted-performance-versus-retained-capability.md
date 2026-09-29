# 支援下の遂行と保持される能力の乖離

## 概要

**支援下の遂行と保持される能力の乖離**(Assisted Performance versus Retained Capability)とは、AIなどの支援を受けているときの成果(assisted performance)と、支援を外した後にその人に残る能力(retained capability)が、別の量であるという原理である。ソースの表現を借りれば「影響は根拠ではなく(Influence is not warrant)、支援下の遂行は保持される能力ではない(assisted performance is not retained capability)」。

ソースによれば、AIの出力は、人が何を「アクセス可能」で「検討に値する」と感じるかを変えられる。しかしそれは、その人に「検証された信じる理由(warrant)」を与えることを意味しない。また、AI支援下で成果が上がっても、支援を撤去した後に残るものはむしろ少なくなりうる。

AI Nativeな設計にとって重要なのは、次の点である。

- 支援下の出力品質や利用可能性だけを指標にすると、能力が育っているのか、代行されているだけなのかを区別できない。
- 意味化(人が差異を読み取り、意味づけ、経験として保持する過程)を経ない情報は、能力に転化しない。
- したがって、社会や組織の設計では「支援下の遂行」と「支援を外した後の能力」を別々に測り、設計する必要がある。

## メカニズム

この原理は、対象を人間・AI・組織・技術に入れ替えても成立する構造として整理できる。

1. **影響と正当化の分離**
   受け手(主体)の状態を変える作用(影響、利用可能性の変化)と、その変化を支える検証済みの根拠(正当化)は別の量である。前者が大きくても後者は増えない。
2. **意味化を介した転化**
   外部から与えられた情報や支援は、受け手が自らの側で意味づけ・保持するプロセスを経て初めて、受け手に帰属する能力になる。このプロセスを経ない支援は、支援がある間だけ機能する。
3. **支援依存による保持の低下**
   支援が遂行を肩代わりすると、遂行は向上して見えても、受け手内部に残る能力(支援撤去後の能力)は低下しうる。
4. **構造的一般化**
   「主体」を組織に、「支援」を技術基盤に置き換えても同じ構図になる。技術が成果を出していても、組織内に理解や運用能力が蓄積されているとは限らない。観測される成果と、主体に帰属する能力は独立に扱う必要がある。

## 理論的背景

ソースは、Yaoharee Lahtee による2026年の概念論文である。論文は **Human Semantic-Cognitive Intelligence (HSCI)** というアーキテクチャを提示する。

- HSCIは新しい方程式ではなく「経路(route)」である。オープンな方程式ライブラリ(Toledo)に登録された対象を順序づける。
- 順序は、人が出会った差異を読み取るところから始まり、意味、経験、保持、問題形成、アクセス可能性、発見、識別的行為を経て、人間とAIの対話に入る。その先に、生きた可能性(live possibility)、選択、行為主体性(agency)、Human Return(支援なしで保持される能力)、Human Conversion(人の能力の変化)が続く。
- このアーキテクチャの目的は、影響、正当化、支援下の遂行、保持される能力といった量を混同せず、別々に保つことにある。

ソースの核心的知見は、表層的な影響(accessibility)と根本的な理解(warrant)の区別が、人間の意味化プロセスを経ない情報では retained capability に転化しない、という点である。なお、提示された抜粋は要旨の途中までであり、実証データや具体的な数値は確認できないため、本記事では概念的主張の範囲にとどめる。

## AI Nativeな設計への示唆

以下は上記原理から導かれる設計指針である(ソース自体が具体的手順を述べているわけではない)。

- **二種類の指標を分ける**:支援下の成果と、支援撤去後の保持能力(Human Return に相当する視点)を別々に評価する。
- **出力の説得力を根拠と混同しない**:AI出力が受け入れやすいことを、その正当性の証拠として扱わない。利用者が自ら検証できる根拠を提示する設計にする。
- **意味化を促す介入を組み込む**:答えをそのまま渡すだけでなく、利用者が差異を読み取り、意味づけ、保持する過程を残す。
- **支援撤去テストを設ける**:定期的に支援なしの状況で能力を確認する。
- **組織にも適用する**:AI導入の成果を、組織に蓄積された能力とは別に扱う。

## 関連コンセプト

- [[assistance-availability-versus-skill-formation]] — 支援の可用性と能力形成の逆相関
- [[assistance-mediated-capability-erosion-and-homogenization]] — 支援による能力侵食と多様性の画一化
- [[delegation-induced-ownership-and-capability-erosion]] — 委譲による所有感・責任・能力の侵食と回復的足場設計
- [[capability-externalization-dual-effects]] — 能力外部化の二面性と非定常環境での再適応
- [[complementary-performance]] — 相補的パフォーマンス
- [[capability-transparency-gap-and-trust-loss]] — 能力と透明性の乖離による信頼の喪失と証拠境界の喪失
- [[capability-as-system-boundary-property-and-composed-intelligence]] — システム境界に帰属する能力と合成知能

## 参考ソース

- Influence Is Not Warrant: An Architecture-First Account of Human Semantic-Cognitive Intelligence in Human–AI Interaction(Yaoharee Lahtee、2026)
  File: raw/papers/systems_engineering/influence-is-not-warrant-an-architecture-first-account-of-human-semantic-cogniti.md
