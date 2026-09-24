""" Oefening 1 (  / 3)
De dictionary 'voorraad' stelt de voorraad van een snackbar voor.
In deze oefening zal je een overzicht opstellen van deze voorraad.

Print een overzicht van de snacks in deze dictionary. Iedere snack moet op een nieuwe lijn staan.
Print tenslotte ook hoeveel snacks er in totaal in de snackbar aanwezig zijn.
Zie onderstaand voorbeeld voor een mogelijke opbouw van dit overzicht.
De code moet blijven werken, ook als de voorraad van de snackbar later wijzigt.
"""

""" VOORBEELD
De snackbar heeft volgende snacks op voorraad...
    - burgers: 12
    - loempias: 8
    - frikandellen: 5
In totaal heeft de snackbar 25 snacks.
# """

# voorraad = {
#     "burgers": 12,
#     "loempias": 8,
#     "frikandellen": 5
# }

# """ PUNTENVERDELING:
#     - Overlopen elementen: 1
#     - Ieder element correct geformatteerd printen: 1
#     - Totaal van elementen op laaste regel printen: 1
# """
# aantal_snacks = 0
# print("De volgende snacks zijn op voorraad")
# for snack, aantal in voorraad.items():
#     print(f"-{snack}: {aantal}")
#     aantal_snacks += aantal
# print(f"in totaal zijn er {aantal_snacks} snacks")

""" Oefening 2 (  / 7)
De dictionary 'voorraad' stelt de voorraad van een snackbar voor.
In deze oefening zal je de aantallen en snacks in deze voorraad wijzigen.

Herhaal het volgende tot in het oneindige.
    - Vraag de gebruiker naar een snack.
    - Vraag de gebruiker hoeveel van de snack hij wilt verkopen/aankopen.
        * verkopen = negatief getal || aankopen = positief getal
    - Wijzig de snack in de dictionary voorraad met de opgegeven hoeveelheid.
    - Print hoeveel van deze snack er na de wijziging in de dictionary voorraad zitten.

Het herhalen moet stoppen wanneer de gebruiker 'STOP' invult in plaats van een snack.
Print tenslotte de bekomen dictionary (je mag hiervoor de code uit oef 1 gebruiken).

Hou rekening met volgende drie regels:
    1. Het product bestaat al in de dictionary.
        * Wijzig dan het aantal in de voorraad.
    2. Het product bestaat NIET in de dictionary. 
        * Voeg de snack dan toe als nieuw element samen met de aangekochte hoeveelheid.
    3. Het aantal snacks mag NOOIT kleiner worden dan 0.
        * Print enkel een foutmelding en wijzig niets aan de dictionary voorraad.
"""

""" VOORBEELD 

** REGEL 1: product bestaat al. **
>>> Kies een product: burgers
>>> Hoeveel stuks (negatief = verkoop, positief = aankoop): -5
Er zijn nu 7 burgers in voorraad.

** REGEL 2: product bestaat niet. **
>>> Kies een product: mexicanos
>>> Hoeveel stuks (negatief = verkoop, positief = aankoop): 6
Er zijn nu 6 mexicanos in voorraad.

** REGEL 3: aantal NOOIT kleiner dan 0. **
>>> Kies een product: loempias
>>> Hoeveel stuks (negatief = verkoop, positief = aankoop): -20
Fout! Er zijn slechts 8 loempias in voorraad. Voorraad wordt niet gewijzigd.

** STOPPEN VAN CODE **
>>> Kies een product: STOP
De snackbar heeft volgende snacks op voorraad...
    - burgers: 7
    - loempias: 8
    - frikandellen: 5
    - mexicanos: 6
"""

""" PUNTENVERDELING:
    - Oneindige while-loop + manier om uit te breken: 1
    - Vraag naar user-input + omvormen naar int: 1
    - Wijzig bestaand element in dictionary + conditie: 1.5
    - Maak nieuw bestand aan in dictionary + conditie: 1.5
    - Geef foutmelding als aantal van snack negatief wordt + conditie: 1.5
    - Print boodschap na (eventuele wijziging) + print bekomen dictionary: 0.5

"""
snack = ""
stuks = ""
snacklijst = {}
while True:
    snack = input("geef een snack " ) 
    if snack == "stop":
        break
    stuks = int(input("hoeveel stuks " ))
    if stuks <= 0 and snack not in snacklijst:
        print("deze snack kan niet verkocht worden omdat deze niet in de lijst staat")
    else:
        if snack in snacklijst:
            for eten, stuk in snacklijst.items():
                if snack == eten:
                    if stuks < 0:
                        genoeg = stuk + stuks
                        if genoeg < 0:
                            print("niet voldoende snacks om te verkopen")
                        else:
                            snacklijst[eten] = genoeg
                    else:
                        snacklijst[eten] += stuks
        else:
            snacklijst[snack] = stuks
    print("de volgende snacks zitten in de lijst ")
    for snack, aantal in snacklijst.items():
        print(f"-{snack}: {aantal}")