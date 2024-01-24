class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long = f"{self.make} {self.model} {self.year}"
        return long

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer += miles

    def dicrement_odometer(self, miles):
        self.odometer -= miles

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it")

class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)

my_tesla = ElectricCar('tesla', 'models s', 2019)
print(my_tesla.get_descriptive_name())

name = Car('bmw', '570', '2020')
print(name.get_descriptive_name())
name.update_odometer(23500)
name.read_odometer()

name.increment_odometer(100)
name.read_odometer()

name.dicrement_odometer(200)
name.read_odometer()
