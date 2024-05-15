class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self.vehicle_type

class Car(Vehicle):
    def __init__(self, name):
        super().__init__("Car")
        self.name = name

    def drive(self):
        return f"The {self.name}, which is a {self.vehicle_type}, is driving."

class Bike(Vehicle):
    def __init__(self, name):
        super().__init__("Bike")
        self.name = name

    def drive(self):
        return f"The {self.name}, which is a {self.vehicle_type}, is driving."


class Tram(Vehicle):
    def __init__(self, name):
        super().__init__("Tram")
        self.name = name

    def drive(self):
        return f"The {self.name}, which is a {self.vehicle_type}, is driving."


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type, name):
        if vehicle_type == "car":
            return Car(name)
        elif vehicle_type == "bike":
            return Bike(name)
        elif vehicle_type == "tram":
            return Tram(name)
        else:
            raise ValueError("Unknown vehicle type")

# Usage example:
factory = VehicleFactory()

car = factory.create_vehicle("car", "Toyota Corolla")
print(car.drive())

bike = factory.create_vehicle("bike", "Yamaha YZF")
print(bike.drive())

tram = factory.create_vehicle("tram", "Villamos1")
print(tram.drive())
