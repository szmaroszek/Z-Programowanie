from classes.Property import Property

class Flat(Property):
    def __init__(self, area, rooms, price, adress, floor):
        super().__init__(area, rooms, price, adress)
        self.floor = floor

    def __str__(self):
        return (f'Flat located in {self.area} area, {self.rooms} rooms ' +
                f'on floor: {self.floor}, for a price of ${self.price} USD.\n')
