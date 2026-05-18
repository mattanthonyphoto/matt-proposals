#!/usr/bin/env python3
"""Check every HTML page has: title, meta description, canonical, viewport, h1 (one), proper image alt text."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
HOME = ROOT


def collect_pages():
    return sorted(HOME.rglob("*.html"))


def main():
    pages = collect_pages()
    print(f"{'PAGE':<58}  {'TITLE':<5}  {'DESC':<5}  {'CANO':<5}  {'VPRT':<5}  {'H1':<3}  {'IMG-NO-ALT':<10}")
    print("-" * 110)
    any_issue = False
    for page in pages:
        rel = page.relative_to(HOME)
        c = page.read_text(errors="replace")
        title = bool(re.search(r'<title>.+?</title>', c, re.DOTALL))
        desc = bool(re.search(r'<meta\s+name=["\']description["\']', c, re.IGNORECASE))
        canon = bool(re.search(r'<link\s+rel=["\']canonical["\']', c, re.IGNORECASE))
        vp = bool(re.search(r'<meta\s+name=["\']viewport["\']', c, re.IGNORECASE))
        h1_count = len(re.findall(r'<h1\b', c))
        imgs = re.findall(r'<img\b[^>]*>', c)
        imgs_no_alt = [i for i in imgs if not re.search(r'\balt\s*=', i)]

        flags = "OK"
        marks = [("y" if title else "MISS"),
                 ("y" if desc else "MISS"),
                 ("y" if canon else "MISS"),
                 ("y" if vp else "MISS"),
                 (str(h1_count) if h1_count == 1 else f"{h1_count}!"),
                 (str(len(imgs_no_alt)) if imgs_no_alt else "0")]
        if not all([title, desc, vp]) or h1_count != 1 or imgs_no_alt:
            any_issue = True
        print(f"{str(rel):<58}  {marks[0]:<5}  {marks[1]:<5}  {marks[2]:<5}  {marks[3]:<5}  {marks[4]:<3}  {marks[5]:<10}")

    print()
    print("Note: redirect pages may have 0 h1 by design.")
    if any_issue:
        print("⚠ See flags above")


if __name__ == "__main__":
    main()
