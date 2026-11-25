import requests, json

url = "https://api.adviceslip.com/advice/search/api"
response_json = requests.get(url).json()
advice = response_json["slips"][0]["advice"]
with open("hfst_4 API\jasonbestanden\dviceslip_data.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")
# niveau 2
#[slip][advice]
    print("Hier is wat wijsheid over API's...")
    print(advice)