from hh_vacancy_scraper import HHVacancyScraper
from sj_vacancy_scraper import SJVacancyScraper
from vacancy import Vacancy
from json_vacancy_repository import JsonVacancyRepository

if __name__ == '__main__':
    hh_scraper = HHVacancyScraper()
    sj_scraper = SJVacancyScraper()

    hh_vacancies = hh_scraper.get_vacancies()
    sj_vacancies = sj_scraper.get_vacancies()

    all_vacancies = hh_vacancies + sj_vacancies

    vacancy_repository = JsonVacancyRepository()

    for vacancy in all_vacancies:
        vacancy_repository.add_vacancy(vacancy)

    filtered_vacancies = vacancy_repository.get_vacancies_by_salary(100000, 200000)

    for vacancy in filtered_vacancies:
        print(vacancy)

    vacancy_repository.remove_vacancy_by_platform

