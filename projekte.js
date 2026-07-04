// ============================================
// DCA WEBSITE — KONFIGURATION
// Diese Datei in Notepad bearbeiten
// ============================================

// HERO BILDER (oben auf der Startseite)
// Bilder in den Ordner "hero/" legen
// Dateinamen hier eintragen — beliebige Namen möglich
const HERO_BILDER = [
    "DCA (1).jpg",
    "DCA (10).jpg",
    "DCA (11).jpg",
    "DCA (12).jpg",
    "DCA (13).jpg",
    "DCA (14).jpg",
    "DCA (15).jpg",
    "DCA (16).jpg",
    "DCA (17).jpg",
    "DCA (18).jpg",
    "DCA (19).jpg",
    "DCA (2).jpg",
    "DCA (20).jpg",
    "DCA (21).jpg",
    "DCA (22).jpg",
    "DCA (23).jpg",
    "DCA (24).jpg",
    "DCA (25).jpg",
    "DCA (26).jpg",
    "DCA (27).jpg",
    "DCA (28).jpg",
    "DCA (29).jpg",
    "DCA (3).jpg",
    "DCA (30).jpg",
    "DCA (31).jpg",
    "DCA (32).jpg",
    "DCA (33).jpg",
    "DCA (34).jpg",
    "DCA (35).jpg",
    "DCA (4).jpg",
    "DCA (5).jpg",
    "DCA (6).jpg",
    "DCA (7).jpg",
    "DCA (8).jpg",
    "DCA (9).jpg",
];

