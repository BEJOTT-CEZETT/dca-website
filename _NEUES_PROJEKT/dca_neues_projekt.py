# ============================================================
# DCA — Neues Projekt einrichten v4
# ============================================================

import os, sys, shutil, glob, re

if getattr(sys, 'frozen', False):
    exe_ordner = os.path.dirname(sys.executable)
else:
    exe_ordner = os.path.dirname(os.path.abspath(__file__))

proj_ordner  = os.path.dirname(exe_ordner)
basis        = os.path.dirname(proj_ordner)
js_pfad      = os.path.join(basis, "projekte.js")
vorlage_pfad = os.path.join(proj_ordner, "_VORLAGE", "index.html")
bilder_input = os.path.join(exe_ordner, "bilder_input")


def trennlinie():
    print("=" * 54)


def pfade_pruefen():
    ok = True
    if not os.path.exists(js_pfad):
        print(f"  ⚠  projekte.js nicht gefunden: {js_pfad}")
        ok = False
    if not os.path.exists(vorlage_pfad):
        print(f"  ⚠  Vorlage nicht gefunden: {vorlage_pfad}")
        ok = False
    if os.path.basename(exe_ordner).lower() == "dist":
        print(f"  ⚠  EXE liegt noch im dist/-Ordner!")
        ok = False
    return ok


def finde_textdatei():
    # Erst neue info.txt-Format, dann alte .txt
    info_pfad = os.path.join(exe_ordner, "info.txt")
    if os.path.exists(info_pfad):
        return info_pfad
    treffer = [f for f in glob.glob(os.path.join(exe_ordner, "*.txt")) if os.path.isfile(f)]
    return treffer[0] if treffer else None


