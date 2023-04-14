
from abc import ABC, abstractmethod
from typing import List
from vacancy import Vacancy


class VacancyRepository(ABC):
    """
    Класс VacancyRepository является наследником ABC,
    что делает его абстрактным и невозможным для инициализации.
    """
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Метод add_vacancy принимает объект вакансии и добавляет его в хранилище.
        :param vacancy:
        """
        pass

    @abstractmethod
    def get_vacancies(self, platform: str, salary: int = None, keywords: List[str] = None) -> List[Vacancy]:
        """
        Метод get_vacancies возвращает список вакансий из хранилища
        :param platform:
        :param salary:
        :param keywords:
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Метод delete_vacancy удаляет вакансию из хранилища по её ID.
        :param vacancy:
        """
        pass
