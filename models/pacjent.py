from models.person import Person

class Pacjent(Person):
    def __init__(self, name: str, surname: str, age: int, sex: str, weight: int, height: int):
        super().__init__(name, surname, age, sex)
        self._weight = weight
        self._height = height


    def __str__(self) -> str:
        return super().__str__() + f" weight: {self.person_weight} kg, height: {self.person_height} cm."


    @property
    def person_weight(self) -> str:
        return self._weight
    
    @person_weight.setter
    def person_weight(self, val: str):
        self._weight = val

    @property
    def person_height(self) -> str:
        return self._height
    
    @person_height.setter
    def person_height(self, val: str):
        self._height = val
