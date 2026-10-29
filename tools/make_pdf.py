"""Setzt den neuen QR-Code ins Brief-PDF und macht das Rückgabedatum ausfüllbar.

Aufruf:  python3 tools/make_pdf.py dokumente/Wasserzaehlerstand_WG_Rabenschwand_alt.pdf \
             assets/qr_mitglieder.png dokumente/Wasserzaehlerstand_WG_Rabenschwand.pdf
Benötigt: pip install pymupdf
"""
import sys, pymupdf
src, qr, out = sys.argv[1:]
d = pymupdf.open(src); p = d[0]
p.replace_image(42, filename=qr)
p.add_redact_annot(pymupdf.Rect(91.0, 354.6, 140.4, 365.3), fill=False)
p.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)
w = pymupdf.Widget()
w.field_type = pymupdf.PDF_WIDGET_TYPE_TEXT
w.field_name = "Rueckgabedatum"
w.field_label = "Rückgabe bis spätestens (TT.MM.JJJJ)"
w.rect = pymupdf.Rect(88.6, 353.2, 143.4, 366.6)   # Text beginnt (mit 2 pt Innenabstand) genau an der alten Stelle
w.text_align = pymupdf.TEXT_ALIGN_LEFT
w.field_value = "01.10.2025"
w.text_font = "Helv"; w.text_fontsize = 10; w.text_color = (0, 0, 0)
w.border_width = 0; w.border_color = None; w.fill_color = None
w.text_maxlen = 10
p.add_widget(w)
# Erscheinungsbild neu erzeugen (sonst fehlt beim Startwert der Innenabstand)
[f for f in p.widgets() if f.field_name == "Rueckgabedatum"][0].update()
d.set_metadata({**d.metadata, "title": "Wasserzählerstand WG Rabenschwand"})
d.save(out, garbage=3, deflate=True)
