""" Oefening 1 (  / 4)
Er is een beveiligingsinbreuk vastgesteld in ons systeem. Uit voorzorg
zal de IT-afdeling de wachtwoorden van een specifieke groep wijzigen. 

Het gaat om alle gebruikers waarvan de gebruikersnaam GEEN punt ('.') bevat.
Pas de wachtwoorden van deze accounts aan. Zet een ! achter hun huidig wachtwoord.
Print op het einde de gewijzigde dictionary, en hoevaak je een wachtwoord hebt gewijzigd.

BELANGRIJK:
De code moet ook werken als de dictionary later uitgebreid wordt.
Doe maar alsof er duizenden gebruikers in de dictionary staan.
"""
# gebruikers = {
#     'hendrik.clijsters': 'SteDri39',
#     'spma300906': 'MauSpi21',
#     'bija080714': 'BirJal08',
#     'johan.colson': 'ColHan44',
#     'momo250308': 'SerRam26'
# }


# """ VERWACHTE OUTPUT NA OVERLOPEN DICTIONARY:
# -------------------------------------------------------------------------------
# {'hendrik.clijsters': 'SteDri39', 
#  'spma300906': 'MauSpi21!',         --> GEWIJZIGD
#  'bija080714': 'BirJal08!',         --> GEWIJZIGD
#  'johan.colson': 'ColHan44',        
#  'momo250308': 'SerRam26!'          --> GEWIJZIGD
# }
# Aantal gewijzigde wachtwoorden: 3
# -------------------------------------------------------------------------------
# """
# aantal_keer_gewijzigd = 0
# for gebruiker, wachtwoord in gebruikers.items():
#     if "." not in gebruiker:
#         gebruikers[gebruiker] = wachtwoord + "!"
#         aantal_keer_gewijzigd += 1
# print(gebruikers)
# print(aantal_keer_gewijzigd)

""" Oefening 2 (  / 6)
Het kassasysteem van een bistro houdt de openstaande rekeningen per tafel bij.
In deze oefening ga je bestellingen toevoegen of tafels laten afrekenen.

Herhaal het volgende tot de gebruiker 'STOP' ingeeft bij de tafelnaam:
    - Vraag naar de tafelnaam (bv. 'Tafel 1').
    - Vraag welke actie de kelner wil uitvoeren: 'bestellen' of 'afrekenen'.

bestellen:
    - Vraag naar het bedrag van de nieuwe bestelling.
    - Als de tafel AL bestaat: tel het bedrag op bij de huidige rekening.
    - Als de tafel NOG NIET bestaat: voeg de tafel toe met dit bedrag.
    - Print de nieuwe totale rekening voor deze tafel.

afrekenen:        
    - Als de tafel AL bestaat: verwijder de tafel uit de dictionary met .pop()
      en print het totaal afgerekende bedrag.
    - Als de tafel NOG NIET bestaat: print een foutmelding dat er geen 
      openstaande rekening is voor deze tafel.

Print na het stoppen van de loop een overzicht van alle nog openstaande tafels.
"""

tafels = {
    'Tafel 1': 45.50,
    'Tafel 3': 22.00,
    'Tafel 4': 87.10
}


""" VOORBEELD:
-------------------------------------------------------------------------------
Voer tafelnaam in: Tafel 1
Welke actie ('bestellen' of 'afrekenen')? bestellen
Voer het bedrag in: 12.50
Nieuw totaal voor Tafel 1: €58.0

Voer tafelnaam in: Tafel 3
Welke actie ('bestellen' of 'afrekenen')? afrekenen
Tafel 3 heeft €22.0 afgerekend en is nu vrij.

Voer tafelnaam in: Tafel 2
Welke actie ('bestellen' of 'afrekenen')? afrekenen
Fout: Tafel 2 heeft geen openstaande rekening!

Voer tafelnaam in: STOP

Nog openstaande rekeningen:
{'Tafel 1': 58.0, 'Tafel 4': 87.1}
-------------------------------------------------------------------------------
"""
while True:
    tafel = input("welke tafel is het? ")
    if tafel == "stop":
        break
    else:
        wat_doen = input("wilt u bestellen of afrekenen? ")
        if wat_doen == "bestellen":
            bedrag_bestellen = float(input("wat is het bedrag van de bestelling? "))
            if tafel in tafels.keys():
                for tafelnummer, bedrag in tafels.items():
                    if tafelnummer == tafel:
                        bedrag += bedrag_bestellen
                        print(f"nieuw totaal is {bedrag}")
            else:
                tafels[tafel] = bedrag_bestellen
                print(f"{tafel} is aangemaakt met als prijs {bedrag_bestellen}")
        if wat_doen == "afrekenen":
            if tafel in tafels.keys():
                print(f"{tafel} heeft afgerekend deze is nu vrij")
            else:
                print("deze tafel bestaat nog niet")





            