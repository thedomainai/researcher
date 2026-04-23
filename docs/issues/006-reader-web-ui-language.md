# Reader Web UI Language

## 問い

Article Reader を「きれいなスライド」ではなく、「毎日使う web UI」の文法に寄せるには、どの演出を削り、どの操作文脈を前に出すべきか。

## 症状

- hero が大見出し中心で、発表用の導入スライドに見える
- metric が showcase のように並び、操作より presentation を感じる
- stage に装飾グラデーションや疑似 window chrome があり、読書面より演出面に見える

## 結論

1. hero は compact header にする
2. metrics は dashboard strip に寄せ、説明文を削る
3. stage は plain surface にし、演出より readable workspace を優先する
4. 装飾的な window metaphor は減らし、state / selection / scope の UI に置き換える

## ネクストアクション

1. hero typography と metric presentation を縮小する
2. stage background と chrome の装飾を弱める
3. reader を再生成して layout test を通す
