import requests
import pytest

URL = 'https://api.pokemonbattle.me'
TOKEN = '3b5e3e238fe20cac8ae283609f13a783'
HEADERS = {
    'Content-Type' : 'application/json',
    'trainer_token': TOKEN          
}

def test_status_code ():
    responce = requests.get(url = f'{URL}/v2/trainers',params = {'trainer_id' : 2644})
    assert responce.status_code == 200

def test_part_of_responce():
    responce = requests.get(url = f'{URL}/v2/trainers',params = {'trainer_id' : 2644})
    assert responce.json(),['data'][0]['trainer_name'] == 'Slavoncha'

