# ============================================================
# DCA — Projektseiten-Typografie vereinheitlichen
# Legt dieses Skript in den Ordner "projekte" und einmal starten.
# ============================================================

import os, glob

basis = os.path.dirname(os.path.abspath(__file__))

ERSETZUNGEN = [
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
        '            letter-spacing: 0.1em;'
    ),
    (
        '.info-block h4 {\n'
        '            font-size: 1.5rem;\n'
        '            font-weight: 600;',
        '.info-block h4 {\n'
        '            font-size: 1.1rem;\n'
        '            font-weight: 700;'
    ),
    (
        '.projekt-info .untertitel { margin-bottom: 3.5rem; }',
        '.projekt-info .untertitel { margin-bottom: 2rem; }'
    ),
]


def main():
    print()
    print("=" * 54)
    print("  DCA — Projektseiten-Typografie vereinheitlichen")
    print("=" * 54)
    print()

    geaendert = 0
    unveraendert = 0

    for pfad in sorted(glob.glob(os.path.join(basis, "*", "index.html"))):
        ordner = os.path.basename(os.path.dirname(pfad))
        if ordner.startswith("_"):
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
