class Vacancy:
    """
    Этот класс имеет пять атрибутов:
    название вакансии (title),
    ссылку на вакансию (link),
    зарплату (salary),
    краткое описание (description)
    и название платформы (platform).
    """

    def __init__(self, title, link, salary, description, platform):
        self.__title = title
        self.__link = link
        self.__salary = salary
        self.__description = description
        self.__platform = platform

    @property
    def title(self):
        return self.__title

    @property
    def link(self):
        return self.__link

    @property
    def salary(self):
        return self.__salary

    @property
    def description(self):
        return self.__description

    @property
    def platform(self):
        return self.__platform

    def __repr__(self):
        """
        Метод repr для представления объекта в строковом виде.
        :return:
        """
        return f"Vacancy({self.__title}, {self.__link}, {self.__salary}, {self.__description}, {self.__platform})"

    def __str__(self):
        return f"{self.__title} ({self.__platform}): {self.__salary}\n{self.__description}\n{self.__link}\n"

    def __eq__(self, other):
        """
        Метод eq для сравнения вакансий по зарплате
        """
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.__salary == other.__salary

    def __lt__(self, other):
        """
        Метод lt для сравнения вакансий в порядке возрастания зарплаты
        :param other:
        :return:
        """
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.__salary < other.__salary

    def __gt__(self, other):
        """
        Метод gt позволяет сравнивать вакансии по зарплате (если у обеих вакансий указана зарплата)
        :param other:
        :return:
        """
        if self.__salary is None or other.salary is None:
            return False
        return self.__salary > other.salary

    def _validate_title(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Некорректное название вакансии")
        return title

    def _validate_link(self, link):
        if not isinstance(link, str) or len(link) == 0:
            raise ValueError("Некорректная ссылка на вакансию")
        return link

    def _validate_salary(self, salary):
        if not isinstance(salary, (int, float)):
            raise ValueError("Зарплата должна быть числом")
        return salary

    def _validate_description(self, description):
        if not isinstance(description, str) or len(description) == 0:
            raise ValueError("Некорректное описание вакансии")
        return description

    def display_info(self):
        """
        Метод display_info для вывода информации о вакансии на экран
        """
        print(f"Title: {self.__title}")
        print(f"Link: {self.__link}")
        print(f"Salary: {self.__salary}")
        print(f"Description: {self.__description}")
