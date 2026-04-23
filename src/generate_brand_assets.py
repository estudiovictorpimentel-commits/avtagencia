from __future__ import annotations

from pathlib import Path
from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "brand"
DESKTOP = Path("/Users/victorpimentel/Desktop")


def remove_white_background(source: Path, target: Path) -> None:
    image = Image.open(source).convert("RGBA")
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if r > 245 and g > 245 and b > 245:
                pixels[x, y] = (255, 255, 255, 0)

    bbox = image.getbbox()
    if bbox:
        image = image.crop(bbox)

    image.save(target)

def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    remove_white_background(
        DESKTOP / "LOGO AVANT-05.png",
        ASSETS / "logo-avant-05-transparent.png",
    )
    remove_white_background(
        DESKTOP / "LOGO AVANT-04.png",
        ASSETS / "logo-avant-04-transparent.png",
    )


if __name__ == "__main__":
    main()
