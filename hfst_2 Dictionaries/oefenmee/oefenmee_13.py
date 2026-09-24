# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appels": 2,
    "bananen": 3,
    "kersen": 10,
    "mango's": 1
}
for fruit, aantal in fruitmand.items():
    bijkopen = int(input(f"hoevel {fruit} wilt u bijkopen(op dit moment heb u er {aantal}) "))
    fruitmand[fruit] += bijkopen

for fruit, hoeveel in fruitmand.items():
    print(f"er zitten {hoeveel, fruit} in de fruitmand")