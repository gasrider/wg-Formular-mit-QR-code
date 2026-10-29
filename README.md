# WG Rabenschwand – Mitglieder-Formular mit QR-Code

Mitglieder scannen den QR-Code, landen auf dem Online-Formular, tragen ihre Daten
und den aktuellen Wasserzählerstand ein. Alles wird per E-Mail an
`wg-rabenschwand@gmx.at` geschickt.

Das Formular wird kostenlos über **GitHub Pages** veröffentlicht (kein bplaced,
kein PHP nötig). Den Mailversand übernimmt der kostenlose Dienst **Web3Forms** (bis 250 Einträge/Monat).
Fällt der Dienst einmal aus, bietet das Formular automatisch an, die Daten per
E-Mail zu schicken (das Mailprogramm öffnet sich mit allen Angaben ausgefüllt).

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

## Datenschutz

Die Eingaben werden über Web3Forms (web3forms.com) per Mail weitergeleitet. Das ist
ein externer Dienst – das sollte im Datenschutzhinweis der Genossenschaft erwähnt werden.

## QR-Code für eine andere Adresse erzeugen

```bash
pip install "qrcode[pil]"
python3 tools/make_qr.py https://neue-adresse.example/mitglieder/
```
