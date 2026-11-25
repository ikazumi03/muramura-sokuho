# むらむら速報｜FANZA（DMM）コード不足リスト

作成日：2026年11月26日
前提：DMMアフィリエイトは2026年11月25日に審査通過済み（アフィリエイトID: murasoku-001）。DLsite指定枠（dlsite.html 3枠＋index-dlsite）は全て設置済み。本リストは、まだ空（準備中表示）のFANZA指定枠に必要な公式コードの一覧。

## 必要なもの（共通）
- 各枠とも、DMMアフィリエイト管理画面（またはFANZA各サービスの「アフィリエイトツールバー」／「キーワードでリンク作成」「バナーリンク作成」）で発行する**公式バナーコード（affiliate_id=murasoku-001）**。改変せずそのまま設置する。
- トップページ設置済みの2枠はウィジェットバナー方式（widget-view.dmm.co.jp の banner_placement.js、banner_id=2124）。同じ方式でカテゴリ別バナーが発行できる場合はそれを優先。
- 全枠の推奨サイズは **300x250**（レクタングル）。
- 合計：**32枠**（内訳：ブックス3／動画3／ゲーム3／同人3／総合20）

## カテゴリ別

### FANZAブックス（電子書籍・漫画）— 3枠
| 枠ID | ページ | 位置 | サイズ |
|---|---|---|---|
| guide-ebook-top | guide-ebook.html | 冒頭 | 300x250 |
| guide-ebook-sidebar | guide-ebook.html | 目次下（サイドバー） | 300x250 |
| guide-ebook-bottom | guide-ebook.html | 記事末 | 300x250 |

必要なコード：FANZAブックスのバナーコード 300x250（トップ設置済みの90%OFFクーポン系 banner_id=2124 のカテゴリ版、またはブックスのキャンペーン素材）。ダイレクトリンクの場合はブックス宛リンク。

### FANZA動画 — 3枠
| 枠ID | ページ | 位置 | サイズ |
|---|---|---|---|
| guide-video-top | guide-video.html | 冒頭 | 300x250 |
| guide-video-sidebar | guide-video.html | 目次下（サイドバー） | 300x250 |
| guide-video-bottom | guide-video.html | 記事末 | 300x250 |

必要なコード：FANZA動画（見放題／単品）のバナーコード 300x250。

### FANZAゲーム — 3枠
| 枠ID | ページ | 位置 | サイズ |
|---|---|---|---|
| guide-game-top | guide-game.html | 冒頭 | 300x250 |
| guide-game-sidebar | guide-game.html | 目次下（サイドバー） | 300x250 |
| guide-game-bottom | guide-game.html | 記事末 | 300x250 |

必要なコード：FANZAゲームのバナーコード 300x250。

### FANZA同人 — 3枠
| 枠ID | ページ | 位置 | サイズ |
|---|---|---|---|
| guide-doujin-top | guide-doujin.html | 冒頭 | 300x250 |
| guide-doujin-sidebar | guide-doujin.html | 目次下（サイドバー） | 300x250 |
| guide-doujin-bottom | guide-doujin.html | 記事末 | 300x250 |

必要なコード：FANZA同人のバナーコード 300x250。

### FANZA総合 — 20枠
| 枠ID | ページ | 位置 | サイズ |
|---|---|---|---|
| beginner-top | beginner.html | 冒頭 | 300x250 |
| beginner-sidebar | beginner.html | 目次下（サイドバー） | 300x250 |
| beginner-bottom | beginner.html | 記事末 | 300x250 |
| price-top | price.html | 冒頭 | 300x250 |
| price-sidebar | price.html | 目次下（サイドバー） | 300x250 |
| price-bottom | price.html | 記事末 | 300x250 |
| campaign-top | campaign.html | 冒頭 | 300x250 |
| campaign-sidebar | campaign.html | 目次下（サイドバー） | 300x250 |
| campaign-bottom | campaign.html | 記事末 | 300x250 |
| payment-top | payment.html | 冒頭 | 300x250 |
| payment-sidebar | payment.html | 目次下（サイドバー） | 300x250 |
| payment-bottom | payment.html | 記事末 | 300x250 |
| faq-top | faq.html | 冒頭 | 300x250 |
| faq-sidebar | faq.html | 目次下（サイドバー） | 300x250 |
| faq-bottom | faq.html | 記事末 | 300x250 |
| safety-sidebar | safety.html | 目次下（サイドバー） | 300x250 |
| safety-bottom | safety.html | 記事末 | 300x250 |
| about-bottom | about.html | 記事末 | 300x250 |
| policy-bottom | policy.html | 記事末 | 300x250 |
| contact-bottom | contact.html | 記事末 | 300x250 |

必要なコード：FANZA総合（ポータル）のバナーコード 300x250。信頼系ページ（safety／about／policy／contact）は設置優先度は最後（ad-slots.mdの優先順位どおり）。

## 設置済み（参考・不足なし）
- index-middle（FANZAブックス ウィジェット 640x200、banner_id=2124）／index-bottom（FANZAブックス ウィジェット 300x250、banner_id=2124）— 2026-11-25設置
- DLsite：dlsite-top／dlsite-sidebar／dlsite-bottom（公式バナー・テキスト、aid=murasoku）／index-dlsite（公式テキストリンク）— 全て設置済み

## コードが揃ったら
1. もち：各枠へ公式コードをそのまま設置（「広告」ラベルは現行CSSのまま枠内に表示）
2. もち：ops/site_audit.py で監査（要修正0）→ push → 公開ページで表示確認
3. もち：ops/広告台帳.csv の当該枠を「設置済み」に更新
