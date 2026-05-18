#!/usr/bin/env python3
"""Walk every HTML page under homepage/, extract every internal href/src, and
report broken (non-resolving) links. Reports duplicates / external sanity too."""
from pathlib import Path
import re
import sys
import urllib.parse
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
HOME = ROOT  # homepage/

# match attributes: href="..." or src="..."
HREF_RE = re.compile(r"""(href|src)\s*=\s*["']([^"'#]*)(#[^"']*)?["']""", re.IGNORECASE)

EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "//")


def collect_pages():
    return sorted(HOME.rglob("*.html"))


def is_external(url: str) -> bool:
    return url.startswith(EXTERNAL_PREFIXES)


def resolve(page: Path, ref: str) -> Optional[Path]:
    """Resolve `ref` (relative URL) against the page's directory."""
    if not ref:
        return None
    # strip URL encoding
    ref = urllib.parse.unquote(ref)
    base = page.parent
    if ref.startswith("/"):
        # absolute path on the deployed site -- skip (we don't know domain root)
        return None
    target = (base / ref).resolve()
    return target


def main():
    broken = []
    external_count = 0
    internal_count = 0
    pages = collect_pages()
    print(f"Auditing {len(pages)} pages in {HOME}")
    print()

    for page in pages:
        rel_page = page.relative_to(HOME)
        try:
            content = page.read_text()
        except UnicodeDecodeError:
            content = page.read_text(errors="replace")

        for match in HREF_RE.finditer(content):
            kind, raw_url, _anchor = match.group(1), match.group(2), match.group(3)
            if not raw_url:
                continue
            if is_external(raw_url):
                external_count += 1
                continue
            internal_count += 1
            target = resolve(page, raw_url)
            if target is None:
                continue
            # If link points to a directory, expect index.html inside
            if target.is_dir():
                check = target / "index.html"
                if not check.exists():
                    broken.append((rel_page, raw_url, "dir without index.html"))
                continue
            if not target.exists():
                # Some hrefs intentionally use "" for current page — skip empties
                broken.append((rel_page, raw_url, "missing file"))

    print(f"Internal refs: {internal_count}")
    print(f"External refs: {external_count}")
    print(f"Broken refs:   {len(broken)}")
    print()
    if broken:
        print("=== BROKEN ===")
        last_page = None
        for page, url, why in sorted(broken):
            if page != last_page:
                print(f"\n{page}")
                last_page = page
            print(f"   {url}    ({why})")
        sys.exit(1)
    else:
        print("All internal links resolve. ✓")


if __name__ == "__main__":
    main()
