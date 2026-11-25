# むらむら速報｜FANZA（DMM）コード設置記録

作成日：2026年11月26日（旧「コード不足リスト」）
**状態：全32枠 設置完了（2026-11-26）** — DMMアフィリエイト（アフィリエイトID: murasoku-001）の公式ウィジェットバナーコードを、各枠のプレースホルダと差し替えて設置済み。サイト監査（ops/site_audit.py）要修正0でpushし、公開ページで配信を確認済み。詳細は ops/広告台帳.csv を参照。

> ⚠️ **要対応：FANZA同人バナー（banner_id=2166_300_250）は表示終了 2026-11-30 15:59**
> guide-doujin.html の3枠（guide-doujin-top／-sidebar／-bottom）に設置した同人EXPOバナーは **2026-11-30 15:59 で表示が止まる**。それまでに代替バナーコードを取得して差し替えること。台帳CSVの該当3行の備考にも「バナー表示終了 2026-11-30 15:59・要差し替え」と明記済み。

## 設置内容（2026-11-26）

方式：全枠ともウィジェットバナー（`https://widget-view.dmm.co.jp/js/banner_placement.js?affiliate_id=murasoku-001&banner_id=...`）300x250。コードは発行どおり無改変で設置。枠のラッパー・data属性・「広告」ラベルは従来どおり。

### カテゴリ別（各3枠：top／sidebar／bottom）
| カテゴリ | ページ | banner_id |
|---|---|---|
| FANZAブックス | guide-ebook.html | 2124_300_250 |
| FANZA動画 | guide-video.html | 67_300_250 |
| FANZAゲーム | guide-game.html | 258_300_250 |
| FANZA同人 | guide-doujin.html | 2166_300_250（⚠️ 2026-11-30 15:59 表示終了・要差し替え） |

### FANZA総合（20枠）
- beginner.html／price.html／campaign.html／payment.html／faq.html：各 top／sidebar／bottom（15枠）
- safety.html：sidebar／bottom（2枠）
- about.html／policy.html／contact.html：各 bottom（1枠ずつ・3枠）
- 使用バナー：FANZAブックス 90%OFFクーポン 300x250（banner_id=2124_300_250）— トップページ index-bottom の総合枠と同じ素材。

## 設置済み（従来分・参考）
- index-middle（FANZAブックス ウィジェット 640x200、banner_id=2124_640_200）／index-bottom（FANZAブックス ウィジェット 300x250、banner_id=2124_300_250）— 2026-11-25設置
- DLsite：dlsite-top／dlsite-sidebar／dlsite-bottom（公式バナー・テキスト、aid=murasoku）／index-dlsite（公式テキストリンク）— 全て設置済み

## 残タスク
1. **2026-11-30 15:59 までに** FANZA同人の代替バナーコードを取得し、guide-doujin.html の3枠を差し替える。
2. DLsiteバナーコードを取得したら index-dlsite のテキストリンクをバナーへ差し替え（台帳備考参照）。
