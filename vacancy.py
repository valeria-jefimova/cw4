
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
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description
        self.platform = platform

    def __repr__(self):
        """
        Метод repr для представления объекта в строковом виде.
        :return:
        """
        return f"Vacancy({self.title}, {self.link}, {self.salary}, {self.description}, {self.platform})"

    def __str__(self):
        return f"{self.title} ({self.platform}): {self.salary}\n{self.description}\n{self.link}\n"

    def __eq__(self, other):
        """
        Метод eq для сравнения вакансий по зарплате
        """
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other):
        """
        Метод lt для сравнения вакансий в порядке возрастания зарплаты
        :param other:
        :return:
        """
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __gt__(self, other):
        """
        Метод gt позволяет сравнивать вакансии по зарплате (если у обеих вакансий указана зарплата)
        :param other:
        :return:
        """
        if self.salary is None or other.salary is None:
            return False
        return self.salary > other.salary

    def display_info(self):
        """
        Метод display_info для вывода информации о вакансии на экран
        """
        print(f"Title: {self.title}")
        print(f"Link: {self.link}")
        print(f"Salary: {self.salary}")
        print(f"Description: {self.description}")
        print(f"Platform: {self.platform}")
