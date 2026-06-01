# 計算による把握とハプティクス

## 概要

計算による把握とハプティクスは、ロボット工学、人間とコンピューターの相互作用（HCI）、神経科学などの分野が交差する学際的な研究領域です。この分野は、物体を効率的かつ適応的に把握する方法や、触覚（ハプティクス）および内臓感覚を介して人間がどのように環境と相互作用するかを理解し、再現することに焦点を当てています。具体的には、最小限の物体情報からロバストな把握を生成するメカニズムの探求や、生理学的フィードバックが人間の感覚や行動に与える影響の調査など、幅広いトピックを扱います。

## 詳細

計算による把握に関する研究は、精密な物体モデルや大規模なデータ駆動型トレーニングに頼ることなく、ロバストで適応的な器用な把握が最小限の物体情報からどのように生まれるかを調査しています。このアプローチでは、把握をロボットと簡略化された物体表現との間の動的な相互接続としてモデル化します。例えば、物体を粗い幾何学的プリミティブ（球、円筒、箱）で近似し、それぞれを人間の把握分類における規範的な把握タイプと関連付けます。把握の実行は、仮想のバネとダンパーが仮想の手を仮想の物体に機械的に結合する「仮想モデル制御（VMC）」フレームワーク内で定式化されます。これにより、定義済みの軌道ではなく、結合されたダイナミクスから把握動作が自然に発生します。構造化された剛性分布と適応的な減衰プロファイルは、協調的で人間のような指の閉鎖を促進します。また、手の動きから物体の姿勢の変化を推測する可能性についても研究されています。

ハプティクス（触覚）と内臓感覚に関する研究は、触覚フィードバックが人間の生理学的感覚や行動に与える影響に焦点を当てています。特に「内臓ハプティクス（VisceroHaptics）」は、胃に基づくオーディオハプティックフィードバックが胃の感覚と胃の内臓感覚行動に与える影響を調査します。胃の内臓感覚は摂食行動や感情に影響を与えるため、その調節はヘルスケアや人間とコンピューターの相互作用のアプリケーションにおいて価値があります。腹部音駆動型ハプティックフィードバックが腸の感覚に似ているという先行研究がある一方で、それが感情や胃の内臓感覚行動に与える影響は不明でした。研究では、胃に適用される腸音駆動型オーディオハプティックフィードバックが、ユーザーの感情にどのように影響するか、空腹感と満腹感の認識にどのように影響するか、そして水負荷試験-IIによって定量化される胃の内臓感覚行動にどのように影響するかを調査しました。

## 関連概念

*   [[ロボット工学]]
*   [[ヒューマン・コンピューター・インタラクション]]
*   [[神経科学]]
*   [[ハプティクス]]
*   [[内臓感覚]]

## 参考ソース

*   "Can We Infer Object Pose Changes from Hand Movements?" (raw/Can We Infer Object Pose Changes from Hand Movements?.md)
*   "VisceroHaptics: Investigating the Effects of Gut-based Audio-Haptic Feedback on Gastric Feelings and Gastric Interoceptive Behavior" (raw/VisceroHaptics: Investigating the Effects of Gut-based Audio-Haptic Feedback on Gastric Feelings and Gastric Interoceptive Behavior.md)
*   "Grasping by interconnection : can robust and adaptive grasping emerge from minimal object information?" (raw/Grasping by interconnection _ can robust and adaptive grasping emerge from minimal object information_.md)