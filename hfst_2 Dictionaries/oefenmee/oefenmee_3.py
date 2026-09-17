# Start de oefen mee met onderstaande dictionary.
persoonsinfo = { # info over een persoon
    "naam": "Jan",
    "leeftijd": 32,
    "massa": 79
}
# niveau 1:
# print(f"{persoonsinfo['naam']} is {persoonsinfo['leeftijd']} jaar oud")

# niveau 2:
print( len( persoonsinfo ) )
# hoeveel waardes in de dictonary staan

# niveau 3:
oogkleur = persoonsinfo["oogkleur"]
print(f"Deze persoon heeft {oogkleur} ogen.")
# oogkleur staat niet in de dictionary

# niveau 4:
naam = "Jan"
print(persoonsinfo[naam])
# omdat de naam een waarde is.
