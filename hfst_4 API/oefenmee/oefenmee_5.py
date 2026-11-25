import requests, json

url = "https://v2.jokeapi.dev/joke/Christmas"
response_json = requests.get(url).json() # Haal JSON uit response.

# Bepaal of de grap uit 1 of 2 delen bestaat.
if ("joke" in response_json):
    print(response_json["joke"])     # De grap
else:
    print(response_json["setup"])    # De setup
    print(response_json["delivery"]) # De punchline
with open("hfst_4 API\jasonbestanden\json_denkt_dat_die_grappig_is.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")
# omdat het een hele lange dictonary is
# https://v2.jokeapi.dev/joke/Christmas
# https://v2.jokeapi.dev/joke/Christmas?amount=3