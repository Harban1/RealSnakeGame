class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("The car is starting.")

    def stop(self):
        print("The car has stopped.")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_percentage):
        super().__init__(make, model, year)
        self.battery_percentage = battery_percentage

    def start(self):
        print("Your electric car is silently starting.")

    def charge(self):
        print(f"Charging the car. Battery level: {self.battery_percentage}%")


toyota = Car("?", "cool model", 2009)
toyota.start()
toyota.stop()

tesla = ElectricCar("made", "bad model", 2020, 1)
tesla.charge()
tesla.start()
tesla.stop()
