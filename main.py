class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f'{self.brand} , {self.model} is driving')
               
my_car = car('Toyota','Honda')
my_car.drive()