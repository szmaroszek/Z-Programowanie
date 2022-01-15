class Test:
    def __init__(self, val):
        self.val = val
        self.__val = val  

    @property
    def get__val(self):
        return self.__val



    @property
    def nazwa_kursu(self) -> str:
        return self._nazwa_kursu

    @nazwa_kursu.setter
    def nazwa_kursu(self, val: str):
        self._nazwa_kursu = val



p1 = Test(10)


print(p1.get__val)