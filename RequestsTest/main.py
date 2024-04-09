import requests

URL = 'https://api.pokemonbattle.me'
TOKEN = '3b5e3e238fe20cac8ae283609f13a783'

HEADERS = {
    'Content-Type' : 'application/json',
    'trainer_token': TOKEN          
}

body = {
    'trainer_token': TOKEN,
    'email': 'valedar.kamdil@yandex.ru',
    "password": "EfF-3pz-ZRD-PqF"
}

# создание покемона
body_create = {
    'name': 'generate',
    'photo': 'generate'
}

response_create = requests.post(url=f'{URL}/v2/pokemons', headers = HEADERS, json=body_create)
#print(response_create.json())
print(response_create.json()['id'])

pokemon_id = response_create.json()['id']

# изменить имя покемона
body_change = {
    'pokemon_id': f'{pokemon_id}',
    'name': 'CHANDLER',
    'photo': 'https://dolnikov.ru/pokemons/albums/007.png'
}

response_change = requests.put(url=f'{URL}/v2/pokemons', headers = HEADERS, json=body_change)
print(response_change.json())

# поймать покемона в покебол
body_catch = {'pokemon_id': f"{pokemon_id}"}

response_catch = requests.post(url=f'{URL}/v2/trainers/add_pokeball', headers = HEADERS, json=body_catch)
print(response_catch.json())