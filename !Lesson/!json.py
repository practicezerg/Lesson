import requests
from pprint import pprint

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
url = "https://pokeapi.co/api/v2/pokemon/"
req = requests.get(url, headers=headers).json()
pprint(req)
for i in req["results"]:
    print(i["name"])


