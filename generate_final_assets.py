from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parent
out_dir = root / 'assets'
out_dir.mkdir(exist_ok=True)


def draw_hero(path):
    img = Image.new('RGBA', (800, 800), '#edf9ff')
    d = ImageDraw.Draw(img)
    d.ellipse((120, 620, 680, 740), fill=(220, 240, 220, 255))
    d.rounded_rectangle((120, 170, 550, 500), radius=18, fill=(130, 210, 120, 255))
    d.polygon([(170, 230), (105, 170), (205, 150), (275, 210)], fill=(120, 192, 95, 255))
    d.polygon([(350, 220), (490, 170), (515, 220), (390, 260)], fill=(120, 192, 95, 255))
    d.ellipse((260, 110, 420, 270), fill=(247, 214, 181, 255))
    d.ellipse((245, 90, 430, 175), fill=(58, 101, 64, 255))
    d.ellipse((300, 160, 315, 175), fill=(35, 35, 35, 255))
    d.ellipse((360, 160, 375, 175), fill=(35, 35, 35, 255))
    d.arc((302, 190, 378, 225), start=200, end=340, fill=(214, 120, 120, 255), width=8)
    d.rounded_rectangle((235, 260, 445, 430), radius=30, fill=(245, 215, 120, 255))
    d.rounded_rectangle((165, 270, 230, 430), radius=18, fill=(247, 214, 181, 255))
    d.rounded_rectangle((450, 270, 515, 430), radius=18, fill=(247, 214, 181, 255))
    d.rounded_rectangle((255, 420, 325, 560), radius=20, fill=(255, 198, 86, 255))
    d.rounded_rectangle((355, 420, 425, 560), radius=20, fill=(255, 198, 86, 255))
    d.rounded_rectangle((242, 550, 340, 610), radius=16, fill=(141, 94, 57, 255))
    d.rounded_rectangle((338, 550, 438, 610), radius=16, fill=(141, 94, 57, 255))
    for x in [160, 210, 450, 490]:
        d.polygon([(x, 150), (x - 28, 90), (x + 24, 90)], fill=(80, 190, 82, 255))
    img.save(path)


def draw_gameplay(path):
    img = Image.new('RGBA', (1200, 800), '#dff8ff')
    d = ImageDraw.Draw(img)
    d.ellipse((930, 70, 1055, 200), fill=(255, 232, 138, 255))
    for c in [(120, 110, 170, 150), (260, 140, 360, 185), (820, 130, 930, 175)]:
        d.ellipse(c, fill=(255, 255, 255, 180))
    d.rectangle((0, 520, 1200, 800), fill=(116, 196, 110, 255))
    d.rounded_rectangle((60, 70, 1140, 710), radius=28, fill=(255, 255, 255, 120))
    d.rounded_rectangle((90, 96, 350, 218), radius=18, fill=(255, 250, 244, 220))
    d.rounded_rectangle((105, 120, 220, 200), radius=12, fill=(247, 214, 168, 255))
    d.rounded_rectangle((228, 137, 312, 156), radius=5, fill=(205, 175, 232, 255))
    d.rounded_rectangle((228, 165, 322, 184), radius=5, fill=(195, 240, 166, 255))
    d.rounded_rectangle((228, 194, 305, 213), radius=5, fill=(154, 215, 255, 255))

    x, y = 470, 250
    d.ellipse((x + 85, y + 80, x + 260, y + 250), fill=(247, 214, 181, 255))
    d.ellipse((x + 95, y + 40, x + 250, y + 150), fill=(58, 101, 64, 255))
    d.ellipse((x + 124, y + 110, x + 138, y + 124), fill=(30, 30, 30, 255))
    d.ellipse((x + 160, y + 110, x + 174, y + 124), fill=(30, 30, 30, 255))
    d.arc((x + 128, y + 138, x + 170, y + 175), start=200, end=340, fill=(211, 134, 122, 255), width=8)
    d.rounded_rectangle((x + 105, y + 220, x + 245, y + 370), radius=30, fill=(245, 215, 120, 255))
    d.rounded_rectangle((x + 80, y + 230, x + 110, y + 440), radius=15, fill=(247, 214, 181, 255))
    d.rounded_rectangle((x + 240, y + 230, x + 270, y + 440), radius=15, fill=(247, 214, 181, 255))
    d.rounded_rectangle((x + 105, y + 370, x + 170, y + 470), radius=18, fill=(255, 198, 86, 255))
    d.rounded_rectangle((x + 180, y + 370, x + 245, y + 470), radius=18, fill=(255, 198, 86, 255))
    for px, py in [(590, 255), (760, 255), (960, 255), (1100, 270)]:
        d.rectangle((px, py, px + 120, py + 80), fill=(112, 176, 120, 255))
    d.rounded_rectangle((900, 330, 1060, 560), radius=16, fill=(255, 249, 238, 220))
    d.rounded_rectangle((915, 350, 1045, 430), radius=16, fill=(215, 239, 221, 255))
    d.ellipse((948, 385, 1012, 450), fill=(255, 215, 105, 255))
    d.rectangle((920, 455, 1042, 474), fill=(154, 215, 255, 255))
    d.rectangle((920, 485, 1014, 504), fill=(244, 199, 209, 255))
    d.rectangle((920, 515, 1002, 534), fill=(194, 232, 167, 255))
    img.save(path)


