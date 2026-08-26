"""Export Bambie Digital Works logo pack sizes from source masters."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

PACK = Path(__file__).resolve().parent
SOURCE = PACK / "source"
WEB = PACK / "web"
APP = PACK / "app"
GITHUB = PACK / "github"

# Brand fill for letterboxed social/banner frames (navy from logo palette)
LIGHT_FILL = (232, 238, 245)  # soft studio blue-gray
DARK_FILL = (11, 18, 32)  # #0B1220


def open_rgb(path: Path) -> Image.Image:
    return Image.open(path).convert("RGBA")


def resize_contain(
    img: Image.Image,
    size: tuple[int, int],
    fill: tuple[int, int, int],
    pad_ratio: float = 0.08,
) -> Image.Image:
    """Fit image inside target with padding; fill remaining with solid color."""
    tw, th = size
    pad_x = int(tw * pad_ratio)
    pad_y = int(th * pad_ratio)
    avail_w = max(1, tw - 2 * pad_x)
    avail_h = max(1, th - 2 * pad_y)
    scale = min(avail_w / img.width, avail_h / img.height)
    nw = max(1, int(img.width * scale))
    nh = max(1, int(img.height * scale))
    resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", size, fill + (255,))
    x = (tw - nw) // 2
    y = (th - nh) // 2
    canvas.paste(resized, (x, y), resized if resized.mode == "RGBA" else None)
    return canvas


def save_png(img: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = img.convert("RGBA")
    out.save(path, format="PNG", optimize=True)
    print(f"  wrote {path.relative_to(PACK)} ({out.width}x{out.height})")


def square_resize(img: Image.Image, size: int) -> Image.Image:
    return img.resize((size, size), Image.Resampling.LANCZOS)


def main() -> None:
    mark_light = open_rgb(SOURCE / "mark-square.png")
    mark_dark = open_rgb(SOURCE / "mark-square-dark.png")
    lockup_light = open_rgb(SOURCE / "lockup-light.png")
    lockup_dark = open_rgb(SOURCE / "lockup-dark.png")

    print("Web assets...")
    # Favicons from light mark (readable on browser tabs)
    for size, name in ((16, "favicon-16x16.png"), (32, "favicon-32x32.png")):
        save_png(square_resize(mark_light, size), WEB / name)

    ico_path = WEB / "favicon.ico"
    # Pillow derives each ICO size from the source image
    square_resize(mark_light, 256).save(
        ico_path,
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
    )
    print(f"  wrote {ico_path.relative_to(PACK)}")

    save_png(square_resize(mark_light, 180), WEB / "apple-touch-icon.png")
    save_png(square_resize(mark_light, 192), WEB / "icon-192.png")
    save_png(square_resize(mark_light, 512), WEB / "icon-512.png")

    # Header lockups: constrain width, preserve aspect
    def lockup_width(img: Image.Image, width: int) -> Image.Image:
        h = max(1, int(img.height * (width / img.width)))
        return img.resize((width, h), Image.Resampling.LANCZOS)

    save_png(lockup_width(lockup_light, 800), WEB / "logo-lockup.png")
    save_png(lockup_width(lockup_light, 1600), WEB / "logo-lockup@2x.png")
    save_png(
        resize_contain(lockup_light, (1200, 630), LIGHT_FILL, pad_ratio=0.06),
        WEB / "og-image.png",
    )

    print("App icons...")
    for size in (1024, 512, 256, 128, 64):
        save_png(square_resize(mark_light, size), APP / f"icon-{size}.png")

    print("GitHub assets...")
    save_png(square_resize(mark_light, 1024), GITHUB / "avatar.png")
    save_png(
        resize_contain(lockup_light, (1280, 640), LIGHT_FILL, pad_ratio=0.07),
        GITHUB / "social-preview.png",
    )
    save_png(
        resize_contain(lockup_light, (1280, 400), LIGHT_FILL, pad_ratio=0.05),
        GITHUB / "readme-banner.png",
    )

    # Also keep dark variants handy next to web/github for theme choice
    save_png(
        resize_contain(lockup_dark, (1200, 630), DARK_FILL, pad_ratio=0.06),
        WEB / "og-image-dark.png",
    )
    save_png(
        resize_contain(lockup_dark, (1280, 640), DARK_FILL, pad_ratio=0.07),
        GITHUB / "social-preview-dark.png",
    )
    save_png(
        resize_contain(lockup_dark, (1280, 400), DARK_FILL, pad_ratio=0.05),
        GITHUB / "readme-banner-dark.png",
    )
    save_png(square_resize(mark_dark, 1024), GITHUB / "avatar-dark.png")
    save_png(lockup_width(lockup_dark, 800), WEB / "logo-lockup-dark.png")
    save_png(lockup_width(lockup_dark, 1600), WEB / "logo-lockup-dark@2x.png")

    print("Done.")


if __name__ == "__main__":
    main()
