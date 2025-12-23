class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f'{self.brand} , {self.model} is driving')
               
my_car = car('Toyota','Honda')
my_car.drive()


class ElectricCar(car):
    def __init__(self, brand, model,battery_size):
        super().__init__(model,brand)
        self.battery_size = battery_size

    def charge(self):
        print(f'{self.brand} ,{self.model}, battery is charging....{self.battery_size}')

car = ElectricCar('Toyota','Honda',150)
car.charge()