def parse_info(pfad):
    daten = {
        "titel": "", "untertitel": "", "auftraggeber": "",
        "ort": "", "bgf": "", "lph": "", "status": "",
        "team": "", "fotos": "", "auszeichnung": "", "beschreibung": "",
    }
    with open(pfad, encoding="utf-8") as f:
        inhalt = f.read()

    # Neues Format: key=value
    if "=" in inhalt.split("\n")[0]:
        for zeile in inhalt.splitlines():
            if "=" in zeile:
                key, _, val = zeile.partition("=")
                key = key.strip().lower()
                val = val.strip()
                if key in daten:
                    daten[key] = val
        return daten

    # Altes Format: Fließtext mit Schlüssel:
    zeilen = [z.strip() for z in inhalt.splitlines()]
    nicht_leer = [z for z in zeilen if z and z != "Projektdaten:"]
    if len(nicht_leer) >= 1:
        daten["titel"] = nicht_leer[0]
    if len(nicht_leer) >= 2 and ":" not in nicht_leer[1]:
        daten["untertitel"] = nicht_leer[1]

    felder = {
        "Auftraggeber": "auftraggeber", "Ort": "ort", "Standort": "ort",
        "BGF": "bgf", "NUF": "bgf", "LPH": "lph", "Leistungsphase": "lph",
        "Status": "status", "Team": "team", "Fotos": "fotos",
        "Auszeichnung": "auszeichnung", "Beschreibung": "beschreibung",
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
    quelle = os.path.realpath(bilder_input)
    ziel   = os.path.realpath(bilder_output)
    if quelle == ziel:
        print("  ⚠  Quelle und Ziel identisch.")
        return 0
    os.makedirs(bilder_output, exist_ok=True)
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
    shutil.copy2(
        os.path.join(bilder_output, "DCA (1).jpg"),
        os.path.join(bilder_output, "DCA-Titelbild.jpg")
    )
    print(f"    →  DCA-Titelbild.jpg erstellt")
    return len(dateien)


def projektseite_erstellen(ziel_pfad, daten, ordnername, anzahl):
    """Kopiert Vorlage und befüllt sie mit den Projektdaten."""
    ziel = os.path.join(ziel_pfad, "index.html")
    if not os.path.exists(vorlage_pfad):
        print(f"    ⚠  Vorlage nicht gefunden.")
        return

    with open(vorlage_pfad, encoding="utf-8") as f:
        html = f.read()

    # Kurztitel (ohne Ortsangabe nach |)
    kurztitel = daten["titel"].split("|")[0].strip() if "|" in daten["titel"] else daten["titel"]
    untertitel = daten["untertitel"].upper() if daten["untertitel"] else ""

    # Titel im <title>-Tag
    html = re.sub(r"<title>[^<]*</title>", f"<title>{kurztitel} | DCA Architekten</title>", html)

    # h2
    html = re.sub(r"<h2>[^<]*</h2>", f"<h2>{kurztitel}</h2>", html)

    # Untertitel
    html = re.sub(r'<div class="untertitel">[^<]*</div>', f'<div class="untertitel">{untertitel}</div>', html)

    # Bildanzahl
    html = re.sub(r"const BILDANZAHL = \d+[^;]*;", f"const BILDANZAHL = {anzahl};", html)

    # Projektdaten-Block ersetzen
    projektdaten = (
        f'                <div class="info-block">\n'
        f'                    <h4>Projektdaten</h4>\n'
        f'                    <p>Auftraggeber: {daten["auftraggeber"]}<br>\n'
        f'                    Ort: {daten["ort"]}<br>\n'
    )
    if daten["bgf"]:
        projektdaten += f'                    BGF: {daten["bgf"]}<br>\n'
    projektdaten += (
        f'                    LPH: {daten["lph"]}<br>\n'
        f'                    Status: {daten["status"]}</p>\n'
        f'                </div>\n'
        f'                <div class="info-block">\n'
        f'                    <h4>Team</h4>\n'
        f'                    <p>{daten["team"]}</p>\n'
        f'                </div>'
    )

    # Auszeichnung einfügen wenn vorhanden
    aus_block = ""
    if daten["auszeichnung"]:
        aus_block = (
            f'                <div class="info-block">\n'
            f'                    <h4>Auszeichnung</h4>\n'
            f'                    <p class="auszeichnung">{daten["auszeichnung"]}</p>\n'
            f'                </div>\n'
        )

    # Fotos einfügen wenn vorhanden
    foto_block = ""
    if daten["fotos"]:
        foto_block = (
            f'\n                <div class="info-block">\n'
            f'                    <h4>Fotos</h4>\n'
            f'                    <p>{daten["fotos"]}</p>\n'
            f'                </div>'
        )

    # Alten Projektdaten-Platzhalter ersetzen
    html = re.sub(
        r'<!-- Auszeichnung.*?<!-- Fotos.*?-->\s*',
        aus_block,
        html,
        flags=re.DOTALL
    )
    html = re.sub(
        r'<div class="info-block">\s*<h4>Projektdaten</h4>.*?</div>\s*<div class="info-block">\s*<h4>Team</h4>.*?</div>',
        projektdaten + foto_block,
        html,
        flags=re.DOTALL
    )

    with open(ziel, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"    → index.html erstellt und befüllt.")


def in_js_eintragen(ordner, daten, anzahl):
    with open(js_pfad, encoding="utf-8") as f:
        inhalt = f.read()
    if f'ordner: "{ordner}"' in inhalt:
        print(f"    → '{ordner}' bereits eingetragen.")
        return
    titel = daten["titel"]
    if " | " not in titel and daten["ort"]:
        titel = f"{titel} | {daten['ort']}"
    block = (
        f'        {{\n'
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
        f'        beschreibung: "",\n'
        f'        bilder: {anzahl}\n'
        f'        }},\n'
    )
    marke = "const PROJEKTE = [\n"
    if marke not in inhalt:
        print("    ⚠  'const PROJEKTE = [' nicht gefunden.")
        return
    with open(js_pfad, "w", encoding="utf-8") as f:
        f.write(inhalt.replace(marke, marke + block, 1))
    print(f"    → In projekte.js eingetragen.")


def aufraeumen(txt_pfad):
    try:
        os.remove(txt_pfad)
        print(f"    → {os.path.basename(txt_pfad)} gelöscht.")
    except Exception as e:
        print(f"    ⚠  Konnte txt nicht löschen: {e}")
    if os.path.isdir(bilder_input):
        for f in os.scandir(bilder_input):
            if f.is_file():
                try:
                    os.remove(f.path)
                except Exception:
                    pass
        print(f"    → Rohbilder gelöscht.")


def main():
    print()
    trennlinie()
    print("  DCA — Neues Projekt einrichten v4")
    trennlinie()

    if not pfade_pruefen():
        input("\n  Fehler — Enter zum Beenden...")
        return

    txt_pfad = finde_textdatei()
    if not txt_pfad:
        print("\n  ⚠  Keine info.txt Datei gefunden.")
        input("  Enter zum Beenden...")
        return

    if not os.path.isdir(bilder_input):
        print(f"\n  ⚠  bilder_input/ nicht gefunden.")
        input("  Enter zum Beenden...")
        return

    ordnername = os.path.splitext(os.path.basename(txt_pfad))[0]
    # info.txt -> Ordnername aus Ordner-Dateiname (z.B. 121-XYZ.txt)
    if ordnername == "info":
        # Fallback: Ordnername des exe_ordners nehmen? Nein — Fehler ausgeben
        print("\n  ⚠  Datei muss [NUMMER-KÜRZEL].txt heißen, z.B. 121-XYZ.txt")
        print("     'info.txt' ist nur die Vorlage, nicht umbenennen!")
        input("  Enter zum Beenden...")
        return

    ziel_pfad = os.path.join(proj_ordner, ordnername)

    print(f"\n  Textdatei:  {os.path.basename(txt_pfad)}")
    print(f"  Zielordner: {ziel_pfad}")

    if os.path.exists(ziel_pfad):
        antwort = input(f"\n  ⚠  '{ordnername}' existiert bereits. Überschreiben? (j/n): ").strip().lower()
        if antwort != "j":
            input("  Abgebrochen. Enter zum Beenden...")
            return

    daten = parse_info(txt_pfad)
    print(f"\n  Titel:  {daten['titel']}")
    print(f"  Status: {daten['status']}")

    os.makedirs(ziel_pfad, exist_ok=True)

    print(f"\n  Bilder:")
    bilder_output = os.path.join(ziel_pfad, "bilder")
    anzahl = bilder_umbenennen(bilder_output)

    if anzahl == 0:
        print("\n  ⚠  Keine Bilder — Abbruch.")
        shutil.rmtree(ziel_pfad)
        input("  Enter zum Beenden...")
        return

    shutil.copy2(txt_pfad, os.path.join(ziel_pfad, "info.txt"))
    print(f"\n  info.txt kopiert.")

    print(f"\n  Projektseite:")
    projektseite_erstellen(ziel_pfad, daten, ordnername, anzahl)

    print(f"\n  projekte.js:")
    in_js_eintragen(ordnername, daten, anzahl)

    print(f"\n  Aufräumen:")
    aufraeumen(txt_pfad)

    print()
    trennlinie()
    print(f"  ✓  {ordnername} abgeschlossen. {anzahl} Bilder.")
    trennlinie()
    print()
    input("  Enter zum Beenden...")


if __name__ == "__main__":
    main()
