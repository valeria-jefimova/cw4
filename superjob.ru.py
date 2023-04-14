from sjapi import SJClient

client = SJClient()
vacancies = client.vacancies(keyword='Python', town='Москва')

print(vacancies)
