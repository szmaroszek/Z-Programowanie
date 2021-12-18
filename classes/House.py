from classes.Property import Property

class House(Property):
    def __init__(self, area, rooms, price, adress, plot: int):
        super().__init__(area, rooms, price, adress)
        self.plot = plot

    def __str__(self):
        return (f'House located in {self.area} area, {self.rooms} rooms, ' +
                f'{self.plot} m^2, for a price of ${self.price} USD.\n')
