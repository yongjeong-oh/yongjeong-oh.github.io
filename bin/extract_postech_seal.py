"""Prepare the official POSTECH emblem PNG.

Source: POSTECH official brand bundle (POSTECH_엠블럼_01.jpg) downloaded from
https://www.postech.ac.kr/_res/postech/kor/etc/logo_1802.zip. We convert
the JPEG to a PNG with the white background made transparent so it sits
cleanly next to the year badge in the Education section.
"""

from pathlib import Path

from PIL import Image

LOGOS = Path(
    r"C:\Users\Yongjeong\OneDrive - Singapore University of Technology and Design"
    r"\바탕 화면\yongjeong-oh.github.io\assets\img\logos"
)
SRC = LOGOS / "_unzipped" / "logo_1802" / "logo_JPG" / "POSTECH_엠블럼_01.jpg"
OUT = LOGOS / "postech.png"

WHITE_THRESHOLD = 245  # pixels brighter than this become transparent


def main() -> None:
    img = Image.open(SRC).convert("RGBA")
    pixels = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, _ = pixels[x, y]
            if r >= WHITE_THRESHOLD and g >= WHITE_THRESHOLD and b >= WHITE_THRESHOLD:
                pixels[x, y] = (255, 255, 255, 0)

    bbox = img.getbbox()
    if bbox is not None:
        img = img.crop(bbox)

    target = 320
    img.thumbnail((target, target), Image.LANCZOS)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT.name} ({OUT.stat().st_size / 1024:.1f} KB, {img.size})")


if __name__ == "__main__":
    main()
