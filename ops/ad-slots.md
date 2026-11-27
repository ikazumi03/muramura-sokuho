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

## 2026-11-27 ランキングポータル化（リデザイン）

ガイド型トップを廃し、FANZAランキングポータルへ作り替え（参考：サキュ姉妹／FANZA Guide／順位変動つきランキングブログ）。
- index.html を全面再生成：今日のおすすめ（日替わり8作品）／カテゴリ別TOP10（AV・同人・コミックス・ゲーム）／セール中のおすすめ（40%OFF以上・横断10作品）／新作（発売日順10作品）。既存の index 枠8枠（index-anim-top / index-middle / index-anim-game / index-large / index-bottom / index-dlsite / index-wide-doujin / index-sticky）は全て同一コード・同一ラベルで同等位置に保持。
- カテゴリページを新設：av.html / doujin.html / books.html / game.html（各TOP30・結論ボックス・順位変動マーク▲▼/NEWつき）。データは DMM WebサービスAPI（ItemList, affiliate_id murasoku-990）で生成し、生成スクリプトは ~/workspace/muramura-tools/build_rankings.py（APIキーはリポジトリ外の .env で管理）。
- 新設ページの広告枠（各ページ2枠＋モバイル固定バー）:

| 枠ID | ページ | 位置 | banner_id | 案件 |
|---|---|---|---|---|
| av-mid1 / doujin-mid1 / game-mid1 | av.html / doujin.html / game.html | ランキング10位と11位の間 | 2124_300_250 | FANZAブックス90%OFFクーポン |
| books-mid1 | books.html | ランキング10位と11位の間 | 738_300_250 | ERO TOON |
| av-mid2 / doujin-mid2 / books-mid2 / game-mid2 | カテゴリ4ページ | ランキング20位と21位の間 | 1150_300_250 | 実写GIF動画・アニメーション |
| av-sticky / doujin-sticky / books-sticky / game-sticky | カテゴリ4ページ | 画面下部固定（モバイル≤768pxのみ） | 1150_320_50 | 実写GIF動画・アニメーション。index-sticky と同一パターン |

- 旧ガイドページ（guide-*.html、dlsite.html、FANZA総合ページ）はこのフェーズでは無変更。メインnavからは外し、ランキングページへ差し替え。

## 2026-11-27 Phase 2: 画像の高解像度化＋ジャンル別ページ新設

- 全作品カードの画像を imageURL.list（小）から imageURL.large（大）に切替（APIが large を返さない作品のみ list にフォールバック）。
- ジャンル別ランキングページを新設（各カテゴリ最大12ジャンル × TOP30）。AVはキュレーション優先リスト、同人・コミックス・ゲームは各フロアTOP30のジャンル出現頻度で自動選出（キャンペーン・形式タグは除外）。選出は生成スクリプト（build_rankings.py）が毎日自動で行うため、顔ぶれは日次で変わりうる。下表は 2026-11-27 時点の設置分。
- 各ジャンルページの広告枠は3枠: ランキング10位の後ろに mid1（books のみ 738_300_250、他は 2124_300_250）、20位の後ろに mid2（1150_300_250・アニメーションGIF）、モバイル固定バー sticky（1150_320_50）。
- カテゴリ4ページの sticky 枠（av/doujin/books/game-sticky）が広告台帳.csv 未登録だったため、今回あわせて登録した。

