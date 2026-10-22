# Maak voor deze oefen mee gebruik van onderstaande dictionary-structuur.
inception_film = {
    'jaar': 2010,
    'genre': ['Actie', 'Sciencefiction', 'Thriller'],
    'cast': [ 
        {'acteur': 'Leonardo DiCaprio', 'rol': 'Cobb'},
        {'acteur': 'Joseph Gordon-Levitt', 'rol': 'Arthur'},
        {'acteur': 'Ellen Page', 'rol': 'Ariadne'},
        
    ],
    'locaties': ['Parijs', 'Los Angeles', 'Tokio'],
    'box_office': {'budget': 160000000, 'opbrengst': 829895144},
    'awards': {'Oscars': 0, 'Golden Globes': 4}
}
# niveau 1 = dictonairy en 3
# niveau 2
print(inception_film["jaar"])  
print(inception_film["genre"][1])
print(inception_film['box_office']["opbrengst"])
inception_film['awards']["Oscars"] = 4
# niveau 3
print(inception_film['awards']["Oscars"])
# niveau 4
inception_film['regisseur'] = 'Christopher Nolan'
inception_film['cast'].append({'acteur': 'Ellen Page', 'rol': 'Ariadne'})
print(inception_film)
