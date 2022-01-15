class Dieta:
    def __init__(self, name: str, diet_type: str, kcal: int, price: float) -> None:
        self._name = name
        self._diet_type = diet_type
        self._kcal = kcal
        self._price = price
    

    def __str__(self) -> str:
        return f"Diet name: {self.diet_name}, diet type: {self.diet_diet_type}, kcal: {self.diet_kcal}, number of price: {self.diet_price} PLN."


    @property
    def diet_name(self) -> str:
        return self._name
    
    @diet_name.setter
    def diet_name(self, val: str):
        self._name = val

    @property
    def diet_diet_type(self) -> str:
        return self._diet_type
    
    @diet_diet_type.setter
    def diet_diet_type(self, val: str):
        self._diet_type = val

    @property
    def diet_kcal(self) -> int:
        return self._kcal
    
    @diet_kcal.setter
    def diet_kcal(self, val: int):
        self._kcal = val

    @property
    def diet_price(self) -> float:
        return self._price
    
    @diet_price.setter
    def diet_price(self, val: float):
        self._price = val
        