// ============================================
// PROJEKTLISTE
// Reihenfolge hier = Reihenfolge auf der Startseite
// Neues Projekt: Block kopieren und einfügen
// ============================================
const PROJEKTE = [
       
        {
        ordner: "101-EAK",
        titel: "Gemeindehaus EAK | Oberhausen",
        untertitel: "Neubau eines Gemeindehauses in Oberhausen",
        auftraggeber: "Evangelische Auferstehungskirchengemeinde Osterfeld",
        ort: "Oberhausen-Osterfeld",
        bgf: "650 m²",
        lph: "1-9 HOAI",
        status: "2020 fertiggestellt",
        team: "Bartosz Czempiel, Lisa Donnerhack und Nicolas Draht (LPH 1-5), Matthias Weber (LPH 6-9)",
        fotos: "© Fotografie Michael Neuhaus, Duisburg",
        auszeichnung: "1. Preis beim Architekturwettbewerb 2015 | 1. Architekturpreis der evangelischen Kirche im Rheinland 2023 | Auszeichnung Baukultur Oberhausen 2024",
        beschreibung: "Das geplante Gemeindehaus soll das vorhandene Gebäude-Ensemble sinnvoll und behutsam ergänzen. Eine klare und bodenständige Architektursprache spiegelt dies ebenso wider wie die Wahl der Materialien im Innen- und Außenraum. In dem Ansatz, das Gebäude baulich und funktional unmittelbar an die Kirche anzuschließen, äußert sich die Strategie für den Umgang mit der historischen Bausubstanz, bei der die Verschmelzung des Alten und Neuen den Gedanken der Einheit von Liturgie und Gemeindeleben repräsentiert. So wird die Außenwand der Kirche zur Innenwand des neuen Gemeindezentrums und macht durch ihre beidseitige Präsenz die Verbundenheit beider Räumlichkeiten erlebbar und wird darüber hinaus ihrer zentralen Rolle bei der Beachtung der historischen Bausubstanz im gestalterischen und funktionalen Kontext gerecht.",
        bilder: 10
    },

{
        ordner: "120-HDS",
        titel: "Haus HDS | Köln",
        untertitel: "Umbau eines Einfamilienhauses",
        auftraggeber: "Privat",
        ort: "Köln",
        bgf: "350 m²",
        lph: "1-8",
        status: "laufendes Projekt",
        team: "DCA Architekten (Köln) in Zusammenarbeit mit sopha Architekten (Köln)",
        fotos: "",
        auszeichnung: "",
        beschreibung: "",
        bilder: 12
    },

 {
        ordner: "010-DCK",
        titel: "Haus DCK | Köln",
        untertitel: "Umbau eines Doppelhauses in Köln",
        auftraggeber: "Privat",
        ort: "Köln",
        bgf: "280 m²",
        lph: "1-3 und 5-9",
        status: "2011 fertiggestellt",
        team: "Lisa Donnerhack und Bartosz Czempiel",
        fotos: "© dca.koeln",
        auszeichnung: "",
        beschreibung: "",
        bilder: 2
        },


    {
        ordner: "102-KHN",
        titel: "Landhaus KHN | Bergisch Gladbach",
        untertitel: "Neubau eines Landhauses",
        auftraggeber: "Privat",
        ort: "Bergisch Gladbach",
        bgf: "300 m²",
        lph: "1-9 HOAI",
        status: "fertiggestellt",
        team: "Lisa Donnerhack, Bartosz Czempiel, Greta Romberger, Nikolas Draht, Philip Euler, Norman Jansen-Nägeler",
        fotos: "",
        auszeichnung: "",
        beschreibung: "Das zweigeschossige Landhaus für eine fünfköpfige Familie wurde als Neubau in Holzbauweise errichtet. Das Ensemble wird durch ein Carport und ein separates Saunagebäude ergänzt. Im Erdgeschoss gehen Wohn-, Koch- und Essbereich fließend ineinander über. Unterschiedlich hohe Raumvolumen erzeugen wechselnde Lichtstimmungen im Tagesverlauf, sodass alle Gemeinschaftszonen vom Sonnenverlauf natürlich durchleuchtet werden. Die Kinderzimmer und zusätzliche Nutzflächen sind klar im Erdgeschoss zoniert. Im Obergeschoss liegen die privaten Räume für Eltern und Gäste. Fassaden und Innenräume bestehen aus nachhaltigen, ökologischen Materialien und betonen den sensiblen Bezug zum angrenzenden Naturschutzgebiet. Naturnahe Außenanlagen und die Nutzung von Regenwasser stärken die lokale Biodiversität und reduzieren den CO2-Fußabdruck.",
        bilder: 31
    },

    {
        ordner: "118-GZN",
        titel: "Gemeindezentrum GZN | Neuss",
        untertitel: "Neubau Gemeindezentrum Nordstadt in Neuss",
        auftraggeber: "Evangelische Stadtgemeinde Neuss",
        ort: "Neuss",
        bgf: "800 m²",
        lph: "Wettbewerb",
        status: "abgeschlossen 2025",
        team: "Bartosz Czempiel und Lisa Donnerhack (Köln) in Zusammenarbeit mit Greta Romberger und Nina Kryvenko (Gießen)",
        fotos: "",
        auszeichnung: "2. Preis beim Architekturwettbewerb",
        beschreibung: "Der Abschied von der Versöhnungskirche fällt uns nicht leicht. Wir schätzen ihr architektonisches Erscheinungsbild ebenso wie die hochwertigen Materialien, aus denen sie erbaut wurde. Doch eine wirtschaftlich vertretbare Kernsanierung ist nicht möglich. Deshalb verfolgen wir mit unserem Neubau ein klares Ziel: Bewahren, was wertvoll ist – und nachhaltig weiterbauen. Unser Konzept setzt auf Wiederverwendung und Ressourcenschonung. Der bestehende Glockenturm bleibt erhalten, ebenso zentrale Elemente wie Altar, Kanzel, Taufbecken und Weltkugel. Doch wir gehen noch weiter: Wir nutzen das Bestandsgebäude als Materialdepot, um wertvolle Ressourcen zu sichern. Die roten Klinkersteine, das Holzpflaster des Bodens, das tragende Holzdachwerk – all das findet im neuen Gemeindehaus eine zweite Heimat. Selbst Leuchten, Saalbestuhlung und Massivholztüren werden wiederverwendet. In einer Zeit, in der nachhaltiges, ressourcenschonendes Bauen immer wichtiger wird, setzen wir auf einen zirkulären Ansatz. Auch wenn dieses Prinzip in der zeitgenössischen Architektur noch jung ist, zeigt ein Blick in die Baugeschichte: Wiederverwendung war schon immer ein fester Bestandteil christlicher Kirchenbauten. Daran knüpfen wir an – mit einem Gemeindehaus, das Tradition und Zukunft verbindet.",
        bilder: 4
    },
        {
        ordner: "040-VVW",
        titel: "Wohnhochhaus VVW | Köln",
        untertitel: "Neubau von vier Wohn(hoch)häusern in Köln",
        auftraggeber: "Privat",
        ort: "Köln",
        bgf: "15.000 m²",
        lph: "Wettbewerb",
        status: "Wettbewerb abgeschlossen",
        team: "Bartosz Czempiel in Zusammenarbeit mit Frederik Jaspert (JSWD Architekten, Köln) und Jakub Sztur (Sztur Architekten, Köln). Entwurf / Konzept (Phase 1 und Phase 2): Bartosz Czempiel. Weitere Teilnehmer: Hadi Teherani (Hamburg), MVRDV (Rotterdam), Benthem Crouwel / Cross architects (Amsterdam, Aachen), RKW Architekten (Düsseldorf), Kister Scheithauer Groß Architekten (Köln)",
        fotos: "",
        auszeichnung: "1. Preis (Baufeld 1 und 4) und 2. Preis (Baufeld 2 und 3) beim 2-phasigen internationalen Wettbewerb",
        beschreibung: "",
        bilder: 4
        },


    {
        ordner: "116-HGK",
        titel: "Haus HGK | Köln",
        untertitel: "Neubau eines Wohn- und Atelierhauses in Köln-Bayenthal",
        auftraggeber: "Privat",
        ort: "Köln",
        bgf: "450 m²",
        lph: "1-3",
        status: "2024 abgeschlossen",
        team: "Bartosz Czempiel und Lisa Donnerhack",
        fotos: "",
        auszeichnung: "",
        beschreibung: "",
        bilder: 3
    },


    {
        ordner: "026-SLM",
        titel: "Haus SLM | Solingen",
        untertitel: "Umbau und Aufstockung eines Einfamilienhauses",
        auftraggeber: "Privat",
        ort: "Solingen",
        bgf: "340 m²",
        lph: "1-8 HOAI",
        status: "fertiggestellt 2013",
        team: "Bartosz Czempiel, Sebastian Filla und Jutta Klare",
        fotos: "Roland Unterbusch",
        auszeichnung: "",
        beschreibung: "Das eingeschossige Einfamilienhaus aus den 70er Jahren wurde vollständig umgebaut. Dazu erfuhr das im Grundriss L-förmige Gebäude eine komplette Neustrukturierung des inneren und äußeren Erscheinungsbildes. Fließend ineinander übergehende Raumabfolgen und variierend hohe Räume prägen die offenen Wohnbereiche im Erdgeschoss. Durch die Aufstockung wurde zusätzlicher Wohnraum geschaffen. Die dunkle Putzfassade ist eine Reminiszenz an die alten, teilweise vollständig mit Schiefer verkleideten Häuser, die typisch für die Region um Solingen sind.",
        bilder: 10
    },

        {
        ordner: "105-BRV",
        titel: "Bürokomplex BRV | Netphen",
        untertitel: "Modernisierung und Umnutzung eines Bürogebäudes in Netphen",
        auftraggeber: "Kriton Immobilien",
        ort: "Netphen",
        bgf: "ca. 12.000 m²",
        lph: "1-8 HOAI",
        status: "2021 fertiggestellt",
        team: "Bartosz Czempiel, Lisa Donnerhack, Matthias Weber, Benjamin Weber, Jakob von Schwanewede und Bernhard Farnschläder",
        fotos: "",
        auszeichnung: "",
        beschreibung: "",
        bilder: 3
        },
    {
        ordner: "117-ODZD",
        titel: "Opernhaus ODZD | Düsseldorf",
        untertitel: "Opernhaus der Zukunft in Düsseldorf",
        auftraggeber: "Stadt Düsseldorf und die Deutsche Oper am Rhein",
        ort: "Düsseldorf",
        bgf: "38.000 m²",
        lph: "internationaler Realisierungswettbewerb",
        status: "abgeschlossen 2025",
        team: "DCA Architekten in Zusammenarbeit mit WXCA Architekci, Warschau",
        fotos: "",
        auszeichnung: "",
        beschreibung: "Die 'Oper der Zukunft' versteht sich als offener, vielfältiger Ort mit zeitloser Gestaltung, der aus dem städtischen Kontext Düsseldorfs entwickelt wurde. Der Standort am Rhein und die Nähe zum Hofgarten prägen das Konzept einer inklusiven Struktur, die Kultur, Natur und Erholung miteinander verbindet. Der Neubau greift diese Qualitäten auf und erweitert sie im Sinne eines 'Forums', das mit anderen Institutionen geteilt wird. Eine Abfolge unterschiedlich gestalteter Räume – von großzügig und repräsentativ bis intim und atmosphärisch – öffnet sich zu den Grünflächen und erfüllt vielfältige Nutzungsansprüche. Das Forum erstreckt sich vom Erdgeschoss entlang der Straßen bis in die oberen Geschosse und verknüpft diese miteinander. Als universeller Raum von überregionaler Bedeutung fügt sich die neue Oper dauerhaft in den kulturellen Kontext Düsseldorfs ein.",
        bilder: 3
    },


    {
        ordner: "104-CUB",
        titel: "Institutsgebäude CUB | Aachen",
        untertitel: "Neubau eines Elektrotechnikinstituts für die RWTH Aachen",
        auftraggeber: "BLB, Aachen Nutzer: RWTH - Institute ITA, IKS & ITHE",
        ort: "Aachen",
        bgf: "6.100 m²",
        lph: "VOF-Verfahren",
        status: "2019 abgeschlossen",
        team: "Bartosz Czempiel in Zusammenarbeit mit Frederik Jaspert und Christian Mammel (JSWD Architekten, Köln).",
        fotos: "",
        auszeichnung: "",
        beschreibung: "",
        bilder: 5
    },

        {
        ordner: "901-TZA",
        titel: "Fraunhofer Institut TZA | Darmstadt",
        untertitel: "Neubau eines Transferzentrums für Adaptronik in Darmstadt",
        auftraggeber: "Fraunhofer-Gesellschaft, München (Nutzer: Fraunhofer LBF, Darmstadt)",
        ort: "Darmstadt",
        bgf: "2.300 m²",
        lph: "1-9 HOAI",
        status: "fertiggestellt 2010",
        team: "Bartosz Czempiel (Federführung LPH 1-5) bei JSWD Architekten",
        fotos: "JSWD Architekten / dca.koeln",
        auszeichnung: "1. Preis beim Verhandlungsverfahren",
        beschreibung: "",
        bilder: 4
        },


    // NEUES PROJEKT EINFÜGEN — Kommentarzeichen // entfernen:
    // {
    //     ordner: "ORDNERNAME",
    //     titel: "Projekttitel | Ort",
    //     untertitel: "Kurzbeschreibung",
    //     auftraggeber: "",
    //     ort: "",
    //     bgf: "",
    //     lph: "",
    //     status: "",
    //     team: "",
    //     fotos: "",
    //     auszeichnung: "",
    //     beschreibung: "",
    //     bilder: 10
    // },
];
