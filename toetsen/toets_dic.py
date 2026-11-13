""" Oefening 1 (  / 2)
Los onderstaande vragen op door gebruik te maken van de geneste dictionary 'pc'.
"""

pc = {
    "processor": {
        "merk": "Intel",
        "model": "i7-12700K",
        "specificaties": {"kloksnelheid": "3.6GHz", "cores": 12, "threads": 20},
        "compatibele_sockets": ["LGA1200", "LGA1700", "LGA1800"]
    },
    "geheugen": {
        "type": "DDRM",
        "capaciteit": "32GB",
        "snelheid": "3200MHz"
    },
    "opslagmedia": {
        "HDD1": {"type": "HDD", "capaciteit": "1TB", "snelheid": "7200RPM"},
        "HDD2": {"type": "HDD", "capaciteit": "256GB", "snelheid": "7200RPM"},
        "SSD1": {"type": "NVMe", "capaciteit": "512GB", "leessnelheid": "3500MB/s"},
        "SSD2": {"type": "NVMe", "capaciteit": "256GB", "leessnelheid": "3500MB/s"}

    },
    "grafische_kaart": {
        "merk": "NVIDIA",
        "model": "RTX 3060",
        "geheugen": "12GB",
        "poorten": ["HDMI", "DisplayPort", "DVI"],
    },
    "revews": ["3/5", "7/10", "3,5 sterren"]
}

""" Vraag 1 ( /0.5) 
Print onderstaande zin. Haal het socket-type op uit bovenstaande dictionary.
'De processor ondersteunt socket-type: LGA1700'
"""
print(f"de processor ondersteunt socket-type: {pc['processor']["compatibele_sockets"][1]} ")
""" Vraag 2 ( /0.5) 
Update de geheugencapaciteit.
Het huidige geheugentype klopt niet. Verander "DDRM" naar "DDR5".
"""
pc["geheugen"]["type"] = "DDR5"


""" Vraag 3 ( /0.5) 
De sleutel "revews" is verkeerd gespeld. Corrigeer dit naar "reviews" in de dictionary.
Zorg ervoor dat de waarde verbonden aan deze sleutel wel hetzelfde blijft.
  TIP! Maak een nieuwe sleutel aan met de correcte naam, verwijder erna de oude sleutel.
"""
pc["revieuws"] = ["3/5", "7/10", "3,5 sterren"]
pc.pop("revews")

""" Vraag 4 ( /0.5) 
Print een overzicht van alle opslagmedia en hun capaciteiten.
Het overzicht moet blijven werken ook als er honderden opslagmedia zijn.

De output moet er als volgt uitzien.
    Opslagoverzicht:
        - HDD1: 1TB
        - HDD2: 256GB
        - SSD1: 512GB
        - SSD2: 128GB
        - ... (voor ieder ander opslagmedia dat je zelf kan toevoegen)
        
"""
pc_opslagmedia = pc["opslagmedia"]
for onderdeel, waarde in pc_opslagmedia.items():
    print(f"{onderdeel}: {waarde['capaciteit']}")


""" Oefening 2 (   / 3)
Onderstaande structuur geeft per persoon het aantal gemaakte doelpunt over 5 wedstrijden.
Print wie gemiddeld de meeste doelpunten heeft gemaakt, en hoeveel er dit waren.
Print wie gemiddeld de minste doelpunten heeft gemaakt, en hoeveel er dit waren.
De code moet blijven werken, ook als er later meer personen bijkomen.

Voor de start-datastructuur is dit het correcte antwoord.
    Meest: Sarah (2.6 doelpunten per match)
    Minst: Kiana (1.2 doelpunten per match)

"""
hoogste_gem = 0
persoon_hoogste = ""
laagste_gem = 99999
persoon_laagste = ""
sport_uitslagen = {
    'Emma': [2, 3, 1, 4, 2],  # Aantal doelpunten per wedstrijd
    'Liam': [1, 2, 1, 3, 0],
    'Noah': [0, 1, 2, 1, 3],
    'Sarah': [3, 3, 4, 2, 1],
    'Kiana': [1, 0, 2, 1, 2],
    'Lucas': [2, 1, 3, 1, 0]
}
for persoon, doelpunten_match in sport_uitslagen.items():
    doelpunten_gem = 0
    for index, doelpunten in enumerate(doelpunten_match):
        doelpunten_gem += doelpunten
    doelpunten_gem/= 5
    if doelpunten_gem > hoogste_gem:
        hoogste_gem = doelpunten_gem
        persoon_hoogste = persoon
    if doelpunten_gem < laagste_gem:
        laagste_gem = doelpunten_gem
        persoon_laagste = persoon
print(f"Meest: {persoon_hoogste}, ({hoogste_gem} doelpunten per match)")
print(f"Minst: {persoon_laagste}, ({laagste_gem} doelpunten per match)")

""" OEFENING 3 (  / 5)
Onderstaande datastructuur bevat als elementen de vragen/antwoorden van een quiz-spel.
Hiernaast bevat het ook hoeveel geld iedere vraag waard is.
Sommige vragen hebben ook een hint. Die hint mag enkel getoond worden als ze aanwezig is.

Stel iedere vraag aan de deelnemer (via de functie input).
Toon eerst de hint als deze bestaat (ZIE VOORBEELD).

Controleer het antwoord en print of de deelnemer het juist/fout had.
 - Heeft de deelnemer het juist? Voeg het gewonnen geld dan toe aan een prijzenpot.
 - Heeft de deelnemer het fout? Print dan ook wat het juiste antwoord was.
Na het overlopen van alle elementen print je hoeveel geld de deelnemer gewonnen heeft.

De code moet blijven werken, ook als er later vragen bijkomen of weggaan.
"""

""" VOORBEELD:
Hint: Tussen 3 en 5
Wat is 2+2? 4
Correct! Je verdient €200.

Hint: denk aan 'for' en 'while'
Hoe kan je code meermaals herhalen? if
Fout! Het juiste antwoord is loops

Welk datatype stelt een kommagetal voor? float
Correct! Je verdient €400.

De quiz is afgelopen. Je hebt €600 gewonnen!
"""
gewonnen_geld = 0
quiz = [
    {"vraag":"Wat is 2+2?", "antwoord":"4", "geld":200, "hint":"Tussen 3 en 5"},
    {"vraag":"Hoe kan je code meermaals herhalen?", "antwoord":"loops", "geld":300, "hint":"Denk aan 'for' en 'while'"},
    {"vraag":"Welk datatype stelt een kommagetal voor?", "antwoord":"float", "geld":400},
]
for vraag in quiz:
    if "hint" in vraag:
        print(f"Hint: {vraag["hint"]}")
    antwoord = input(f"{vraag["vraag"]}")
    if antwoord == vraag["antwoord"]:
        print(f"Correct! Je verdient {vraag["geld"]}")
        gewonnen_geld += vraag["geld"]
    else:
        print(f"Fout!, het juiste antwoord is {vraag['antwoord']}")
    print("----------------------------------------------")
print(gewonnen_geld)