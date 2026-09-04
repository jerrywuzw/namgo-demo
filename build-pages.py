#!/usr/bin/env python3
"""
Generate the dedicated comparison pages from index.html.

index.html is the single source of truth. This copies it into a subdirectory
per comparison, activates that view instead of the home view, rewrites the
head tags so each URL has its own title/description/canonical, and fixes the
relative links for being one directory deeper.

Run after editing index.html:

    python3 build-pages.py

No dependencies, no build step in the usual sense — it is a copy with a few
substitutions, so the three pages can never drift apart in styling.
"""

import io
import os
import re
import sys

SITE = "https://jerrywuzw.github.io/namgo-demo/"

PAGES = [
    {
        "slug": "vs-printful",
        "view": "view-vs-printful",
        "title": "NAMGO vs. Printful — merch without running the shop",
        "description": (
            "Printful sells fulfilment to someone who has already built the store, made "
            "the designs and found the buyers. NAMGO does that work: we design, make, "
            "ship and sell, and the shop pays nothing on Storefront."
        ),
        "og_title": "NAMGO vs. Printful",
    },
    {
        "slug": "vs-clover",
        "view": "view-vs-clover",
        "title": "NAMGO vs. Clover — a storefront that earns instead of costing",
        "description": (
            "Clover sells the register, and its website is sold on top of that "
            "commitment. NAMGO sells merch and the digital presence that carries it, "
            "alongside whatever POS the shop already runs."
        ),
        "og_title": "NAMGO vs. Clover",
    },
]


def build(src, page):
    html = src

    # activate this comparison instead of the home view
    html = html.replace('<main id="view-home" class="view active">',
                        '<main id="view-home" class="view">', 1)
    marker = '<main id="%s" class="view">' % page["view"]
    if marker not in html:
        sys.exit("could not find %s in index.html" % page["view"])
    html = html.replace(marker, '<main id="%s" class="view active">' % page["view"], 1)

    # its own head, so the URL is worth sharing and worth indexing
    html = re.sub(r"<title>.*?</title>", "<title>%s</title>" % page["title"], html, count=1)
    html = re.sub(r'(<meta name="description" content=")[^"]*(">)',
                  lambda m: m.group(1) + page["description"] + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:title" content=")[^"]*(">)',
                  lambda m: m.group(1) + page["og_title"] + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:description" content=")[^"]*(">)',
                  lambda m: m.group(1) + page["description"] + m.group(2), html, count=1)
    html = re.sub(r'(<link rel="canonical" href=")[^"]*(">)',
                  lambda m: m.group(1) + SITE + page["slug"] + "/" + m.group(2), html, count=1)

    # the page now sits one directory deeper
    html = html.replace('href="vs-printful/"', 'href="../vs-printful/"')
    html = html.replace('href="vs-clover/"', 'href="../vs-clover/"')
    html = html.replace('href="./"', 'href="../"')

    os.makedirs(page["slug"], exist_ok=True)
    out = os.path.join(page["slug"], "index.html")
    io.open(out, "w", encoding="utf-8").write(html)
    return out, len(html)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    src = io.open("index.html", encoding="utf-8").read()
    for page in PAGES:
        out, size = build(src, page)
        print("wrote %-24s %6d bytes" % (out, size))


if __name__ == "__main__":
    main()
