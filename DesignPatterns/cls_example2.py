class Car:
    total_cars = 0  # Osztály szintű változó az összes autó számának számlálására

    def __init__(self, make, model):
        self.make = make  # Példány szintű változó
        self.model = model  # Példány szintű változó
        Car.increment_total()  # Osztálymetódus hívása az autók számának növelésére

    @classmethod
    def increment_total(cls):
        cls.total_cars += 1  # Növeli az összes autó számát

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars  # Visszaadja az összes autó számát

    def get_car_info(self):
        return f"{self.make} {self.model}"  # Visszaadja az adott autó információit

# Autók létrehozása
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Információk lekérdezése
print(car1.get_car_info())  # Kiírja: Toyota Corolla
print(car2.get_car_info())  # Kiírja: Honda Civic

# Osztály szintű adatok lekérdezése
print(Car.get_total_cars())  # Kiírja: 2
