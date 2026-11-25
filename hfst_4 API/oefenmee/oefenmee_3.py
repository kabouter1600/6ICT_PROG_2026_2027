import requests, json

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
response_json = response.json()
# niveau 2
with open("hfst_4 API\jasonbestanden\chucknorris_data.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")
# niveau 1
# omdat je geen locatie hebt gegeven waar deze map moet aangemaakt moet worden

# niveau 3
# hij verwijderd de waarde en maakt geen nieuwe aan