class Car:
    def __init__(self, make, model):
        self._make = make  # _make attribútum, belső használatra
        self._model = model  # _model attribútum, belső használatra

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        if make:
            self._make = make

    def _internal_method(self):
        # belső működés
        pass

# Példa használat:
car = Car("Toyota", "Corolla")
car.make = "RRR"

print(car.make)  # külső hozzáférés a make attribútumhoz
car.make = "Ford"  # külső hozzáférés a make attribútumhoz
print(car.make)  # külső hozzáférés a make attribútumhoz


car._internal_method()  # belső metódus hívása
