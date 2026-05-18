#!/usr/bin/env python3
"""Extract nav link text + counts for each page, plus footer column counts."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
HOME = ROOT


def collect_pages():
    return sorted(HOME.rglob("*.html"))


NAV_RE = re.compile(r'<nav class="(?:site|primary)".*?</nav>', re.DOTALL)
LINK_TEXT_RE = re.compile(r'<a[^>]*>(.*?)</a>', re.DOTALL)
FOOTER_RE = re.compile(r'<footer class="site">(.*?)</footer>', re.DOTALL)
FOOTER_H4_RE = re.compile(r'<h4[^>]*>(.*?)</h4>', re.DOTALL)


def strip(text: str) -> str:
    # remove inner HTML tags and collapse whitespace
    text = re.sub(r'<[^>]+>', '', text)
    return re.sub(r'\s+', ' ', text).strip()


def main():
    pages = collect_pages()
    print(f"{'PAGE':<58}  {'NAV-ITEMS':<45}  FOOTER COLS")
    print("-" * 130)

    issues = []
    for page in pages:
        rel = page.relative_to(HOME)
        content = page.read_text(errors="replace")
        nav = NAV_RE.search(content)
        if not nav:
            issues.append((rel, "NO NAV found"))
            print(f"{str(rel):<58}  -- no nav --")
            continue
        nav_text = nav.group(0)
        link_texts = [strip(t) for t in LINK_TEXT_RE.findall(nav_text)]
        link_texts = [t for t in link_texts if t]  # drop empty

        footer = FOOTER_RE.search(content)
        if footer:
            cols = [strip(h) for h in FOOTER_H4_RE.findall(footer.group(0))]
        else:
            cols = ["NO FOOTER"]

        labels = " / ".join(link_texts)
        if len(labels) > 43:
            labels = labels[:40] + "..."

        col_summary = " · ".join(cols)
        print(f"{str(rel):<58}  {labels:<45}  {col_summary}")

    if issues:
        print()
        print("Issues:")
        for rel, msg in issues:
            print(f"   {rel}: {msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
