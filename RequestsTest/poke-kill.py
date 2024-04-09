import requests

URL = 'https://api.pokemonbattle.me'

TOKEN = '3b5e3e238fe20cac8ae283609f13a783'

HEADERS = {
    'Content-Type' : 'application/json',
    'trainer_token': TOKEN          
}

body = {
    "pokemon_id": "16977"
}

response = requests.post(url=f'{URL}/v2/pokemons/knockout', headers = HEADERS, json=body)
print(response.json())