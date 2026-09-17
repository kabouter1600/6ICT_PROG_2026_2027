# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
naam = ""
while naam != "stop":
    naam = input("geef uw naam"  )
    if naam in gasten:
        job = gasten[naam]
        print(f"welkom {job} {naam}, Kom binnen")
        gasten.pop(naam)
    else:
        print("u staat niet op de lijst")

