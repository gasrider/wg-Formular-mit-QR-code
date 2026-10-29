"""Erzeugt die QR-Codes zu den Formularen (PNG + SVG, ohne Logo).

Aufruf:  python3 tools/make_qr.py
Benötigt: pip install "qrcode[pil]"
"""
import qrcode
import qrcode.image.svg

BASIS = "https://gasrider.github.io/wg-Formular-mit-QR-code/"
FORMULARE = {"mitglieder": BASIS + "mitglieder/", "kontakt": BASIS + "kontakt/"}


def build(url, box_size=10):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=box_size, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    return qr


for name, url in FORMULARE.items():
    # Web-/PDF-Auflösung, Druckqualität und Vektor (beliebig skalierbar)
    build(url).make_image(fill_color="black", back_color="white").save(f"assets/qr_{name}.png")
    build(url, box_size=30).make_image(fill_color="black", back_color="white").save(f"assets/qr_{name}_druck.png")
    build(url).make_image(image_factory=qrcode.image.svg.SvgPathFillImage).save(f"assets/qr_{name}.svg")
    print("QR-Code erzeugt für:", url)
