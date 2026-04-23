# Reader Surface Hierarchy

## 問い

Article Reader の queue / stage / companion を、枠線で説明しすぎず、それでも迷わない reading workspace として成立させるにはどういう surface 階層にするべきか。

## 論点

1. queue controls は 1 カラムで読むべきか、2 カラムで圧縮すべきか
2. どの境界は明示的な panel として残し、どの境界は暗黙化するべきか
3. 本文を主役にしながら queue と companion の役割を弱めすぎないにはどうするか

## 論点分解

### Layout

- queue controls は検索 -> tier -> sort -> queue scope の順に縦に流したほうが scan cost が低い
- queue card だけは click target なので surface を持ってよい
- companion は 3 枚カードではなく 3 つの section として読ませたほうが本文補助面として自然

### Graphics

- main shell には surface を残す
- shell の中の subsection は border box より divider / tonal background / spacing で分節する
- nested card の数を減らす

### Typography

- 見出しが役割を宣言し、枠が役割を肩代わりしない状態にする
- label / section head / small summary の hierarchy で読む順番を作る

## 結論

1. queue controls は 1 カラムに戻す
2. queue panel / reading stage / companion panel の 3 surface は残す
3. その内部は card-in-card を避け、以下で分節する
   - section heading
   - 余白
   - 薄い horizontal divider
   - 弱い tonal fill
4. queue card と article metric strip のような interaction / metric 要素だけは clickability と機能境界のために surface を維持する

## ネクストアクション

1. queue controls を 1 カラム stack に変更する
2. queue-control-card / stage-meta-card / stage-brief-card / companion-card の border box 感を弱める
3. reader.html を再生成し、reader layout test を通す
