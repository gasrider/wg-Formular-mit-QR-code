"""Erzeugt die Bilder zum Teilen per WhatsApp:

- assets/qr_whatsapp_<formular>.png  Hochformat-Bild (QR-Code, Überschrift, Link) zum Verschicken
- assets/og_<formular>.png           Vorschaubild, das WhatsApp beim Teilen des Links anzeigt

Aufruf:  python3 tools/make_share_image.py
Benötigt: pip install "qrcode[pil]"
"""
import qrcode
from PIL import Image, ImageDraw, ImageFont

BASIS = "https://gasrider.github.io/wg-Formular-mit-QR-code/"
FONTS = "/usr/share/fonts/truetype/liberation/"
BLAU, GRAU, LINK = "#003366", "#444444", "#274fc1"

FORMULARE = {
    "mitglieder": ("Zählerstand & Kontaktdaten", "online melden"),
    "kontakt": ("Kontaktdaten", "aktualisieren"),
}


def fett(size):
    return ImageFont.truetype(FONTS + "LiberationSans-Bold.ttf", size)


def normal(size):
    return ImageFont.truetype(FONTS + "LiberationSans-Regular.ttf", size)


def qr_bild(url, groesse):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white").get_image().convert("RGB").resize(
        (groesse, groesse), Image.NEAREST)


def hochformat(url, titel, datei):
    W, H = 1080, 1350
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    def zentriert(y, text, font, farbe):
        draw.text(((W - draw.textlength(text, font=font)) / 2, y), text, font=font, fill=farbe)

    draw.rectangle([0, 0, W, 24], fill="#4169e1")
    zentriert(80, "Wassergenossenschaft Rabenschwand", normal(44), GRAU)
    zentriert(150, titel[0], fett(64), BLAU)
    zentriert(235, titel[1], fett(64), BLAU)
    img.paste(qr_bild(url, 640), ((W - 640) // 2, 360))
    zentriert(1030, "QR-Code scannen oder Link öffnen:", normal(40), GRAU)
    zentriert(1090, url.replace("https://", ""), fett(34), LINK)
    zentriert(1190, "Keine Anmeldung nötig · dauert ca. 1 Minute", normal(36), GRAU)
    img.save(datei)


def vorschau(url, titel, datei):
    # 1200 x 630 – dieses Format zeigt WhatsApp als große Vorschau über dem Link an
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 20], fill="#4169e1")
    img.paste(qr_bild(url, 500), (50, 85))
    x = 600
    draw.text((x, 95), "WG Rabenschwand", font=normal(40), fill=GRAU)
    groesse = 52
    while max(draw.textlength(t, font=fett(groesse)) for t in titel) > W - x - 50:
        groesse -= 2
    draw.text((x, 160), titel[0], font=fett(groesse), fill=BLAU)
    draw.text((x, 225), titel[1], font=fett(groesse), fill=BLAU)
    draw.text((x, 340), "► Hier tippen", font=fett(44), fill=LINK)
    draw.text((x, 400), "oder QR-Code scannen", font=normal(40), fill=GRAU)
    draw.text((x, 490), "Keine Anmeldung nötig", font=normal(34), fill=GRAU)
    draw.text((x, 535), "dauert ca. 1 Minute", font=normal(34), fill=GRAU)
    img.save(datei, optimize=True)


for name, titel in FORMULARE.items():
    url = BASIS + name + "/"
    hochformat(url, titel, f"assets/qr_whatsapp_{name}.png")
    vorschau(url, titel, f"assets/og_{name}.png")
    print("Bilder erzeugt für:", url)
