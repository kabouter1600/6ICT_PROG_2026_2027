# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}

# #niveau 1:
# fruit = "banaan"
# print( fruitmand[fruit] )

# print de waarde van banaan (3)

# niveau 2:
# nieuw_fruit  = "mango"
# nieuw_aantal = 1
# fruitmand[nieuw_fruit] = nieuw_aantal
# print(fruitmand)

# niveau 3:
# fruit = "banaan"
# nieuw_aantal = 8
# fruitmand[fruit] = nieuw_aantal
# print(fruitmand)

# niveau 4:
# fruit = "kers"
# verlaag_met = 43
# fruitmand[fruit] -= verlaag_met
# print(fruitmand)

# niveau 5:
terugleggen_fruit = "kers"
fruitmand.pop(terugleggen_fruit)
print(fruitmand)