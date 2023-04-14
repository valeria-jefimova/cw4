
import requests

url = 'https://api.hh.ru/vacancies'
params = {
    'text': 'Python разработчик',  # поиск по ключевым словам
    'area': '1',  # поиск по городу (Москва)
    'period': '30',  # период публикации вакансии (30 дней)
    'per_page': '100'  # количество результатов на страницу (максимум 100)
}
response = requests.get(url, params=params)
vacancies = response.json()['items']
"""
После выполнения запроса мы получаем список словарей 
с информацией о вакансиях в переменной vacancies.
"""


"""
Это условие проверяет, был ли успешный ответ от сервера
"""
if response.status_code == 200:
    vacancies = response.json()
    print(vacancies)
else:
    print(f'Request failed with error {response.status_code}: {response.text}')
