# むらむら速報｜広告枠一覧（準備版）

作成日：2026年11月20日
状態：DMMアフィリエイト審査中。すべての枠は「準備中」表示で、広告リンク・公式コードは未設置。
設置ルール：承認後、公式コードをそのまま貼る（改変しない）。枠ごとに data-ad-slot で識別する。隠し広告・小さく隠しての大量表示はしない。

## 枠の構成（全25枠）

| 枠ID | ページ | 位置 | 想定案件 | 推奨サイズ | 備考 |
|---|---|---|---|---|---|
| index-middle | index.html | ジャンル紹介直後 | FANZAブックス | 728x90（スマホ300x250） | トップの中段 |
| index-bottom | index.html | フッター直前 | FANZA総合 | 300x250 | トップ下部 |
| guide-video-top / -sidebar / -bottom | guide-video.html | 冒頭／目次下／記事末 | FANZA動画 | 300x250 | 見放題・単品の記事内容に合わせる |
| guide-ebook-top / -sidebar / -bottom | guide-ebook.html | 冒頭／目次下／記事末 | FANZAブックス | 300x250 | 本命枠。漫画キャンペーン素材の候補 |
| guide-game-top / -sidebar / -bottom | guide-game.html | 冒頭／目次下／記事末 | FANZAゲーム | 300x250 | |
| guide-doujin-top / -sidebar / -bottom | guide-doujin.html | 冒頭／目次下／記事末 | FANZA同人 | 300x250 | |
| beginner-top / -sidebar / -bottom | beginner.html | 冒頭／目次下／記事末 | FANZA総合 | 300x250 | 初めての読者向けの入口案件 |
| price-top / -sidebar / -bottom | price.html | 冒頭／目次下／記事末 | FANZA総合 | 300x250 | 料金確認の文脈と矛盾しない案件のみ |
| safety-sidebar / -bottom | safety.html | 目次下／記事末 | FANZA総合 | 300x250 | 安心面の記事のため冒頭枠は置かない |
| about-bottom | about.html | 記事末 | FANZA総合 | 300x250 | 運営情報ページは末尾のみ |
| policy-bottom | policy.html | 記事末 | FANZA総合 | 300x250 | ポリシーページは末尾のみ |
| contact-bottom | contact.html | 記事末 | FANZA総合 | 300x250 | 問い合わせページは末尾のみ |

## 承認後にやること（ステップ5）
1. 中村：DMMアフィリエイトの口座登録（本人作業。もちは口座・本人情報に触れない）
2. もち：各枠へ公式バナーコードを設置し、PR・広告表記を確認
3. もち：ops/site_audit.py で監査（要修正0を確認）してから GitHub へ push、公開サイトで表示確認
4. 配信ネットワーク（ExoClick／JuicyAds／TrafficJunky／TrafficStars）と DLsite は、この枠とは分けて台帳管理する

## 優先順位（承認直後）
1. guide-ebook の3枠（FANZAブックス＝本命）
2. index の2枠
3. guide-video の3枠
4. 残りのガイド・beginner・price
5. safety・about・policy・contact は最後（信頼系ページは控えめに）
