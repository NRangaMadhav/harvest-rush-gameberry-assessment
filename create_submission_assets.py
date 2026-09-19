from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"


def font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def create_transparent_hero():
    source = Image.open(ASSETS / "hero.png").convert("RGBA")
    pixels = source.load()
    for y in range(source.height):
        for x in range(source.width):
            r, g, b, a = pixels[x, y]
            # Remove the pale blue presentation background while preserving the hero.
            if b > 220 and g > 220 and r > 210:
                pixels[x, y] = (r, g, b, 0)
    source.save(ASSETS / "hero-transparent.png")


def create_presentation_sheet():
    sheet = Image.new("RGB", (1600, 1120), "#f6faf0")
    draw = ImageDraw.Draw(sheet)
    draw.rectangle((0, 0, 1600, 145), fill="#b21a5d")
    draw.text((70, 36), "HARVEST RUSH", fill="white", font=font(56, True))
    draw.text((72, 98), "Farm Dash — Gen AI Designer Assessment", fill="#ffd6e8", font=font(25))

    cards = [
        ("01  HERO / VARIANT", ASSETS / "hero-transparent.png", (70, 205, 710, 690)),
        ("02  GAMEPLAY / LOBBY", ASSETS / "gameplay.png", (890, 205, 1530, 690)),
        ("03  FARM WORLD / BACKGROUND", ASSETS / "background.png", (70, 770, 710, 1050)),
        ("04  COLLECTIBLES / ITEMS", ASSETS / "items.png", (890, 770, 1530, 1050)),
    ]
    for label, path, box in cards:
        x1, y1, x2, y2 = box
        draw.rounded_rectangle(box, radius=24, fill="white", outline="#d9e7d0", width=3)
        draw.text((x1 + 22, y1 + 18), label, fill="#1d6c35", font=font(23, True))
        if label.startswith("01"):
            images = [
                Image.open(ASSETS / "hero-transparent.png").convert("RGBA"),
                Image.open(ASSETS / "hero-variant.png").convert("RGBA"),
            ]
            for image_index, image in enumerate(images):
                image.thumbnail((260, y2 - y1 - 100))
                ix = x1 + 85 + image_index * 285
                iy = y1 + 72 + (y2 - y1 - 90 - image.height) // 2
                sheet.paste(image, (ix, iy), image)
            draw.text((x1 + 120, y2 - 42), "BASE HERO", fill="#5d5d5d", font=font(16, True))
            draw.text((x1 + 405, y2 - 42), "BLUE APRON VARIANT", fill="#5d5d5d", font=font(16, True))
        else:
            image = Image.open(path).convert("RGBA")
            image.thumbnail((x2 - x1 - 40, y2 - y1 - 80))
            ix = x1 + (x2 - x1 - image.width) // 2
            iy = y1 + 64 + (y2 - y1 - 80 - image.height) // 2
            sheet.paste(image, (ix, iy), image)

    sheet.save(ROOT / "presentation-sheet.png")


def create_before_after():
    before = Image.open(ASSETS / "hero.png").convert("RGB")
    after = Image.open(ASSETS / "hero-transparent.png").convert("RGBA")
    canvas = Image.new("RGB", (1400, 720), "#f6faf0")
    draw = ImageDraw.Draw(canvas)
    draw.text((50, 28), "Hero cleanup / colour correction workflow", fill="#1d6c35", font=font(34, True))
    before.thumbnail((580, 580))
    after.thumbnail((580, 580))
    canvas.paste(before, (70, 100))
    canvas.paste(after, (750, 100), after)
    draw.text((70, 650), "BEFORE — source render", fill="#5d5d5d", font=font(22, True))
    draw.text((750, 650), "AFTER — cleaned transparent export", fill="#5d5d5d", font=font(22, True))
    canvas.save(ROOT / "hero-before-after.png")


create_transparent_hero()
create_presentation_sheet()
create_before_after()
print("Created transparent hero, presentation sheet, and before/after sheet.")
