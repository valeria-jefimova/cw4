from json_vacancy_repository import JsonVacancyRepository
from vacancy import Vacancy


def run_console_interface():
    repo = ('vacancies.json')

    while True:
        print('Выберите действие:')
        print('1. Добавить вакансию')
        print('2. Просмотреть список вакансий')
        print('3. Фильтровать вакансии')
        print('4. Удалить вакансию')
        print('5. Выход')

        choice = input()

        if choice == '1':
            print('Введите информацию о вакансии:')
            title = input('Название вакансии: ')
            url = input('Ссылка на вакансию: ')
            salary = input('Зарплата: ')
            description = input('Описание: ')
            platform = input('Платформа: ')

            vacancy = Vacancy(title, url, salary, description, platform)
            repo.add_vacancy(vacancy)

            print('Вакансия добавлена')
            print()

        elif choice == '2':
            vacancies = repo.get_all_vacancies()

            if not vacancies:
                print('Список вакансий пуст')
                print()
            else:
                for vacancy in vacancies:
                    vacancy.print_info()

        elif choice == '3':
            print('Введите критерии фильтрации:')
            platform = input('Платформа: ')
            min_salary = input('Минимальная зарплата: ')

            filtered_vacancies = repo.filter_vacancies(platform, min_salary)

            if not filtered_vacancies:
                print('Нет вакансий, удовлетворяющих заданным критериям')
                print()
            else:
                for vacancy in filtered_vacancies:
                    vacancy.print_info()

        elif choice == '4':
            url = input('Введите ссылку на вакансию, которую нужно удалить: ')
            repo.delete_vacancy(url)

            print('Вакансия удалена')
            print()

        elif choice == '5':
            print('До свидания!')
            break

        else:
            print('Неверный выбор, попробуйте снова')
            print()
