"""Erzeugt den QR-Code zum Mitglieder-Formular (PNG + SVG, ohne Logo).

Aufruf:  python3 tools/make_qr.py [URL]
Benötigt: pip install "qrcode[pil]"
"""
import sys

import qrcode
import qrcode.image.svg

URL = sys.argv[1] if len(sys.argv) > 1 else "http://wgrabenschwand.bplaced.net/mitglieder/index.html"


def build():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
    qr.add_data(URL)
    qr.make(fit=True)
    return qr


# Web-/PDF-Auflösung
build().make_image(fill_color="black", back_color="white").save("assets/qr_mitglieder.png")

# Druckqualität (ca. 3 cm bei 300 dpi und größer)
qr = build()
qr.box_size = 30
qr.make_image(fill_color="black", back_color="white").save("assets/qr_mitglieder_druck.png")

# Vektor (beliebig skalierbar, ideal für Word/PDF)
build().make_image(image_factory=qrcode.image.svg.SvgPathFillImage).save("assets/qr_mitglieder.svg")

print("QR-Code erzeugt für:", URL)
