#!/usr/bin/env python3
"""Dependency-free static content audit for むらむら速報 (FANZA guide site).
Does not browse affiliate links or access any private ASP account.
"""
from __future__ import annotations
import csv
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import argparse, json, re, sys

ROOT=Path(__file__).resolve().parents[1]
PAGES=sorted(ROOT.glob('*.html'))

class PageReader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links=[]; self.title=''; self._intitle=False
        self.descriptions=[]; self.h1=0
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='title': self._intitle=True
        if tag=='h1': self.h1+=1
        if tag=='a' and attrs.get('href'): self.links.append(attrs['href'])
        if tag=='link' and attrs.get('href'): self.links.append(attrs['href'])
        if tag=='script' and attrs.get('src'): self.links.append(attrs['src'])
        if tag=='meta' and attrs.get('name')=='description': self.descriptions.append(attrs.get('content',''))
    def handle_endtag(self,tag):
        if tag=='title': self._intitle=False
    def handle_data(self,data):
        if self._intitle: self.title+=data

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--base-url',default='',help='Optional publicly deployed URL for reporting only')
    args=parser.parse_args()
    report={'timestamp_utc':datetime.now(timezone.utc).isoformat(), 'page_count':len(PAGES), 'base_url':args.base_url,'errors':[], 'warnings':[], 'pages':[],'ad_candidates':0}
    for path in PAGES:
        src=path.read_text(encoding='utf-8')
        p=PageReader(); p.feed(src)
        issues=[]
        if not p.title.strip(): issues.append('title がありません')
        if not p.descriptions or not p.descriptions[0].strip(): issues.append('meta description がありません')
        if p.h1 !=1: issues.append(f'h1 は1個が望ましい（現在 {p.h1}個）')
        if 'アフィリエイト' not in src and 'PR' not in src and '広告' not in src: issues.append('広告・PRの表記を要確認')
        if '18歳' not in src: issues.append('18歳以上向けの明記を要確認')
        for href in p.links:
            split=urlsplit(href)
            if split.scheme in ('http','https','mailto','tel') or href.startswith('//') or href.startswith('#'): continue
            if split.scheme or href.startswith('javascript:'): issues.append(f'不審なリンク: {href}');continue
            item=(path.parent / split.path).resolve()
            if not item.is_relative_to(ROOT) or not item.exists(): issues.append(f'内部リンク/アセットがありません: {href}')
        report['pages'].append({'file':path.name,'title':p.title.strip(),'issues':issues})
        for issue in issues: report['errors'].append(f'{path.name}: {issue}')
    adcsv=ROOT/'ops'/'広告候補一覧.csv'
    if adcsv.exists():
        with adcsv.open(encoding='utf-8-sig',newline='') as f:
            candidates=list(csv.DictReader(f))
        report['ad_candidates']=len(candidates)
        for row in candidates:
            if not row.get('提携状況'): report['warnings'].append(f"広告候補 {row.get('案件名')}: 提携状況が未設定")
    if not args.base_url:
        report['warnings'].append('公開URLは未設定です。GitHubの変数 SITE_URL に pages.dev URLを設定可能です（任意）。')
    report['warnings'].append('DMMアフィリエイト側の審査、成果報酬、利用料金、最新規約は自動検証していません。')
    out=ROOT/'reports';out.mkdir(exist_ok=True)
    (out/'latest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    lines=['# サイト自動点検レポート（むらむら速報）', '',f"- 検査日時 (UTC): {report['timestamp_utc']}",f"- HTMLページ数: {len(PAGES)}",f"- 広告候補: {report['ad_candidates']}件",f"- 要修正: {len(report['errors'])}件",'']
    for label,vals in [('要修正',report['errors']),('注意事項',report['warnings'])]:
        lines.append('## '+label)
        lines.extend('- '+v for v in vals) if vals else lines.append('- なし')
        lines.append('')
    (out/'latest.md').write_text('\n'.join(lines),encoding='utf-8')
    print('\n'.join(lines))
    return 1 if report['errors'] else 0
if __name__=='__main__': sys.exit(main())
