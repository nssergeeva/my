class House():
    def __init__(self):
        self.number_of_floors = 0

    def set_new_number_of_floors(self, floor):
        self.number_of_floors = floor
        print(f'Номер этажа: {self.number_of_floors}')


floor = House()
floor.set_new_number_of_floors(1)