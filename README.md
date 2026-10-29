# WG Rabenschwand – Mitglieder-Formular mit QR-Code

Mitglieder scannen den QR-Code, landen auf dem Online-Formular, tragen ihre Daten
und den aktuellen Wasserzählerstand ein. Alles wird per E-Mail an
`wg-rabenschwand@gmx.at` geschickt.

Das Formular wird kostenlos über **GitHub Pages** veröffentlicht (kein bplaced,
kein PHP nötig). Den Mailversand übernimmt der kostenlose Dienst **Web3Forms** (bis 250 Einträge/Monat).
Fällt der Dienst einmal aus, bietet das Formular automatisch an, die Daten per
E-Mail zu schicken (das Mailprogramm öffnet sich mit allen Angaben ausgefüllt).

**Zwei Formulare:**

| Formular | Adresse | Inhalt |
|---|---|---|
| Zählerstand & Kontaktdaten | https://gasrider.github.io/wg-Formular-mit-QR-code/mitglieder/ | Kontaktdaten + Wasserzählerstand (QR-Code im Brief) |
| Nur Kontaktdaten | https://gasrider.github.io/wg-Formular-mit-QR-code/kontakt/ | Kontaktdaten ohne Zählerstand |

Die E-Mail-Adresse ist freiwillig – Mitglieder ohne E-Mail senden nur mit Telefonnummer ab.

## Per WhatsApp verschicken

Einfach den **Link** (nicht nur ein Bild) in WhatsApp schicken. WhatsApp zeigt dann
automatisch ein großes Vorschaubild mit QR-Code und „Hier tippen“ – ein Tipp darauf
öffnet direkt das Formular. Vorlage zum Kopieren (Nur-Kontaktdaten-Formular):

```
Liebe Mitglieder der Wassergenossenschaft Rabenschwand,

bitte helft uns, unsere Kontaktliste aktuell zu halten (wichtig für Notfälle, z. B. Wasserrohrbruch).
Einfach auf den Link tippen, Formular ausfüllen und absenden – dauert ca. 1 Minute, keine Anmeldung nötig.
Wer keine E-Mail-Adresse hat, lässt das Feld einfach leer.

https://gasrider.github.io/wg-Formular-mit-QR-code/kontakt/

Danke!
Eure WG Rabenschwand
```

Für Zählerstände den Link `…/mitglieder/` verwenden.

## Dateien

| Datei | Zweck |
|---|---|
| `mitglieder/index.html` | Das Formular |
| `mitglieder/danke.html` | Bestätigungsseite nach dem Absenden |
| `kontakt/index.html`, `kontakt/danke.html` | Zweites Formular: nur Kontaktdaten |
| `index.html` | Leitet von der Startseite zum Formular weiter |
| `assets/qr_<formular>.png` | QR-Code, Web-Auflösung (für PDF/Brief) |
| `assets/qr_<formular>_druck.png` | QR-Code, Druckqualität |
| `assets/qr_<formular>.svg` | QR-Code als Vektor (beliebig skalierbar) |
| `dokumente/Wasserzaehlerstand_WG_Rabenschwand.pdf` | Brief an die Mitglieder (ausfüllbar, mit neuem QR-Code) |
| `dokumente/Wasserzaehlerstand_WG_Rabenschwand_alt.pdf` | Ursprünglicher Brief (QR-Code zeigt noch auf bplaced) |
| `tools/make_pdf.py` | Setzt den QR-Code ins Brief-PDF und macht das Rückgabedatum ausfüllbar |
| `assets/qr_whatsapp_<formular>.png` | Hochformat-Bild zum Verschicken (QR-Code, Überschrift, Link) |
| `assets/og_<formular>.png` | Vorschaubild, das WhatsApp beim Teilen des Links anzeigt |
| `tools/make_share_image.py` | Erzeugt WhatsApp- und Vorschaubilder neu |
| `tools/make_qr.py` | Erzeugt die QR-Codes neu (z. B. für eine andere Adresse) |

## Einmalige Einrichtung

### 1. GitHub Pages einschalten

1. https://github.com/gasrider/wg-Formular-mit-QR-code/settings/pages öffnen
2. Bei **Source**: „Deploy from a branch“
3. Bei **Branch**: `claude/gracious-hypatia-pa302w` und Ordner `/ (root)` wählen → **Save**
4. 1–2 Minuten warten, dann die Formular-Adresse oben im Handy-Browser öffnen.

### 2. Web3Forms-Zugangsschlüssel holen (nur einmal)

1. https://web3forms.com öffnen, `wg-rabenschwand@gmx.at` eintragen und auf
   **„Create Access Key“** klicken.
2. Der Schlüssel (z. B. `a1b2c3d4-...`) kommt per Mail an diese Adresse.
3. In `mitglieder/index.html` den Text `HIER-ACCESS-KEY-EINTRAGEN` durch den
   Schlüssel ersetzen. Der Schlüssel darf öffentlich sichtbar sein – er erlaubt
   nur, Mails an `wg-rabenschwand@gmx.at` zu schicken.

### 3. Test mit dem Handy

QR-Code (`assets/qr_mitglieder.png`) mit der Handykamera scannen → das Formular
muss erscheinen → absenden → „Vielen Dank!“ und die Mail kommt an.

## Brief (PDF) anpassen

`dokumente/Wasserzaehlerstand_WG_Rabenschwand.pdf` in Adobe Acrobat Reader öffnen.
Ausfüllbar sind die drei Adresszeilen, das **Rückgabedatum** („… bis spätestens
01.10.2025“ – einfach anklicken und überschreiben, Format TT.MM.JJJJ) und die
Felder der Antwortkarte. Danach speichern bzw. drucken.

## Datenschutz

Die Eingaben werden über Web3Forms (web3forms.com) per Mail weitergeleitet. Das ist
ein externer Dienst – das sollte im Datenschutzhinweis der Genossenschaft erwähnt werden.

## QR-Code für eine andere Adresse erzeugen

```bash
pip install "qrcode[pil]"
python3 tools/make_qr.py            # Adressen stehen oben im Skript
python3 tools/make_share_image.py
```
