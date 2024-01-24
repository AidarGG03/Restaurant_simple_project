class Restaraunt:
    def __init__(self, restaraunt_name, cuisine_type):
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaraunt(self):
        print(f"{self.restaraunt_name}")
        print(f"{self.cuisine_type}")

    def open_restaraunt(self):
        print(f"{self.restaraunt_name} is now opening!")

    def update_numbers(self, number):
        self.number_served = number

    def increment_numbers(self, increment):
        self.number_served += increment

    def served_number(self):
        print(f"Served numbers: {self.number_served}")

restaraunt = Restaraunt("Oblako_53", "Italian Cuisine")
restaraunt.describe_restaraunt()
restaraunt.open_restaraunt()
restaraunt.update_numbers(56)
restaraunt.served_number()

restaraunt.increment_numbers(100)
restaraunt.served_number()
