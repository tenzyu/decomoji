# デコ文字！

<p align="center"><i>ディスコードライフにイロドリを！</i></p>

**Decomoji** は SNS アプリ **Discord** で **簡単** に可愛い **デコ文字** を使えるようにする Discord bot です。

**[Tips]** うまく動かない場合は下のトラブルシューティングを参考にしてください！

> ## **[✉️ Click To Invite !](https://discord.com/api/oauth2/authorize?client_id=792956411248246796&permissions=537226240&scope=bot)**

## 使い方

### `!decomoji <Message>`

このコマンドは `!emoji <Message>` でも同様に動きます。

また、 **`!d` や `!e` に省略可能です。**

## こんな感じ

![demo](https://cdn.discordapp.com/attachments/752286472383758416/793070793893347328/demo.gif)

### Required Permissions (必要な権限リスト)

- View Channels
- Manage Webhooks (ウェブフックの管理)
- Send Messages (メッセージを送信)
- Embed Link (埋め込みリンク)
- Use External Emoji
- Manage Messages (メッセージの管理)
- Read Messages History (メッセージ履歴を読む)

#### その他

使用フォントは **ましゅまろポップ** です。

開始日は **2020 年 12 月 28 日** です。

**GCE** で動かしています。 **(Python3.7.0)**

> ## **[✉️ Click To Invite!](https://discord.com/api/oauth2/authorize?client_id=792956411248246796&permissions=537226240&scope=bot)**

# トラブルシューティング

## 問題 1：変なのが返ってくる。

`!e てすと` と送信して、デコ文字ではなく `:81_te::87_su::80_to:` のような絵文字のエイリアスが返ってきた場合は、

_**サーバーの設定から、@everyone に対して Use External Emoji の権限を与えてください。**_

Decomoji は **Webhook** という仕組みを利用して、デコ文字に置き換えたメッセージを送信しています。このときに参照される権限先が @Decomoji **ではなく** @everyone であるため、このように解決する必要があります。

<hr />

**解決しない or 新しい問題** があれば **Issue** を立てるか、**[Twitter](https://twitter.com/tenzyumasuda)** にダイレクトメッセージを送ってください。気軽にどうぞ！

<br />

<br />

<p align="center">©️ 2020 - 2021 Tenzyu Masuda</p>

<br />

<br />
