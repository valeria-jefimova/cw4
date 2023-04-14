import json
from typing import List
from vacancy import Vacancy
from vacancy_repository import VacancyRepository


class JsonVacancyRepository(VacancyRepository):
    """
    Предназначен для сохранения информации о вакансиях в формате JSON в файле
    и для выполнения операций с данными в этом файле.
    Он наследуется от абстрактного класса VacancyRepository
    и реализует его абстрактные методы.
    """
    def __init__(self, file_path: str):
        """
        Инициализирует объект класса и открывает файл для работы
        """
        self.file_path = file_path

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавляет вакансию в файл
        :param vacancy:
        """
        with open(self.file_path, 'r') as f:
            """
            Для чтения из файла используется метод load
            """
            data = json.load(f)

        data.append({
            'name': vacancy.name,
            'url': vacancy.url,
            'salary': vacancy.salary,
            'description': vacancy.description,
            'platform': vacancy.platform
        })

        with open(self.file_path, 'w') as f:
            """
            Для сохранения вакансий в файл используется метод dump из этой библиотеки
            """
            json.dump(data, f)

    def get_vacancies(self, platform: str, salary: int = None, keywords: List[str] = None) -> List[Vacancy]:
        """
        Получает список вакансий из файла
        :param platform:
        :param salary:
        :param keywords:
        :return:
        """
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        result = []
        for item in data:
            if item['platform'] == platform:
                if salary is not None and item['salary'] is not None and item['salary'] >= salary:
                    result.append(Vacancy(
                        name=item['name'],
                        url=item['url'],
                        salary=item['salary'],
                        description=item['description'],
                        platform=item['platform']
                    ))
                elif keywords is not None and all(kw in item['description'] for kw in keywords):
                    result.append(Vacancy(
                        name=item['name'],
                        url=item['url'],
                        salary=item['salary'],
                        description=item['description'],
                        platform=item['platform']
                    ))

        return result

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаляет вакансию из файла
        :param vacancy:
        """
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        data = [item for item in data if item['name'] != vacancy.name and item['url'] != vacancy.url]

        with open(self.file_path, 'w') as f:
            json.dump(data, f)
