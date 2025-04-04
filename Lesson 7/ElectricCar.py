import Car

class ElectricCar(Car):
    def __init__(self,make,model,year,battery_level):
        super().__init__(make,model,year)
        self.battery_level = battery_level

    