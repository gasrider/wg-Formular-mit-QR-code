# WG Rabenschwand – Mitglieder-Formular mit QR-Code

Mitglieder scannen den QR-Code, landen auf dem Online-Formular und die Daten
werden per E-Mail an `wg-rabenschwand@gmx.at` geschickt.

Das Formular wird kostenlos über **GitHub Pages** veröffentlicht (kein bplaced,
kein PHP nötig). Den Mailversand übernimmt der kostenlose Dienst **FormSubmit**.

**Adresse des Formulars / Ziel des QR-Codes:**
https://gasrider.github.io/wg-Formular-mit-QR-code/mitglieder/

## Dateien

| Datei | Zweck |
|---|---|
| `mitglieder/index.html` | Das Formular |
| `mitglieder/danke.html` | Bestätigungsseite nach dem Absenden |
| `index.html` | Leitet von der Startseite zum Formular weiter |
| `assets/qr_mitglieder.png` | QR-Code, Web-Auflösung (für PDF/Brief) |
| `assets/qr_mitglieder_druck.png` | QR-Code, Druckqualität |
| `assets/qr_mitglieder.svg` | QR-Code als Vektor (beliebig skalierbar) |
| `tools/make_qr.py` | Erzeugt die QR-Codes neu (z. B. für eine andere Adresse) |

## Einmalige Einrichtung

### 1. GitHub Pages einschalten

1. https://github.com/gasrider/wg-Formular-mit-QR-code/settings/pages öffnen
2. Bei **Source**: „Deploy from a branch“
3. Bei **Branch**: `claude/gracious-hypatia-pa302w` und Ordner `/ (root)` wählen → **Save**
4. 1–2 Minuten warten, dann die Formular-Adresse oben im Handy-Browser öffnen.

### 2. FormSubmit freischalten (nur beim allerersten Mal)

1. Das Formular einmal selbst mit Testdaten ausfüllen und absenden.
2. FormSubmit schickt eine Mail an `wg-rabenschwand@gmx.at` (evtl. im Spam-Ordner)
   → den Link **„Activate Form“** anklicken.
3. Ab jetzt kommt jeder Eintrag als Mail mit einer übersichtlichen Tabelle an.

Tipp: In der Aktivierungsmail steht eine zufällige Zeichenfolge. Wenn man diese in
`mitglieder/index.html` statt der E-Mail-Adresse in `action="https://formsubmit.co/…"`
einträgt, ist die Mailadresse im Quelltext der Seite nicht mehr sichtbar.

### 3. Test mit dem Handy

QR-Code (`assets/qr_mitglieder.png`) mit der Handykamera scannen → das Formular
muss erscheinen → absenden → „Vielen Dank!“ und die Mail kommt an.

## Datenschutz

Die Eingaben werden über FormSubmit (formsubmit.co) weitergeleitet. FormSubmit
speichert laut eigenen Angaben keine Formulardaten dauerhaft, ist aber ein externer
Dienst – das sollte im Datenschutzhinweis der Genossenschaft erwähnt werden.

## QR-Code für eine andere Adresse erzeugen

```bash
pip install "qrcode[pil]"
python3 tools/make_qr.py https://neue-adresse.example/mitglieder/
```
