# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}
aantal_personen = int(input("voor hoeveel personen kookt u? "))
for ingredient_1, waarde_1 in recept.items():
    recept[ingredient_1] /= 4
    recept[ingredient_1] *= aantal_personen

print("Recept voor worst met wortelen een erwten")
for ingredient_2, waarde_2 in recept.items():
    print(f"-{ingredient_2}: {waarde_2}gr")