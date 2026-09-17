# Start de oefening met onderstaande code.
films = ["godfather", "avatar", "oppenheimer"]
scores = [9, 3, 7.5]

filmscores = {}
for index, film in enumerate(films):
    sleutel = film  # De sleutel is de huidige film.
    score = scores[index]
    waarde = score   # De waarde is de overeenkomstige score.
    filmscores[film] = score
    # Gebruik sleutel/waarde om nieuw dict element te maken.

print(filmscores)
