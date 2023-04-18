
# Создание экземпляра класса для работы с API сайтов с вакансиями
from json_vacancy_repository import JsonVacancyRepository
from vacancy import Vacancy

hh_api = 'https://api.hh.ru/vacancies'
superjob_api = "https://api.superjob.ru/2.0/vacancies/"

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies("Python", "Москва")
superjob_vacancies = superjob_api.get_vacancies("Python")

# Создание экземпляра класса для работы с вакансиями
vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
json_saver = JsonVacancyRepository()
json_saver.add_vacancy(vacancy)
json_saver.get_vacancies("100 000-150 000 руб.")
json_saver.delete_vacancy(vacancy)


if __name__ == "__main__":
    user_interaction()
