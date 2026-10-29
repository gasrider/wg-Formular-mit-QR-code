"""Erzeugt ein Bild zum Teilen per WhatsApp (QR-Code mit Überschrift und Link).

Aufruf:  python3 tools/make_share_image.py
Benötigt: pip install "qrcode[pil]"
"""
import qrcode
from PIL import Image, ImageDraw, ImageFont

URL = "https://gasrider.github.io/wg-Formular-mit-QR-code/mitglieder/"
FONTS = "/usr/share/fonts/truetype/liberation/"
BLAU, GRAU = "#003366", "#444444"
W, H = 1080, 1350

img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
fett = lambda size: ImageFont.truetype(FONTS + "LiberationSans-Bold.ttf", size)
normal = lambda size: ImageFont.truetype(FONTS + "LiberationSans-Regular.ttf", size)


def zentriert(y, text, font, farbe):
    breite = draw.textlength(text, font=font)
    draw.text(((W - breite) / 2, y), text, font=font, fill=farbe)


draw.rectangle([0, 0, W, 24], fill="#4169e1")
zentriert(80, "Wassergenossenschaft Rabenschwand", normal(44), GRAU)
zentriert(150, "Zählerstand & Kontaktdaten", fett(64), BLAU)
zentriert(235, "online melden", fett(64), BLAU)

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=2)
qr.add_data(URL)
qr.make(fit=True)
code = qr.make_image(fill_color="black", back_color="white").get_image().convert("RGB")
code = code.resize((640, 640), Image.NEAREST)
img.paste(code, ((W - 640) // 2, 360))

zentriert(1030, "QR-Code scannen oder Link öffnen:", normal(40), GRAU)
zentriert(1090, URL.replace("https://", ""), fett(34), "#274fc1")
zentriert(1190, "Keine Anmeldung nötig · dauert ca. 1 Minute", normal(36), GRAU)

img.save("assets/qr_whatsapp.png")
print("Erzeugt: assets/qr_whatsapp.png")
