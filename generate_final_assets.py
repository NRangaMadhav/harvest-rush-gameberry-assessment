from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)


def hero_art():
    image = Image.new("RGBA", (800, 800), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    draw.ellipse((155, 686, 645, 750), fill=(39, 104, 57, 70))
    draw.rounded_rectangle((240, 280, 560, 530), radius=75, fill="#f7c94f", outline="#d99038", width=8)
    draw.rounded_rectangle((285, 300, 515, 480), radius=52, fill="#48a45b")
    draw.polygon([(300, 336), (380, 380), (500, 330), (468, 450), (320, 450)], fill="#357e48")

    draw.rounded_rectangle((165, 310, 242, 500), radius=34, fill="#f3caa5", outline="#d99678", width=5)
    draw.rounded_rectangle((558, 310, 635, 500), radius=34, fill="#f3caa5", outline="#d99678", width=5)
    draw.rounded_rectangle((276, 492, 350, 650), radius=28, fill="#f4ad3d", outline="#d88732", width=5)
    draw.rounded_rectangle((450, 492, 524, 650), radius=28, fill="#f4ad3d", outline="#d88732", width=5)
    draw.ellipse((250, 635, 375, 685), fill="#7a4d31")
    draw.ellipse((425, 635, 550, 685), fill="#7a4d31")

    draw.ellipse((260, 112, 540, 390), fill="#f3caa5", outline="#d99678", width=7)
    draw.pieslice((247, 74, 553, 285), 180, 360, fill="#315c3b", outline="#23492e", width=7)
    draw.ellipse((208, 97, 592, 160), fill="#f6ba4c", outline="#ce8332", width=7)
    draw.polygon([(235, 108), (186, 34), (250, 64)], fill="#5ab56a", outline="#357e48")
    draw.polygon([(560, 108), (614, 41), (566, 70)], fill="#5ab56a", outline="#357e48")
    draw.ellipse((323, 211, 349, 240), fill="#272727")
    draw.ellipse((451, 211, 477, 240), fill="#272727")
    draw.ellipse((329, 216, 337, 224), fill="#ffffff")
    draw.ellipse((457, 216, 465, 224), fill="#ffffff")
    draw.arc((350, 247, 450, 330), 20, 160, fill="#c56d6d", width=9)
    draw.ellipse((284, 280, 320, 304), fill="#ef8b82")
    draw.ellipse((480, 280, 516, 304), fill="#ef8b82")
    draw.ellipse((120, 450, 172, 502), fill="#ffd971", outline="#d99038", width=5)
    draw.ellipse((628, 450, 680, 502), fill="#ffd971", outline="#d99038", width=5)
    return image


def draw_hero(path):
    image = Image.new("RGBA", (800, 800), "#edf9ff")
    art = hero_art()
    image.alpha_composite(art)
    image.save(path)


def draw_hero_variant(path):
    image = hero_art()
    draw = ImageDraw.Draw(image)
    # Alternate harvest pose: raised watering can and blue apron accent.
    draw.rounded_rectangle((544, 270, 690, 315), radius=18, fill="#f3caa5", outline="#d99678", width=6)
    draw.rounded_rectangle((625, 210, 700, 282), radius=16, fill="#69c8ff", outline="#438fb7", width=6)
    draw.rectangle((644, 184, 684, 218), fill="#d5f5ff", outline="#438fb7", width=5)
    draw.line((633, 215, 600, 170), fill="#438fb7", width=9)
    draw.rounded_rectangle((290, 312, 510, 470), radius=48, fill="#4d9dc0")
    draw.rounded_rectangle((320, 330, 480, 455), radius=36, fill="#2e6f8c")
    image.save(path)


def draw_gameplay(path):
    image = Image.new("RGBA", (1200, 800), "#cfefff")
    draw = ImageDraw.Draw(image)
    draw.ellipse((990, 44, 1115, 169), fill="#ffe28a")
    for x, y, w, h in [(90, 112, 170, 48), (300, 146, 210, 55), (860, 120, 230, 54)]:
        draw.ellipse((x, y, x + w, y + h), fill=(255, 255, 255, 190))
        draw.ellipse((x + 42, y - 18, x + w - 20, y + h + 18), fill=(255, 255, 255, 190))
    draw.polygon([(0, 480), (170, 380), (390, 475), (620, 390), (850, 475), (1060, 380), (1200, 450), (1200, 800), (0, 800)], fill="#b9df83")
    draw.rectangle((0, 535, 1200, 800), fill="#69b867")

    draw.rounded_rectangle((48, 42, 1152, 758), radius=34, fill=(255, 255, 255, 66), outline="#ffffff", width=4)
    draw.rounded_rectangle((78, 75, 340, 235), radius=24, fill="#fff9ee", outline="#ead5b3", width=4)
    draw.text((102, 92), "HARVEST RUN", fill="#1d6c35")
    draw.ellipse((104, 139, 191, 226), fill="#ffd56e")
    draw.rectangle((217, 137, 304, 155), fill="#e0b0df")
    draw.rectangle((217, 174, 320, 192), fill="#bfe69a")
    draw.rectangle((217, 211, 290, 229), fill="#9ad7ff")

    hero = hero_art()
    hero.thumbnail((340, 470))
    image.alpha_composite(hero, (435, 188))
    for px, py in [(710, 315), (875, 350), (1030, 292)]:
        draw.rounded_rectangle((px, py, px + 120, py + 75), radius=18, fill="#8b5a35")
        draw.ellipse((px + 22, py - 20, px + 55, py + 20), fill="#6eb35d")
        draw.ellipse((px + 66, py - 20, px + 99, py + 20), fill="#6eb35d")

    draw.rounded_rectangle((875, 495, 1080, 680), radius=22, fill="#fff9ee", outline="#ead5b3", width=4)
    draw.text((900, 518), "MISSION", fill="#b21a5d")
    draw.text((900, 555), "Harvest Run", fill="#1d6c35")
    draw.text((900, 590), "Collect 10 items", fill="#5d5d5d")
    draw.rounded_rectangle((900, 625, 1048, 654), radius=12, fill="#f6c95a")
    draw.text((929, 631), "START", fill="#543a24")
    image.save(path)


def draw_background(path):
    image = Image.new("RGBA", (1400, 800), "#d9f5ff")
    draw = ImageDraw.Draw(image)
    draw.ellipse((1135, 62, 1285, 212), fill="#ffe49a")
    for x, y, w, h in [(100, 108, 180, 55), (340, 145, 235, 64), (930, 122, 250, 58)]:
        draw.ellipse((x, y, x + w, y + h), fill=(255, 255, 255, 185))
        draw.ellipse((x + 35, y - 20, x + w - 25, y + h + 20), fill=(255, 255, 255, 185))
    draw.polygon([(0, 475), (180, 350), (380, 470), (600, 340), (830, 460), (1050, 350), (1400, 470), (1400, 800), (0, 800)], fill="#c0e58d")
    draw.polygon([(0, 615), (210, 520), (440, 595), (740, 500), (980, 610), (1230, 510), (1400, 555), (1400, 800), (0, 800)], fill="#76be6a")
    draw.rectangle((0, 690, 1400, 800), fill="#559e5b")

    for x in [150, 920]:
        draw.rectangle((x, 300, x + 190, 500), fill="#fff1d7", outline="#d39158", width=6)
        draw.polygon([(x - 18, 305), (x + 95, 220), (x + 208, 305)], fill="#d56e54", outline="#9c4b43")
        for bx in [x + 35, x + 120]:
            draw.rounded_rectangle((bx, 380, bx + 40, 450), radius=5, fill="#9ad7ff", outline="#467b81", width=4)
        draw.rectangle((x + 80, 428, x + 112, 500), fill="#a06b3d")

    for x in [80, 330, 585, 820, 1080, 1280]:
        draw.ellipse((x, 594, x + 60, 660), fill="#6cc260")
        draw.ellipse((x + 40, 580, x + 108, 660), fill="#77cc68")
        draw.line((x + 42, 650, x + 42, 720), fill="#4d8f48", width=8)
        draw.line((x + 70, 650, x + 70, 720), fill="#4d8f48", width=8)
    image.save(path)


def draw_items(path):
    image = Image.new("RGBA", (1200, 500), "#f9faf1")
    draw = ImageDraw.Draw(image)
    for x, label, color in [(100, "CARROT", "#ff984c"), (360, "TOMATO", "#ef5a51"), (620, "HAMMER", "#c7a54a"), (880, "WATER", "#69c8ff")]:
        draw.ellipse((x, 48, x + 210, 258), fill="#e8f6e8", outline="#c9e6c3", width=5)
        if label == "CARROT":
            draw.polygon([(x + 105, 75), (x + 145, 170), (x + 105, 235), (x + 65, 170)], fill=color)
            draw.line((x + 105, 105, x + 105, 215), fill="#4ea85a", width=12)
            draw.line((x + 75, 130, x + 137, 145), fill="#4ea85a", width=10)
        elif label == "TOMATO":
            draw.ellipse((x + 62, 84, x + 164, 188), fill=color)
            draw.line((x + 113, 65, x + 113, 96), fill="#4ea85a", width=10)
        elif label == "HAMMER":
            draw.rectangle((x + 78, 110, x + 140, 190), fill="#c7a54a")
            draw.rectangle((x + 126, 90, x + 180, 140), fill="#8a5d2e")
            draw.line((x + 108, 185, x + 108, 245), fill="#8a5d2e", width=14)
        else:
            draw.rounded_rectangle((x + 70, 100, x + 155, 230), radius=18, fill=color)
            draw.rectangle((x + 96, 72, x + 130, 105), fill="#d5f5ff")
        draw.text((x + 46, 300), label, fill="#1d6c35")
    image.save(path)


def draw_transparent_collectible(path, kind):
    image = Image.new("RGBA", (360, 360), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((25, 275, 335, 335), fill=(39, 104, 57, 60))
    if kind == "carrot":
        draw.polygon([(180, 62), (246, 194), (180, 280), (114, 194)], fill="#ff984c", outline="#d96d35")
        draw.line((180, 96, 180, 242), fill="#4ea85a", width=16)
        draw.line((130, 132, 225, 153), fill="#4ea85a", width=13)
    elif kind == "tomato":
        draw.ellipse((82, 76, 278, 275), fill="#ef5a51", outline="#c74243", width=7)
        draw.polygon([(180, 68), (205, 101), (246, 90), (224, 130), (180, 112), (137, 130), (114, 90), (155, 101)], fill="#4ea85a")
    elif kind == "hammer":
        draw.rounded_rectangle((132, 95, 224, 220), radius=16, fill="#c7a54a", outline="#8a5d2e", width=7)
        draw.rounded_rectangle((198, 65, 292, 140), radius=18, fill="#8a5d2e", outline="#5d3d29", width=7)
        draw.line((178, 207, 178, 292), fill="#8a5d2e", width=18)
    else:
        draw.rounded_rectangle((112, 82, 248, 284), radius=30, fill="#69c8ff", outline="#438fb7", width=8)
        draw.rectangle((150, 38, 210, 88), fill="#d5f5ff", outline="#438fb7", width=7)
        draw.ellipse((150, 132, 185, 167), fill="#ffffff", outline="#438fb7", width=5)
    image.save(path)


def main():
    draw_hero(ASSETS / "hero.png")
    draw_hero_variant(ASSETS / "hero-variant.png")
    draw_gameplay(ASSETS / "gameplay.png")
    draw_background(ASSETS / "background.png")
    draw_items(ASSETS / "items.png")
    for kind in ["carrot", "tomato", "hammer", "watering-can"]:
        draw_transparent_collectible(ASSETS / f"{kind}.png", kind)
    print("Regenerated hero, gameplay lobby, farm background, and collectibles.")


main()
