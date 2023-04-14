
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
    'X-Api-App-Id': 'v3.h.4458973.6fdfa2327420abc8efc1e7f9a0a39a0993bce569.1407b0e49c8811e4492f2928b2092c53d560bc7b',
    'Content-Type': 'application/json'
}

response = requests.get(url, params=params, headers=headers)