def draw_background(path):
    img = Image.new('RGBA', (1400, 800), '#dff9ff')
    d = ImageDraw.Draw(img)
    d.ellipse((1150, 70, 1290, 210), fill=(255, 233, 154, 255))
    for x, y, w, h in [(130, 120, 200, 60), (300, 140, 260, 70), (980, 150, 230, 70)]:
        d.ellipse((x, y, x + w, y + h), fill=(255, 255, 255, 200))
        d.ellipse((x + 40, y - 18, x + w + 30, y + 60), fill=(255, 255, 255, 200))
    d.polygon([(0, 520), (180, 420), (420, 520), (580, 440), (830, 520), (1030, 420), (1400, 520), (1400, 800), (0, 800)], fill=(190, 230, 136, 255))
    d.polygon([(0, 640), (180, 560), (420, 620), (760, 700), (1000, 630), (1400, 520), (1400, 800), (0, 800)], fill=(120, 185, 110, 255))
    for x in [160, 420, 640, 930, 1200]:
        d.rectangle((x, 620, x + 80, 710), fill=(141, 94, 57, 255))
        d.rectangle((x - 20, 560, x + 100, 620), fill=(120, 185, 110, 255))
        for i in range(5):
            d.line((x + 10 + i * 15, 610, x + 10 + i * 15, 560), fill=(93, 145, 73, 255), width=6)
    for x in [150, 760]:
        d.rectangle((x, 350, x + 190, 530), fill=(252, 232, 210, 255))
        d.polygon([(x, 350), (x + 95, 280), (x + 190, 350)], fill=(122, 185, 84, 255))
        for bx in [x + 40, x + 120]:
            d.rectangle((bx, 430, bx + 30, 500), fill=(140, 207, 255, 255))
    img.save(path)


def draw_items(path):
    img = Image.new('RGBA', (1200, 500), '#f9faf1')
    d = ImageDraw.Draw(img)
    for x, y, t in [(90, 0, 'carrot'), (350, 0, 'tomato'), (610, 0, 'hammer'), (870, 0, 'water')]:
        d.ellipse((x, y, x + 220, y + 220), fill=(234, 247, 234, 255))
        if t == 'carrot':
            d.polygon([(x + 110, y + 30), (x + 150, y + 130), (x + 110, y + 200), (x + 70, y + 130)], fill=(255, 143, 79, 255))
            d.line((x + 110, y + 70, x + 110, y + 180), fill=(80, 180, 90, 255), width=10)
            d.line((x + 75, y + 100, x + 145, y + 110), fill=(80, 180, 90, 255), width=10)
        elif t == 'tomato':
            d.ellipse((x + 60, y + 40, x + 160, y + 160), fill=(239, 90, 81, 255))
            d.line((x + 110, y + 20, x + 110, y + 170), fill=(80, 180, 90, 255), width=8)
        elif t == 'hammer':
            d.rectangle((x + 80, y + 80, x + 140, y + 170), fill=(199, 165, 74, 255))
            d.rectangle((x + 120, y + 70, x + 160, y + 150), fill=(150, 120, 50, 255))
            d.line((x + 100, y + 170, x + 110, y + 250), fill=(90, 80, 70, 255), width=12)
        elif t == 'water':
            d.rounded_rectangle((x + 75, y + 60, x + 145, y + 200), radius=18, fill=(110, 200, 255, 255))
            d.rectangle((x + 95, y + 25, x + 125, y + 60), fill=(214, 245, 255, 255))
    img.save(path)


def main():
    draw_hero(out_dir / 'hero.png')
    draw_gameplay(out_dir / 'gameplay.png')
    draw_background(out_dir / 'background.png')
    draw_items(out_dir / 'items.png')
    print('Created assets:')
    for p in sorted(out_dir.iterdir()):
        print(' -', p.name)


main()
