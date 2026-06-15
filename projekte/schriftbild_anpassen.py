# ============================================================
# DCA — Projektseiten: Typografie vereinheitlichen
#       + Buchstabenabstände reduzieren
# Legt dieses Skript in den Ordner "projekte" und einmal starten.
# Ersetzt das vorherige Skript "typografie_vereinheitlichen.py".
# ============================================================

import os, glob

basis = os.path.dirname(os.path.abspath(__file__))

ERSETZUNGEN = [
    # --- H2 Titel: Variante A (alt: 2.4rem/600/0.06em) -> Ziel ---
    (
        '.projekt-info h2 {\n'
        '            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;\n'
        '            font-size: 2.4rem;\n'
        '            font-weight: 600;\n'
        '            letter-spacing: 0.06em;',
        '.projekt-info h2 {\n'
        '            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;\n'
        '            font-size: 1.9rem;\n'
        '            font-weight: 700;\n'
        '            letter-spacing: 0.02em;'
    ),
    # --- H2 Titel: Variante B (neu: 1.9rem/700/0.1em) -> Ziel ---
    (
        '.projekt-info h2 {\n'
        '            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;\n'
        '            font-size: 1.9rem;\n'
        '            font-weight: 700;\n'
        '            letter-spacing: 0.1em;',
        '.projekt-info h2 {\n'
        '            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;\n'
        '            font-size: 1.9rem;\n'
        '            font-weight: 700;\n'
        '            letter-spacing: 0.02em;'
    ),
    # --- Untertitel: letter-spacing reduzieren ---
    (
        '.projekt-info .untertitel {\n'
        '            font-size: 1.5rem;\n'
        '            color: #000;\n'
        '            margin-bottom: 3rem;\n'
        '            line-height: 1.5;\n'
        '            text-transform: uppercase;\n'
        '            letter-spacing: 0.06em;\n'
        '        }',
        '.projekt-info .untertitel {\n'
        '            font-size: 1.5rem;\n'
        '            color: #000;\n'
        '            margin-bottom: 3rem;\n'
        '            line-height: 1.5;\n'
        '            text-transform: uppercase;\n'
        '            letter-spacing: 0.01em;\n'
        '        }'
    ),
    # --- Info-block h4: Variante A (alt: 1.5rem/600/0.15em) -> Ziel ---
    (
        '.info-block h4 {\n'
        '            font-size: 1.5rem;\n'
        '            font-weight: 600;\n'
        '            letter-spacing: 0.15em;',
        '.info-block h4 {\n'
        '            font-size: 1.1rem;\n'
        '            font-weight: 700;\n'
        '            letter-spacing: 0.05em;'
    ),
    # --- Info-block h4: Variante B (neu: 1.1rem/700/0.15em) -> Ziel ---
    (
        '.info-block h4 {\n'
        '            font-size: 1.1rem;\n'
        '            font-weight: 700;\n'
        '            letter-spacing: 0.15em;',
        '.info-block h4 {\n'
        '            font-size: 1.1rem;\n'
        '            font-weight: 700;\n'
        '            letter-spacing: 0.05em;'
    ),
    # --- Untertitel Abstand nach unten (alt) -> Ziel ---
    (
        '.projekt-info .untertitel { margin-bottom: 3.5rem; }',
        '.projekt-info .untertitel { margin-bottom: 2rem; }'
    ),
]


def main():
    print()
    print("=" * 54)
    print("  DCA — Typografie & Buchstabenabstände anpassen")
    print("=" * 54)
    print()

    geaendert = 0
    unveraendert = 0

    for pfad in sorted(glob.glob(os.path.join(basis, "*", "index.html"))):
        ordner = os.path.basename(os.path.dirname(pfad))
        if ordner == "_NEUES_PROJEKT":
            continue

        with open(pfad, encoding="utf-8") as f:
            html = f.read()

        original = html
        for alt, neu in ERSETZUNGEN:
            html = html.replace(alt, neu)

        if html != original:
            with open(pfad, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  ✓  {ordner}  — angepasst")
            geaendert += 1
        else:
            print(f"  –  {ordner}  — keine Änderung nötig")
            unveraendert += 1

    print()
    print("=" * 54)
    print(f"  {geaendert} Seiten angepasst, {unveraendert} bereits aktuell.")
    print("=" * 54)
    print()
    input("  Enter zum Beenden...")


if __name__ == "__main__":
    main()
