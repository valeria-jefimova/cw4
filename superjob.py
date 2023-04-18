
import requests
import json

# Вставьте свой токен вместо YOUR_TOKEN
headers = {'X-Api-App-Id': 'v3.h.4458973.6fdfa2327420abc8efc1e7f9a0a39a0993bce569.1407b0e49c8811e4492f2928b2092c53d560bc7b'}

# Отправляем запрос на получение вакансий по ключевому слову "python"
response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params={'keyword': 'python'})

# Преобразуем ответ в формат JSON
data = json.loads(response.content)

# Сохраняем данные в файл vacancies.json
with open('vacancies.json', 'w') as file:
    json.dump(data, file)

"""
Это условие проверяет, был ли успешный ответ от сервера
"""
if response.status_code == 200:
    vacancies = response.json()
    print(vacancies)
else:
    print(f'Request failed with error {response.status_code}: {response.text}')