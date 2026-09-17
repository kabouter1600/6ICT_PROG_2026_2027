# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}

# niveau 1:
wanted_fruit = input("Geef een fruit. ")
if wanted_fruit in fruitmand:
    print(f"de waarde van {wanted_fruit} is {fruitmand[wanted_fruit]}")
# niveau 2:
else:
    print("dit zit niet in de fruitmand")
