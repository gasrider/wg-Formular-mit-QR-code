<?php
// Empfänger der Formulardaten
$to   = "wg-rabenschwand@gmx.at";
$from = "noreply@wgrabenschwand.bplaced.net";

function antwort($titel, $text) {
    header("Content-Type: text/html; charset=UTF-8");
    echo "<!DOCTYPE html><html lang=\"de\"><head><meta charset=\"UTF-8\">"
       . "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
       . "<title>" . htmlspecialchars($titel) . "</title>"
       . "<style>body{font-family:Arial,sans-serif;max-width:640px;margin:0 auto;padding:24px;}"
       . "h1{color:#003366;font-size:1.6rem;}a{color:#4169e1;}</style></head><body>"
       . "<h1>" . htmlspecialchars($titel) . "</h1><p>" . htmlspecialchars($text) . "</p>"
       . "<p><a href=\"index.html\">Zurück zum Formular</a></p></body></html>";
    exit;
}

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    antwort("Ungültiger Zugriff", "Bitte verwenden Sie das Formular.");
}

// Spam-Schutz: Bots füllen das unsichtbare Feld aus
if (!empty($_POST["website"])) {
    antwort("Vielen Dank!", "Ihre Daten wurden erfolgreich übermittelt.");
}

// Zeilenumbrüche entfernen, damit keine zusätzlichen Mail-Header eingeschleust werden können
function feld($key) {
    return trim(str_replace(["\r", "\n"], " ", strip_tags($_POST[$key] ?? "")));
}

$name    = feld("name");
$adresse = feld("adresse");
$telefon = feld("telefon");
$email   = feld("email");
$kontakt = feld("kontakt");
$notfall = isset($_POST["notfall"]) ? "Ja" : "Nein";

if ($name === "" || $adresse === "" || $telefon === "" || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    antwort("Angaben unvollständig", "Bitte füllen Sie alle Felder aus und geben Sie eine gültige E-Mail-Adresse an.");
}

$subject = "=?UTF-8?B?" . base64_encode("WG Rabenschwand – Aktualisierte Mitgliederdaten") . "?=";

$message  = "Neue Mitgliederdaten:\n\n";
$message .= "Name:             $name\n";
$message .= "Adresse:          $adresse\n";
$message .= "Telefon:          $telefon\n";
$message .= "E-Mail:           $email\n";
$message .= "Kontaktweg:       $kontakt\n";
$message .= "Notfall-Freigabe: $notfall\n\n";
$message .= "Eingegangen am:   " . date("d.m.Y H:i") . "\n";

$headers  = "From: WG Rabenschwand <$from>\r\n";
$headers .= "Reply-To: $email\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "Content-Transfer-Encoding: 8bit\r\n";

if (mail($to, $subject, $message, $headers)) {
    antwort("Vielen Dank!", "Ihre Daten wurden erfolgreich übermittelt.");
} else {
    antwort("Fehler beim Senden", "Bitte versuchen Sie es später erneut oder schreiben Sie direkt an $to.");
}
