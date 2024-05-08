class Car:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def get_make(self):
        return self._make

    def set_make(self, newMake):
        if newMake:
            self._make = newMake

    def _internal_method(self):
        # belső működés
        pass

    publicMake = property(get_make, set_make)

# Példa használat:
car = Car("Toyota", "Corolla")
print(car.publicMake)

car.publicMake = "Ford"
print(car.publicMake)
