"""
Verkleinert die Datei "DCA-Titelbild.jpg" in jedem Projektordner unter "projekte",
damit das Grid auf der Startseite schneller lädt.

Vorgehen:
- Original wird einmalig in einen Unterordner "original" verschoben (Sicherung)
- Aus dem Original wird eine verkleinerte/komprimierte Version erzeugt
  und unter dem ursprünglichen Namen (DCA-Titelbild.jpg) gespeichert

Benötigt: Pillow  ->  pip install Pillow
"""

import os
from pathlib import Path
from PIL import Image

# === Einstellungen ===
# "projekte"-Ordner liegt im selben Verzeichnis wie dieses Skript
PROJEKTE_ORDNER = Path(__file__).resolve().parent / "projekte"
DATEINAME = "DCA-Titelbild.jpg"
MAX_BREITE = 2000           # maximale Breite in Pixel (Höhe wird proportional angepasst)
JPEG_QUALITAET = 82          # Kompressionsqualität 1-100, 80-85 ist ein guter Kompromiss
BACKUP_ORDNER = "original"   # Unterordner, in dem die Originaldatei gesichert wird


def verkleinere_bild(pfad: Path):
    backup_dir = pfad.parent / BACKUP_ORDNER
    backup_dir.mkdir(exist_ok=True)
    backup_pfad = backup_dir / pfad.name

    # Original einmalig sichern
    if not backup_pfad.exists():
        pfad.rename(backup_pfad)

    quelle = backup_pfad

    with Image.open(quelle) as img:
        img = img.convert("RGB")
        breite, hoehe = img.size
        if breite > MAX_BREITE:
            verhaeltnis = MAX_BREITE / breite
            neue_groesse = (MAX_BREITE, round(hoehe * verhaeltnis))
            img = img.resize(neue_groesse, Image.LANCZOS)
        img.save(pfad, "JPEG", quality=JPEG_QUALITAET, optimize=True)

    alt_kb = quelle.stat().st_size / 1024
    neu_kb = pfad.stat().st_size / 1024
    projekt = pfad.parent.parent.name
    print(f"{projekt}: {alt_kb:.0f} KB -> {neu_kb:.0f} KB")


def main():
    projekte = Path(PROJEKTE_ORDNER)
    if not projekte.is_dir():
        print(f"Ordner nicht gefunden: {projekte}")
        return

    for projekt_ordner in sorted(projekte.iterdir()):
        if not projekt_ordner.is_dir():
            continue
        titelbild = projekt_ordner / "bilder" / DATEINAME
        if titelbild.exists():
            verkleinere_bild(titelbild)
        else:
            print(f"{projekt_ordner.name}: kein {DATEINAME} gefunden")


if __name__ == "__main__":
    main()
