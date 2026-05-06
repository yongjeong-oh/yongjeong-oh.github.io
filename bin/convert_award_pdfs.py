"""Convert award certificate PDFs to JPEG images for the website.

Reads source PDFs from the user's local certificate folder and writes
JPEGs into assets/img/awards/. Filenames mirror the slugs already used
in _pages/about.md so the iframe -> img swap stays trivial.
"""

from pathlib import Path

import pymupdf

SRC_DIR = Path(
    r"C:\Users\Yongjeong\OneDrive - Singapore University of Technology and Design"
    r"\바탕 화면\POSTECH컴퓨터\바탕화면\상장들"
)
OUT_DIR = Path(
    r"C:\Users\Yongjeong\OneDrive - Singapore University of Technology and Design"
    r"\바탕 화면\yongjeong-oh.github.io\assets\img\awards"
)

# (source pdf, output slug, list of 1-indexed pages to render -- empty == all)
JOBS = [
    ("scan_20010317001703.pdf", "piuri-postdoc-2026", [1]),
    ("scan2.pdf", "postechee-excellence-2026", [1]),
    ("scan_20010317001428.pdf", "best-doctoral-dissertation-2026", [1]),
    ("scan_20010317001534.pdf", "samsung-humantech-bronze-2026", [1, 2]),
    ("scan_20010317001456.pdf", "postechian-fellowship-2025", [1]),
    ("KICS.pdf", "kics-summer-2023", [1]),
    ("scan_20010317001358.pdf", "best-master-thesis-2023", [1]),
    ("postech-EE.pdf", "postechee-excellence-2023", [1]),
    ("scan_20010317001330.pdf", "kics-summer-2022", [1]),
]

# 200 DPI -> ~1.65x mat zoom; readable text without bloating files.
ZOOM = 200 / 72


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    matrix = pymupdf.Matrix(ZOOM, ZOOM)

    for src_name, slug, pages in JOBS:
        src = SRC_DIR / src_name
        if not src.exists():
            print(f"MISSING: {src}")
            continue

        with pymupdf.open(src) as doc:
            page_indices = [p - 1 for p in pages] if pages else range(len(doc))
            multi = len(list(page_indices)) > 1
            for idx in page_indices:
                page = doc.load_page(idx)
                pix = page.get_pixmap(matrix=matrix, alpha=False)
                if multi:
                    out = OUT_DIR / f"{slug}-p{idx + 1}.jpg"
                else:
                    out = OUT_DIR / f"{slug}.jpg"
                pix.pil_save(out, format="JPEG", quality=85, optimize=True)
                size_kb = out.stat().st_size / 1024
                print(f"wrote {out.name} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
