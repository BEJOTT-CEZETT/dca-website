# ============================================================
# DCA — Neues Projekt einrichten v3
# ============================================================
# Struktur:
#
#   projekte/
#     _NEUES_PROJEKT/
#       dca_neues_projekt.exe   ← EXE hier (nicht in dist/)
#       118-GZN.txt
#       bilder_input/
#           foto1.jpg ...
#     _VORLAGE/
#       index.html
#   projekte.js
# ============================================================

import os, sys, shutil, glob

# ---- Pfade ermitteln ----
if getattr(sys, 'frozen', False):
    exe_ordner = os.path.dirname(sys.executable)
else:
    exe_ordner = os.path.dirname(os.path.abspath(__file__))

proj_ordner  = os.path.dirname(exe_ordner)
basis        = os.path.dirname(proj_ordner)
js_pfad      = os.path.join(basis, "projekte.js")
vorlage_pfad = os.path.join(proj_ordner, "_VORLAGE", "index.html")
bilder_input = os.path.join(exe_ordner, "bilder_input")


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def trennlinie():
    print("=" * 54)


def pfade_pruefen():
    """Gibt Warnung aus wenn Pfade nicht stimmen."""
    ok = True
    if not os.path.exists(js_pfad):
        print(f"  ⚠  projekte.js nicht gefunden: {js_pfad}")
        ok = False
    if not os.path.exists(vorlage_pfad):
        print(f"  ⚠  Vorlage nicht gefunden: {vorlage_pfad}")
        ok = False
    # Sicherheitsprüfung: EXE darf nicht in dist/ liegen
    if os.path.basename(exe_ordner).lower() == "dist":
        print(f"  ⚠  EXE liegt noch im dist/-Ordner!")
        print(f"     Bitte erst nach _NEUES_PROJEKT/ verschieben.")
        ok = False
    return ok


def finde_textdatei():
    treffer = [
        f for f in glob.glob(os.path.join(exe_ordner, "*.txt"))
        if os.path.isfile(f)
    ]
    return treffer[0] if treffer else None


def parse_info(pfad):
    daten = {
        "titel": "", "untertitel": "", "auftraggeber": "",
        "ort": "", "bgf": "", "lph": "", "status": "",
        "team": "", "fotos": "", "auszeichnung": "", "beschreibung": "",
    }
    with open(pfad, encoding="utf-8") as f:
        zeilen = [z.strip() for z in f.readlines()]

    nicht_leer = [z for z in zeilen if z and z != "Projektdaten:"]
    if len(nicht_leer) >= 1:
        daten["titel"] = nicht_leer[0]
    if len(nicht_leer) >= 2 and ":" not in nicht_leer[1]:
        daten["untertitel"] = nicht_leer[1]

    felder = {
        "Auftraggeber": "auftraggeber",
        "Ort": "ort", "Standort": "ort",
        "BGF": "bgf", "NUF": "bgf", "Nutzfläche": "bgf",
        "LPH": "lph", "Leistungsphase": "lph",
        "Status": "status", "Team": "team",
        "Fotos": "fotos", "Auszeichnung": "auszeichnung",
        "Beschreibung": "beschreibung",
        "Projektbeschreibung": "beschreibung",
    }

    aktives_feld = None
    puffer = []

    for zeile in zeilen:
        gefunden = False
        for schlüssel, feld in felder.items():
            if zeile.lower().startswith(schlüssel.lower() + ":"):
                if aktives_feld and puffer:
                    daten[aktives_feld] = " ".join(puffer).strip()
                wert = zeile[len(schlüssel)+1:].strip()
                aktives_feld = feld
                puffer = [wert] if wert else []
                gefunden = True
                break
        if not gefunden and aktives_feld:
            if zeile:
                puffer.append(zeile)
            else:
                if puffer:
                    daten[aktives_feld] = " ".join(puffer).strip()
                aktives_feld = None
                puffer = []

    if aktives_feld and puffer:
        daten[aktives_feld] = " ".join(puffer).strip()

    return daten


