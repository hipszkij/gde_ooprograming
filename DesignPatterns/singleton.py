class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CarRegistry(metaclass=Singleton):
    def __init__(self):
        self.cars = {}

    def register_car(self, owner, make, model):
        self.cars[owner] = {"make": make, "model": model}

    def get_car_details(self, owner):
        return self.cars.get(owner, "No car registered for this owner.")

# Usage
registry1 = CarRegistry()
registry1.register_car("John Doe", "Toyota", "Corolla")

registry2 = CarRegistry()
print(registry1 is registry2)  # Output: True

print(registry2.get_car_details("John Doe"))  # Output: {'make': 'Toyota', 'model': 'Corolla'}
