class Property:
    def __init__(self, area: str, rooms: int, price: float, adress: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = adress


class House(Property):
    def __init__(self, area, rooms, price, adress, plot: int):
        super().__init__(area, rooms, price, adress)
        self.plot = plot

    def __str__(self):
        return (f'House located in {self.area} area, {self.rooms} rooms, ' +
                f'{self.plot} m^2, for a price of ${self.price} USD.\n')


class Flat(Property):
    def __init__(self, area, rooms, price, adress, floor):
        super().__init__(area, rooms, price, adress)
        self.floor = floor

    def __str__(self):
        return (f'Flat located in {self.area} area, {self.rooms} rooms ' +
                f'on floor: {self.floor}, for a price of ${self.price} USD.\n')


house_1 = House('Bay', 5, 119000.0, "5th Street, Los Angeles", 100)
flat_1 = Flat('Center', 3, 219000.0, "15th Street, Los Angeles", 50)

print(house_1)
print(flat_1)
