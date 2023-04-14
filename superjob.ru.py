
import requests

url = 'https://api.superjob.ru/2.0/vacancies/'

params = {
    'town': 'Москва',
    'payment_from': 100000,
    'catalogues': 33,
    'count': 100,
    'page': 0,
    'period': 7
}

headers = {
    'X-Api-App-Id': 'ваш API-ключ',
    'Content-Type': 'application/json'
}

response = requests.get(url, params=params, headers=headers)
