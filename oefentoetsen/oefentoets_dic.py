# """ OEFENING 1 (  / 3)
# Gegeven is een grote datastructuur over de band Queen.
# Los de vragen onder deze datastructuur op.

# Je moet voor iedere vraag springen in de datastructuur!
# """

# band = {
#     "algemene_info": {
#         "naam": "Queen",
#         "opgericht": 1970,
#         "leden": [
#             {
#                 "naam": "Freddie Mercury",
#                 "rol": "zanger",
#                 "instrumenten": ["zang", "piano"],
#                 "liedjes": [
#                     {"titel": "Bohemian Rhapsody", "jaar": 1975, "album": "A Night at the Opera"},
#                     {"titel": "Don't Stop Me Now", "jaar": 1978, "album": "Jazz"}
#                 ]
#             },
#             {
#                 "naam": "Brian May",
#                 "rol": "gitarist",
#                 "instrumenten": ["gitaar", "zang"],
#                 "liedjes": [
#                     {"titel": "We Will Rock You", "jaar": 1977, "album": "News of the World"}
#                 ]
#             },
#             {
#                 "naam": "Roger Taylor",
#                 "rol": "zanger",
#                 "instrumenten": ["drums", "bass"],
#                 "liedjes": [
#                     {"titel": "Radio Ga Ga", "jaar": 1984, "album": "The Works"}
#                 ]
#             }
#         ]
#     },
#     "awards": ["Brit Award", "Grammy Lifetime Achievement Award", "Best Song of All Time"],
#     "tour": {
#         "naam": "A Night at the Opera Tour", 
#         "jaar": 1975, 
#         "locaties": ["Londen", "New York", "Tokyo"]
#     }
# }

# Vraag 1: print de award "Best Song of All Time" door in de structuur te springen. (0.5)
# print(band["awards"][2])
# Vraag 2: Voeg "Sydney" toe aan de locaties waar hun toer is doorgegaan. (0.5)
# band["tour"]["locaties"].append("sydney")
# print(band["tour"])
# # Vraag 3: Wijzig de rol van Roger Taylor naar "drummer". (0.5)
# band["algemene_info"]["leden"][2]["rol"] = "drummer"
# print(band["algemene_info"]["leden"][2])
# Vraag 4: print alle awards die de band behaald heeft. Gebruik hiervoor de for-loop. (0.5)
# for award in band["awards"]:
#     print(award)
# Vraag 5: Print de titel van ieder liedje in de datastructuur. Gebruik hiervoor de for-loop. (1)
#          !! Opgelet: dit is een lastige vraag !!
# for index, lid in enumerate(band["algemene_info"]['leden']):
#     for lied in lid['liedjes']:
#         print(lied['titel'])

""" OEFENING 2 (  / 2)
Onderstaande structuur bevat score/level behaald in het spel brickbreaker voor meerdere personen.

Print de naam van de speler met de hoogste score. Op het moment is dit Jan.
De code moet correct blijven werken, ook als er in de toekomst iemand anders een hogere score haalt.
Je kan dit zelf testen door de scores in de datastructuur aan te passen.
"""
# hoogste_score = 0
# index_hoogste_score = 0
# brickbreaker = [
#     {"speler": "Eva", "score": 1500, "level": 5},
#     {"speler": "Jan", "score": 2300, "level": 7},
#     {"speler": "Lotte", "score": 1800, "level": 6},
#     {"speler": "Pieter", "score": 900, "level": 3},
#     {"speler": "Sofie", "score": 2000, "level": 7},
# ]
# for index, persoon in enumerate(brickbreaker):
#     if hoogste_score < brickbreaker[index]['score']:
#         hoogste_score = brickbreaker[index]['score']
#         index_hoogste_score = index
# print(f"{brickbreaker[index_hoogste_score]["speler"]} heeft de hoogste score")
""" OEFENING 3 (  / 5)
Onderstaande datastructuur is een vereenvoudigde weergave van het asset-management binnen de school.

De sleutel van de hoofd-dictionary is het SPB-nummer van de asset.
De waarde is een sub-dictionary met erin volgende informatie:
    - serial         (verplicht, altijd ingevuld)
    - categorie      (optioneel, kan None zijn als de asset niet in een categorie geplaatst is)
    - toegewezen_aan (optioneel, komt niet voor als de asset niet toegewezen is)

Maak een overzicht van alle assets die toegewezen zijn aan een bepaalde gebruiker (naam_gebruiker). 
Voor elk toegewezen asset moet je volgende informatie printen:
    - SPB-nummer
    - Serial
    - Categorie (alleen als deze niet None is)
Print tenslotte het totaal aantal assets dat aan deze gebruiker is toegewezen.

De code moet correct blijven werken als er in de toekomst meer assets worden toegevoegd of gewijzigd.
"""

""" VOORBEELD (naam_gebruiker = jan.janssen)
Overzicht van assets toegewezen aan jan.janssen...
    - spb2021-098817 met serial 5CD133BZBC en categorie Huur100
    - spb2021-100101 met serial 5CD133FEED
Totaal aantal toegewezen assets: 2
"""

assets = {
    "spb2021-098817": {
        "serial": "5CD133BZBC",
        "categorie": "Huur100",
        "toegewezen_aan": "jan.janssen"
    },
    "spb2023-092814": {
        "serial": "5CD235BZBC",
        "categorie": "Overgekocht",
        "toegewezen_aan": "piet.pieters"
    },
    "spb2022-043299": {
        "serial": "5CD183BADC",
        "categorie": "Huur100",
    },
    "spb2021-100101": {
        "serial": "5CD133FEED",
        "categorie": None,
        "toegewezen_aan": "jan.janssen"
    },
}

naam_gebruiker = "jan.janssen"
teller = 0
for asset, info in assets.items():
    for waarde, gegeven in info.items():
        if gegeven == naam_gebruiker:
            teller += 1
            print(asset)
            toegewezen = asset
    if toegewezen == asset:
        if assets[toegewezen]["categorie"] != None:
            print(f"- {asset} met als serial {assets[toegewezen]["serial"]} en met categorie {assets[toegewezen]["categorie"]}")
        else:
            print(f"- {asset} met als serial {assets[toegewezen]["serial"]}")
print(f"totaal aantal keren toegewezen assets:{teller}")
