""" Voorbeelden (API geeft enkel Engelse zinnen terug):

Advies 1:
    Input || Topic for advice: spiders
    Print || Remember that spiders are more afraid of you, than you are of them.
Advies 2:
    Input || Topic for advice: teeth
    Print || You don't need to floss all of your teeth. Only the ones you want to keep.
Advies 3:
    Input || Topic for advice: programming
    Print || No advice slips found matching that search term.

"""

"""
Maak een script om advies te geven over een onderwerp. 
Je zult voor deze oefening gebruik maken van de API "adviceslip" (zie verder).

Dit script vraagt de gebruiker naar een onderwerp.  
Het script zal bij de API https://api.adviceslip.com/ aankloppen om te vragen welk advies deze heeft over dit onderwerp. 
Vervolgens print het script het verkregen advies.

Hou met volgende zaken rekening:
	• Het is mogelijk dat de API geen advies heeft over het onderwerp. 
Print in dit geval de zin: "No advice slips found matching that search term." .
	• Hiernaast kan de API ook meer dan 1 advies geven over het onderwerp.
Print in dit geval enkel het eerste advies in de lijst.

Maak voor dit script gebruik van de API: https://api.adviceslip.com/ .
Alle informatie is op deze pagina terug te vinden. Je zal dus zelf moeten bepalen welk endpoint je gebruikt, en hoe deze werkt.
"""