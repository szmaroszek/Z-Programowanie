class Person:
    def __init__(self, name: str, surname: str, age: int, sex: str) -> None:
        self._name = name
        self._surname = surname
        self._age = age
        self._sex = sex
    

    def __str__(self) -> str:
        return f"{self.person_name} {self.person_surname}, {self.person_sex}, age {self.person_age}"


    @property
    def person_name(self) -> str:
        return self._name
    
    @person_name.setter
    def person_name(self, val: str):
        self._name = val

    @property
    def person_surname(self) -> str:
        return self._surname
    
    @person_surname.setter
    def person_surname(self, val: str):
        self._surname = val

    @property
    def person_age(self) -> str:
        return self._age
    
    @person_age.setter
    def person_age(self, val: str):
        self._age = val

    @property
    def person_sex(self) -> str:
        return self._sex
    
    @person_sex.setter
    def person_sex(self, val: str):
        self._sex = val
 