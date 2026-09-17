# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
stad = input("In welke stad bent u" )
if stad in steden_temp:
    graden = steden_temp[stad]
else:
    graden = "???"
print(f"Het is {graden}°C op dit moment")