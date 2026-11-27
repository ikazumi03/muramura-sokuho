# むらむら速報｜広告枠一覧（準備版）

作成日：2026年11月20日
状態：DMMアフィリエイト審査中。すべての枠は「準備中」表示で、広告リンク・公式コードは未設置。
設置ルール：承認後、公式コードをそのまま貼る（改変しない）。枠ごとに data-ad-slot で識別する。隠し広告・小さく隠しての大量表示はしない。

## 枠の構成（全37枠）

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
| campaign-top / -sidebar / -bottom | campaign.html | 冒頭／目次下／記事末 | FANZA総合 | 300x250 | 2026-11-20追加 |
| payment-top / -sidebar / -bottom | payment.html | 冒頭／目次下／記事末 | FANZA総合 | 300x250 | 2026-11-20追加 |
| faq-top / -sidebar / -bottom | faq.html | 冒頭／目次下／記事末 | FANZA総合 | 300x250 | 2026-11-20追加 |
| dlsite-top / -sidebar / -bottom | dlsite.html | 冒頭／目次下／記事末 | DLsite | 300x250 | DLsite専用枠。FANZA枠とは混在させない。2026-11-20追加 |

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

## 2026-11-27 増枠（広告密度アップ：38枠 → 66枠）

オーナー指示「サイトが寂しい。もっと広告多く、動くやつもたくさん」を受けて28枠を追加。全枠に「広告」ラベル（.ad-slot／.ad-label構造、スティッキーバーは同等構造）を付け、既存枠のコードは一切変更していない。アニメーションGIF素材を優先採用。

| 枠ID | ページ | 位置 | banner_id | 備考 |
|---|---|---|---|---|
| index-anim-top | index.html | ヒーロー直後 | 1150_300_250 | 実写GIF動画・アニメーション |
| index-anim-game | index.html | 中段（新着ガイド後） | 2198_300_250 | FANZA GAMES GIF・アニメーション |
| index-large | index.html | 下段 | 2198_600_500 | FANZA GAMES GIF・アニメーション |
| index-wide-doujin | index.html | 最下段 | 2210_640_200 | FANZA冬の同人祭（〜2027-02-01） |
| guide-video-mid1 | guide-video.html | 記事中段 | 1150_300_250 | 実写GIF動画・アニメーション |
| guide-video-mid2 | guide-video.html | 記事中段 | 1148_300_250 | 実写GIF動画・アニメーション |
| guide-video-mid3 | guide-video.html | 記事中段 | 123_300_250 | 月額動画 |
| guide-game-mid1 | guide-game.html | 記事中段 | 2198_300_250 | FANZA GAMES GIF・アニメーション |
| guide-game-mid2 | guide-game.html | 記事中段 | 2201_336_280 | FANZA GAMES GIF・アニメーション |
| guide-game-mid3 | guide-game.html | 記事中段 | 2187_300_250 | ウィンターセール（〜2027-01-13） |
| guide-doujin-mid1 | guide-doujin.html | 記事中段 | 2210_300_250 | FANZA冬の同人祭（〜2027-02-01） |
| guide-doujin-wide | guide-doujin.html | 記事末 | 2210_640_200 | FANZA冬の同人祭（〜2027-02-01） |
| guide-ebook-mid1 | guide-ebook.html | 記事中段 | 738_640_200 | ERO TOON |
| guide-ebook-large | guide-ebook.html | 記事中段 | 738_600_500 | ERO TOON |
| beginner-mid | beginner.html | 記事中段 | 83_300_250 | ライブチャット |
| price-mid | price.html | 記事中段 | 1277_300_250 | FANZA TV |
| campaign-mid | campaign.html | 記事中段 | 1506_300_250 | 通販・大人のおもちゃ |
| payment-mid | payment.html | 記事中段 | 2134_300_250 | キャラチャット |
| faq-mid | faq.html | 記事中段 | 860_300_250 | オンラインくじ |
| safety-mid | safety.html | 記事下段 | 1169_640_100 | FANZAキャッチ |
| about-mid | about.html | 記事下段 | 83_300_250 | ライブチャット |
| policy-mid | policy.html | 記事下段 | 1277_300_250 | FANZA TV |
| contact-mid | contact.html | 記事中段 | 1506_300_250 | 通販・大人のおもちゃ |
| index-sticky / guide-video-sticky / guide-game-sticky / guide-doujin-sticky / guide-ebook-sticky | index＋ガイド4ページ | 画面下部固定（モバイル≤768pxのみ） | 1150_320_50 | 実写GIF動画・アニメーション。×ボタンで閉じるとセッション中は再表示しない（sessionStorage）。本文が隠れないようモバイル時は body に padding-bottom を追加 |

未使用のまま残したコード：1150_320_100、1148_320_50、164_300_250、67_468_60、1326_300_250、258_336_280（枠数目標に合わせて見送り。今後の差し替え・増枠候補）
