from __future__ import annotations

from pathlib import Path
from textwrap import dedent

from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "brand"
DESKTOP = Path("/Users/victorpimentel/Desktop")

BLUE = "#0F5BD3"
CYAN = "#16D0D5"
NAVY = "#071A3D"
MIST = "#EFF6FF"


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


def write_svg(path: Path, content: str) -> None:
    path.write_text(dedent(content).strip() + "\n")


def build_logo_variants() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)

    write_svg(
        ASSETS / "logo-avant-primary.svg",
        f"""
        <svg width="1180" height="360" viewBox="0 0 1180 360" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="1180" height="360" rx="36" fill="white"/>
          <path d="M238 64L299 231L360 64L325 92L299 167L273 92L238 64Z" fill="{CYAN}"/>
          <text x="54" y="235" fill="{BLUE}" font-size="168" font-weight="800" font-family="'Oxanium', 'Montserrat', sans-serif" letter-spacing="-6">A</text>
          <text x="375" y="235" fill="{BLUE}" font-size="168" font-weight="800" font-family="'Oxanium', 'Montserrat', sans-serif" letter-spacing="-6">ANT</text>
          <text x="160" y="304" fill="{BLUE}" font-size="44" font-weight="500" font-family="'Sora', 'Arial', sans-serif" letter-spacing="14">AGENCIA DIGITAL</text>
        </svg>
        """,
    )

    write_svg(
        ASSETS / "logo-avant-light.svg",
        f"""
        <svg width="1180" height="360" viewBox="0 0 1180 360" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="1180" height="360" rx="36" fill="{NAVY}"/>
          <path d="M238 64L299 231L360 64L325 92L299 167L273 92L238 64Z" fill="{CYAN}"/>
          <text x="54" y="235" fill="white" font-size="168" font-weight="800" font-family="'Oxanium', 'Montserrat', sans-serif" letter-spacing="-6">A</text>
          <text x="375" y="235" fill="white" font-size="168" font-weight="800" font-family="'Oxanium', 'Montserrat', sans-serif" letter-spacing="-6">ANT</text>
          <text x="160" y="304" fill="{MIST}" font-size="44" font-weight="500" font-family="'Sora', 'Arial', sans-serif" letter-spacing="14">AGENCIA DIGITAL</text>
        </svg>
        """,
    )

    write_svg(
        ASSETS / "logo-avant-dark.svg",
        f"""
        <svg width="1180" height="360" viewBox="0 0 1180 360" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="1180" height="360" rx="36" fill="{MIST}"/>
          <path d="M238 64L299 231L360 64L325 92L299 167L273 92L238 64Z" fill="{CYAN}"/>
          <text x="54" y="235" fill="{NAVY}" font-size="168" font-weight="800" font-family="'Oxanium', 'Montserrat', sans-serif" letter-spacing="-6">A</text>
          <text x="375" y="235" fill="{NAVY}" font-size="168" font-weight="800" font-family="'Oxanium', 'Montserrat', sans-serif" letter-spacing="-6">ANT</text>
          <text x="160" y="304" fill="{BLUE}" font-size="44" font-weight="500" font-family="'Sora', 'Arial', sans-serif" letter-spacing="14">AGENCIA DIGITAL</text>
        </svg>
        """,
    )

    write_svg(
        ASSETS / "logo-avant-symbol.svg",
        f"""
        <svg width="512" height="512" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="512" height="512" rx="96" fill="{NAVY}"/>
          <path d="M160 92L256 352L352 92L297 136L256 253L215 136L160 92Z" fill="{CYAN}"/>
        </svg>
        """,
    )

    write_svg(
        ASSETS / "logo-avant-avatar.svg",
        f"""
        <svg width="512" height="512" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="512" height="512" rx="128" fill="white"/>
          <path d="M160 92L256 352L352 92L297 136L256 253L215 136L160 92Z" fill="{CYAN}"/>
          <circle cx="256" cy="256" r="220" stroke="{BLUE}" stroke-opacity="0.08" stroke-width="16"/>
        </svg>
        """,
    )


def main() -> None:
    remove_white_background(
        DESKTOP / "LOGO AVANT-05.png",
        ASSETS / "logo-avant-05-transparent.png",
    )
    remove_white_background(
        DESKTOP / "LOGO AVANT-04.png",
        ASSETS / "logo-avant-04-transparent.png",
    )
    build_logo_variants()


if __name__ == "__main__":
    main()
