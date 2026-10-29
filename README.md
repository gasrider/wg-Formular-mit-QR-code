# WG Rabenschwand – Mitglieder-Formular mit QR-Code

Mitglieder scannen den QR-Code, landen auf dem Online-Formular und die Daten
werden per E-Mail an `wg-rabenschwand@gmx.at` geschickt.

## Dateien

| Datei | Zweck |
|---|---|
| `mitglieder/index.html` | Das Formular |
| `mitglieder/send.php` | Verschickt die Eingaben per E-Mail |
| `assets/qr_mitglieder.png` | QR-Code, Web-Auflösung (für PDF/Brief) |
| `assets/qr_mitglieder_druck.png` | QR-Code, Druckqualität |
| `assets/qr_mitglieder.svg` | QR-Code als Vektor (beliebig skalierbar) |
| `tools/make_qr.py` | Erzeugt die QR-Codes neu (z. B. für eine andere Adresse) |

Der QR-Code zeigt auf: **http://wgrabenschwand.bplaced.net/mitglieder/index.html**

## Warum der alte QR-Code „nicht funktioniert“ hat

Unter der Adresse oben liefert bplaced derzeit eine **„Fehler 404 – Seite nicht
auffindbar“**-Seite (Stand 29.10.2026). Der QR-Code kann noch so korrekt sein –
solange `mitglieder/index.html` nicht auf dem Server liegt, landet man auf einer
Fehlerseite. Daher zuerst die Dateien hochladen (siehe unten) und im Browser
prüfen, ob das Formular erscheint.

## Hochladen (FileZilla)

1. Bei bplaced einloggen und prüfen, ob der Account `wgrabenschwand` noch aktiv ist
   (inaktive Gratis-Accounts werden von bplaced gesperrt/gelöscht).
2. Mit FileZilla verbinden und im Webroot (`/www/` bzw. `/`) anlegen:
   - Ordner `mitglieder` → `index.html` und `send.php` hochladen
   - Ordner `assets` → die QR-Dateien hochladen (optional)
3. Rechte: Ordner `0755`, Dateien `0644`.
4. Im Handy-Browser öffnen: http://wgrabenschwand.bplaced.net/mitglieder/index.html
5. Testeintrag absenden und prüfen, ob die Mail ankommt (auch im Spam-Ordner).

## Falls keine E-Mail ankommt

Manche Gratis-Pakete (z. B. bplaced „Freestyle“) erlauben den Mailversand per PHP
nicht. Dann in `mitglieder/index.html` die Formularzeile ändern auf:

```html
<form action="https://formsubmit.co/wg-rabenschwand@gmx.at" method="post">
```

Beim ersten Absenden schickt FormSubmit eine Bestätigungsmail an
`wg-rabenschwand@gmx.at` – einmal bestätigen, danach kommen alle Einträge per Mail.
`send.php` wird dann nicht mehr benötigt.

## QR-Code für eine andere Adresse erzeugen

```bash
pip install "qrcode[pil]"
python3 tools/make_qr.py https://neue-adresse.example/mitglieder/index.html
```
