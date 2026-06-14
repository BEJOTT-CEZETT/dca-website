# ============================================================
# DCA — Hero-Bilder aktualisieren
# ============================================================
# Liest alle Bilder aus dem hero/-Ordner und trägt sie
# automatisch in projekte.js ein.
#
# Ablage: Website-Hauptordner (neben projekte.js)
# Starten: Doppelklick oder python hero_aktualisieren.py
# ============================================================

import os, sys, glob, re

if getattr(sys, 'frozen', False):
    basis = os.path.dirname(sys.executable)
else:
    basis = os.path.dirname(os.path.abspath(__file__))

hero_ordner = os.path.join(basis, "hero")
js_pfad     = os.path.join(basis, "projekte.js")

print()
print("=" * 50)
print("  DCA — Hero-Bilder aktualisieren")
print("=" * 50)

if not os.path.isdir(hero_ordner):
    print(f"\n  ⚠  hero/-Ordner nicht gefunden: {hero_ordner}")
    input("\n  Enter zum Beenden...")
    sys.exit()

if not os.path.exists(js_pfad):
    print(f"\n  ⚠  projekte.js nicht gefunden: {js_pfad}")
    input("\n  Enter zum Beenden...")
    sys.exit()

# Alle Bilddateien im hero/-Ordner einlesen
gefunden = {}
for f in glob.glob(os.path.join(hero_ordner, "*")):
    ext = os.path.splitext(f)[1].lower()
    if ext in [".jpg", ".jpeg", ".png", ".tif"]:
        key = os.path.normcase(os.path.basename(f))
        if key not in gefunden:
            gefunden[key] = os.path.basename(f)

dateien = sorted(gefunden.values(), key=lambda f: os.path.normcase(f))

if not dateien:
    print(f"\n  ⚠  Keine Bilder im hero/-Ordner gefunden.")
    input("\n  Enter zum Beenden...")
    sys.exit()

print(f"\n  {len(dateien)} Bilder gefunden:")
for d in dateien:
    print(f"    → {d}")

# Neue HERO_BILDER Liste bauen
zeilen = ',\n'.join([f'    "{d}"' for d in dateien])
neue_liste = f"const HERO_BILDER = [\n{zeilen},\n];"

# In projekte.js ersetzen
with open(js_pfad, encoding="utf-8") as f:
    inhalt = f.read()

# Alten Block per Regex ersetzen
muster = r'const HERO_BILDER = \[.*?\];'
neuer_inhalt = re.sub(muster, neue_liste, inhalt, flags=re.DOTALL)

if neuer_inhalt == inhalt:
    print("\n  ⚠  HERO_BILDER-Block nicht gefunden — nichts geändert.")
else:
    with open(js_pfad, "w", encoding="utf-8") as f:
        f.write(neuer_inhalt)
    print(f"\n  ✓  projekte.js aktualisiert.")

print()
print("=" * 50)
input("  Enter zum Beenden...")