def bilder_umbenennen(bilder_output):
    """Kopiert Bilder aus bilder_input nach bilder_output mit neuem Namen."""

    # Sicherstellen dass Quelle und Ziel verschieden sind
    quelle = os.path.realpath(bilder_input)
    ziel   = os.path.realpath(bilder_output)
    if quelle == ziel:
        print("  ⚠  Quelle und Ziel sind identisch — abgebrochen.")
        return 0

    os.makedirs(bilder_output, exist_ok=True)

    # Set mit normcase verhindert Duplikate auf Windows zuverlässig
    gefunden = {}
    for f in glob.glob(os.path.join(bilder_input, "*")):
        ext = os.path.splitext(f)[1].lower()
        if ext in [".jpg", ".jpeg", ".png", ".tif"]:
            key = os.path.normcase(os.path.basename(f))
            if key not in gefunden:
                gefunden[key] = f
    dateien = sorted(gefunden.values(), key=lambda f: os.path.normcase(os.path.basename(f)))

    if not dateien:
        print("    ⚠  Keine Bilder in bilder_input gefunden.")
        return 0

    for i, quelle_datei in enumerate(dateien, start=1):
        ziel_datei = os.path.join(bilder_output, f"DCA ({i}).jpg")
        shutil.copy2(quelle_datei, ziel_datei)
        print(f"    {i:02d}  {os.path.basename(quelle_datei):<40} → DCA ({i}).jpg")

    # Titelbild
    shutil.copy2(
        os.path.join(bilder_output, "DCA (1).jpg"),
        os.path.join(bilder_output, "DCA-Titelbild.jpg")
    )
    print(f"    →  DCA-Titelbild.jpg erstellt")
    return len(dateien)


def projektseite_erstellen(ziel_pfad):
    ziel = os.path.join(ziel_pfad, "index.html")
    if os.path.exists(ziel):
        print("    → index.html bereits vorhanden.")
        return
    if os.path.exists(vorlage_pfad):
        shutil.copy2(vorlage_pfad, ziel)
        print("    → index.html aus Vorlage kopiert.")
    else:
        print(f"    ⚠  Vorlage nicht gefunden.")


def in_js_eintragen(ordner, daten, anzahl):
    with open(js_pfad, encoding="utf-8") as f:
        inhalt = f.read()

    if f'ordner: "{ordner}"' in inhalt:
        print(f"    → '{ordner}' bereits eingetragen, übersprungen.")
        return

    titel = daten["titel"]
    if " | " not in titel:
        if daten["ort"]:
            titel = f"{titel} | {daten['ort']}"

    block = (
        f'    {{\n'
        f'        ordner: "{ordner}",\n'
        f'        titel: "{titel}",\n'
        f'        untertitel: "{daten["untertitel"]}",\n'
        f'        auftraggeber: "{daten["auftraggeber"]}",\n'
        f'        ort: "{daten["ort"]}",\n'
        f'        bgf: "{daten["bgf"]}",\n'
        f'        lph: "{daten["lph"]}",\n'
        f'        status: "{daten["status"]}",\n'
        f'        team: "{daten["team"]}",\n'
        f'        fotos: "{daten["fotos"]}",\n'
        f'        auszeichnung: "{daten["auszeichnung"]}",\n'
        f'        beschreibung: "{daten["beschreibung"]}",\n'
        f'        bilder: {anzahl}\n'
        f'    }},\n'
    )

    marke = "const PROJEKTE = [\n"
    if marke not in inhalt:
        print("    ⚠  'const PROJEKTE = [' nicht gefunden.")
        return

    with open(js_pfad, "w", encoding="utf-8") as f:
        f.write(inhalt.replace(marke, marke + block, 1))
    print(f"    → An erster Stelle in projekte.js eingetragen.")


