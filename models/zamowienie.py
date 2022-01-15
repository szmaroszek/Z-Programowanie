class Zamowienie:
    def __init__(self, diet_list: list = None, dietetyk: object = None, pacjent: object = None, placowka: str = None) -> None:
        self._diet_list = diet_list
        self._dietetyk = dietetyk
        self._pacjent = pacjent
        self._placowka = placowka

    def __str__(self) -> str:
        return f"--- ZAMÓWIENIE ---\nPacjent: {self._pacjent},\nDietetyk: {self._dietetyk},\ndiety: {[dieta._name for dieta in self._diet_list]},\nplacówka: {self._placowka}."

    def get_value(self) -> float:
        value = 0
        for diet in self._diet_list:
            value += diet._price
        return round(value, 2)


    def get_kcal(self) -> int:
        value = 0
        for diet in self._diet_list:
            value += diet._kcal
        return value

    @property
    def zamowienie_diet_list(self) -> list:
        return self._diet_list
    
    @zamowienie_diet_list.setter
    def zamowienie_diet_list(self, val: list):
        self._diet_list = val

    @property
    def zamowienie_dietetyk(self) -> object:
        return self._dietetyk
    
    @zamowienie_dietetyk.setter
    def zamowienie_dietetyk(self, val: object):
        self._dietetyk = val

    @property
    def zamowienie_pacjent(self) -> object:
        return self._pacjent
    
    @zamowienie_pacjent.setter
    def zamowienie_pacjent(self, val: object):
        self._pacjent = val

    @property
    def zamowienie_placowka(self) -> list:
        return self._placowka
    
    @zamowienie_placowka.setter
    def zamowienie_placowka(self, val: list):
        self._placowka = val
