from models.person import Person

class Dietetyk(Person):
    def __init__(self, name: str, surname: str, age: int, sex: str, degree: str, specialization: str) -> None:
        super().__init__(name, surname, age, sex)
        self._degree = degree
        self._specialization = specialization


    def __str__(self) -> str:
        return super().__str__() + f" Eductation: {self.person_degree}, specialization: {self.person_specialization} field."


    @property
    def person_degree(self) -> str:
        return self._degree
    
    @person_degree.setter
    def person_degree(self, val: str):
        self._degree = val

    @property
    def person_specialization(self) -> str:
        return self._specialization
    
    @person_specialization.setter
    def person_specialization(self, val: str):
        self._specialization = val