def aufraeumen(txt_pfad):
    """Löscht .txt und Rohbilder in bilder_input. Ordner bleibt erhalten."""
    # .txt löschen
    try:
        os.remove(txt_pfad)
        print(f"    → {os.path.basename(txt_pfad)} gelöscht.")
    except Exception as e:
        print(f"    ⚠  Konnte txt nicht löschen: {e}")
    # Rohbilder in bilder_input löschen, Ordner bleibt
    if os.path.isdir(bilder_input):
        for f in os.scandir(bilder_input):
            if f.is_file():
                try:
                    os.remove(f.path)
                except Exception:
                    pass
        print(f"    → Rohbilder aus bilder_input/ gelöscht. Ordner bleibt.")


# ============================================================
# HAUPTPROGRAMM
# ============================================================

def main():
    print()
    trennlinie()
    print("  DCA — Neues Projekt einrichten")
    trennlinie()

    # Pfade prüfen
    if not pfade_pruefen():
        print()
        input("  Fehler — Enter zum Beenden...")
        return

    print(f"\n  Website-Ordner: {basis}")
    print(f"  projekte/:      {proj_ordner}")

    # Textdatei suchen
    txt_pfad = finde_textdatei()
    if not txt_pfad:
        print("\n  ⚠  Keine .txt Datei gefunden.")
        print(f"     Erwartet in: {exe_ordner}")
        print()
        input("  Enter zum Beenden...")
        return

    # bilder_input prüfen
    if not os.path.isdir(bilder_input):
        print(f"\n  ⚠  bilder_input/ Ordner nicht gefunden.")
        print(f"     Erwartet in: {exe_ordner}")
        print()
        input("  Enter zum Beenden...")
        return

    # Ordnername aus Dateiname
    ordnername = os.path.splitext(os.path.basename(txt_pfad))[0]
    ziel_pfad  = os.path.join(proj_ordner, ordnername)

    print(f"\n  Textdatei:  {os.path.basename(txt_pfad)}")
    print(f"  Zielordner: {ziel_pfad}")

    # Zielordner darf noch nicht existieren
    if os.path.exists(ziel_pfad):
        print(f"\n  ⚠  Zielordner existiert bereits: {ziel_pfad}")
        antwort = input("     Überschreiben? (j/n): ").strip().lower()
        if antwort != "j":
            print("  Abgebrochen.")
            input("  Enter zum Beenden...")
            return

    # Infos parsen
    daten = parse_info(txt_pfad)
    print(f"\n  Titel:   {daten['titel']}")
    print(f"  Status:  {daten['status']}")

    # Zielordner anlegen
    os.makedirs(ziel_pfad, exist_ok=True)

    # 1. Bilder umbenennen und kopieren
    print(f"\n  Bilder:")
    bilder_output = os.path.join(ziel_pfad, "bilder")
    anzahl = bilder_umbenennen(bilder_output)

    if anzahl == 0:
        print("\n  ⚠  Keine Bilder verarbeitet — Abbruch.")
        shutil.rmtree(ziel_pfad)
        input("  Enter zum Beenden...")
        return

    # 2. info.txt kopieren
    shutil.copy2(txt_pfad, os.path.join(ziel_pfad, "info.txt"))
    print(f"\n  info.txt kopiert.")

    # 3. index.html erstellen
    print(f"\n  Projektseite:")
    projektseite_erstellen(ziel_pfad)

    # 4. projekte.js eintragen
    print(f"\n  projekte.js:")
    in_js_eintragen(ordnername, daten, anzahl)

    # 5. Aufräumen (erst ganz am Ende!)
    print(f"\n  Aufräumen:")
    aufraeumen(txt_pfad)

    print()
    trennlinie()
    print(f"  ✓  {ordnername} erfolgreich abgeschlossen.")
    print(f"     {anzahl} Bilder verarbeitet.")
    trennlinie()
    print()
    input("  Enter zum Beenden...")


if __name__ == "__main__":
    main()