| ページ | ジャンル | 枠ID（接頭辞） | mid1 banner_id |
|---|---|---|---|
| av-genre-1014.html | AV × 熟女 | av-genre-1014-mid1 / av-genre-1014-mid2 / av-genre-1014-sticky | 2124_300_250 |
| av-genre-1018.html | AV × 女子校生 | av-genre-1018-mid1 / av-genre-1018-mid2 / av-genre-1018-sticky | 2124_300_250 |
| av-genre-1027.html | AV × 美少女 | av-genre-1027-mid1 / av-genre-1027-mid2 / av-genre-1027-sticky | 2124_300_250 |
| av-genre-1031.html | AV × 痴女 | av-genre-1031-mid1 / av-genre-1031-mid2 / av-genre-1031-sticky | 2124_300_250 |
| av-genre-1039.html | AV × 人妻・主婦 | av-genre-1039-mid1 / av-genre-1039-mid2 / av-genre-1039-sticky | 2124_300_250 |
| av-genre-2001.html | AV × 巨乳 | av-genre-2001-mid1 / av-genre-2001-mid2 / av-genre-2001-sticky | 2124_300_250 |
| av-genre-4006.html | AV × ナンパ | av-genre-4006-mid1 / av-genre-4006-mid2 / av-genre-4006-sticky | 2124_300_250 |
| av-genre-4024.html | AV × 素人 | av-genre-4024-mid1 / av-genre-4024-mid2 / av-genre-4024-sticky | 2124_300_250 |
| av-genre-4031.html | AV × コスプレ | av-genre-4031-mid1 / av-genre-4031-mid2 / av-genre-4031-sticky | 2124_300_250 |
| av-genre-5001.html | AV × 中出し | av-genre-5001-mid1 / av-genre-5001-mid2 / av-genre-5001-sticky | 2124_300_250 |
| av-genre-5002.html | AV × フェラ | av-genre-5002-mid1 / av-genre-5002-mid2 / av-genre-5002-sticky | 2124_300_250 |
| av-genre-5019.html | AV × パイズリ | av-genre-5019-mid1 / av-genre-5019-mid2 / av-genre-5019-sticky | 2124_300_250 |
| books-genre-1018.html | コミックス × 女子校生 | books-genre-1018-mid1 / books-genre-1018-mid2 / books-genre-1018-sticky | 738_300_250 |
| books-genre-102.html | コミックス × 美乳 | books-genre-102-mid1 / books-genre-102-mid2 / books-genre-102-sticky | 738_300_250 |
| books-genre-1027.html | コミックス × 美少女 | books-genre-1027-mid1 / books-genre-1027-mid2 / books-genre-1027-sticky | 738_300_250 |
| books-genre-2001.html | コミックス × 巨乳 | books-genre-2001-mid1 / books-genre-2001-mid2 / books-genre-2001-sticky | 738_300_250 |
| books-genre-4106.html | コミックス × 騎乗位 | books-genre-4106-mid1 / books-genre-4106-mid2 / books-genre-4106-sticky | 738_300_250 |
| books-genre-48.html | コミックス × 制服 | books-genre-48-mid1 / books-genre-48-mid2 / books-genre-48-sticky | 738_300_250 |
| books-genre-5001.html | コミックス × 中出し | books-genre-5001-mid1 / books-genre-5001-mid2 / books-genre-5001-sticky | 738_300_250 |
| books-genre-5002.html | コミックス × フェラ | books-genre-5002-mid1 / books-genre-5002-mid2 / books-genre-5002-sticky | 738_300_250 |
| books-genre-5003.html | コミックス × ぶっかけ | books-genre-5003-mid1 / books-genre-5003-mid2 / books-genre-5003-sticky | 738_300_250 |
| books-genre-5019.html | コミックス × パイズリ | books-genre-5019-mid1 / books-genre-5019-mid2 / books-genre-5019-sticky | 738_300_250 |
| books-genre-55.html | コミックス × 処女 | books-genre-55-mid1 / books-genre-55-mid2 / books-genre-55-sticky | 738_300_250 |
| books-genre-583.html | コミックス × ラブ＆H | books-genre-583-mid1 / books-genre-583-mid2 / books-genre-583-sticky | 738_300_250 |
| doujin-genre-1039.html | 同人 × 人妻・主婦 | doujin-genre-1039-mid1 / doujin-genre-1039-mid2 / doujin-genre-1039-sticky | 2124_300_250 |
| doujin-genre-152004.html | 同人 × ラブラブ・あまあま | doujin-genre-152004-mid1 / doujin-genre-152004-mid2 / doujin-genre-152004-sticky | 2124_300_250 |
| doujin-genre-153003.html | 同人 × おっぱい | doujin-genre-153003-mid1 / doujin-genre-153003-mid2 / doujin-genre-153003-sticky | 2124_300_250 |
| doujin-genre-2001.html | 同人 × 巨乳 | doujin-genre-2001-mid1 / doujin-genre-2001-mid2 / doujin-genre-2001-sticky | 2124_300_250 |
| doujin-genre-4111.html | 同人 × 寝取り・寝取られ・NTR | doujin-genre-4111-mid1 / doujin-genre-4111-mid2 / doujin-genre-4111-sticky | 2124_300_250 |
| doujin-genre-48.html | 同人 × 制服 | doujin-genre-48-mid1 / doujin-genre-48-mid2 / doujin-genre-48-sticky | 2124_300_250 |
| doujin-genre-5001.html | 同人 × 中出し | doujin-genre-5001-mid1 / doujin-genre-5001-mid2 / doujin-genre-5001-sticky | 2124_300_250 |
| doujin-genre-5002.html | 同人 × フェラ | doujin-genre-5002-mid1 / doujin-genre-5002-mid2 / doujin-genre-5002-sticky | 2124_300_250 |
| doujin-genre-5003.html | 同人 × ぶっかけ | doujin-genre-5003-mid1 / doujin-genre-5003-mid2 / doujin-genre-5003-sticky | 2124_300_250 |
| doujin-genre-5005.html | 同人 × アナル | doujin-genre-5005-mid1 / doujin-genre-5005-mid2 / doujin-genre-5005-sticky | 2124_300_250 |
| doujin-genre-5019.html | 同人 × パイズリ | doujin-genre-5019-mid1 / doujin-genre-5019-mid2 / doujin-genre-5019-sticky | 2124_300_250 |
| doujin-genre-7110.html | 同人 × シミュレーション | doujin-genre-7110-mid1 / doujin-genre-7110-mid2 / doujin-genre-7110-sticky | 2124_300_250 |
| game-genre-301085.html | ゲーム × CGがいい | game-genre-301085-mid1 / game-genre-301085-mid2 / game-genre-301085-sticky | 2124_300_250 |
| game-genre-301088.html | ゲーム × キャラクターがいい | game-genre-301088-mid1 / game-genre-301088-mid2 / game-genre-301088-sticky | 2124_300_250 |
| game-genre-301090.html | ゲーム × シナリオがいい | game-genre-301090-mid1 / game-genre-301090-mid2 / game-genre-301090-sticky | 2124_300_250 |
| game-genre-301119.html | ゲーム × 世界観がいい | game-genre-301119-mid1 / game-genre-301119-mid2 / game-genre-301119-sticky | 2124_300_250 |
| game-genre-7037.html | ゲーム × 巨乳 | game-genre-7037-mid1 / game-genre-7037-mid2 / game-genre-7037-sticky | 2124_300_250 |
| game-genre-7203.html | ゲーム × 辱め | game-genre-7203-mid1 / game-genre-7203-mid2 / game-genre-7203-sticky | 2124_300_250 |
| game-genre-7213.html | ゲーム × 恋愛 | game-genre-7213-mid1 / game-genre-7213-mid2 / game-genre-7213-sticky | 2124_300_250 |
| game-genre-7252.html | ゲーム × ハーレム | game-genre-7252-mid1 / game-genre-7252-mid2 / game-genre-7252-sticky | 2124_300_250 |
| game-genre-7301.html | ゲーム × 制服 | game-genre-7301-mid1 / game-genre-7301-mid2 / game-genre-7301-sticky | 2124_300_250 |
| game-genre-7466.html | ゲーム × 萌えゲーアワード/美少女ゲームアワード受賞作品 | game-genre-7466-mid1 / game-genre-7466-mid2 / game-genre-7466-sticky | 2124_300_250 |
| game-genre-7501.html | ゲーム × ファンタジー | game-genre-7501-mid1 / game-genre-7501-mid2 / game-genre-7501-sticky | 2124_300_250 |
| game-genre-7502.html | ゲーム × 学園もの | game-genre-7502-mid1 / game-genre-7502-mid2 / game-genre-7502-sticky | 2124_300_250 |
