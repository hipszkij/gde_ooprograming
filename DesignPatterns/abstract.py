from abc import ABC, abstractmethod, abstractproperty

class Vehicle(ABC):
    def __init__(self, make, model):
        self._make = make
        self._model = model

    @abstractmethod
    def start_engine(self):
        """Start the engine of the vehicle."""
        pass

    @abstractmethod
    def stop_engine(self):
        """Stop the engine of the vehicle."""
        pass

    @property
    @abstractmethod
    def make(self):
        """Return the make of the vehicle."""
        pass

    @property
    @abstractmethod
    def model(self):
        """Return the model of the vehicle."""
        pass

class Car(Vehicle):
    def start_engine(self):
        return f"{self.make} {self.model} engine started."

    def stop_engine(self):
        return f"{self.make} {self.model} engine stopped."

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

class Motorcycle(Vehicle):
    def start_engine(self):
        return f"{self.make} {self.model} motorcycle engine started."

    def stop_engine(self):
        return f"{self.make} {self.model} motorcycle engine stopped."

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

# Usage
car = Car("Toyota", "Corolla")
motorcycle = Motorcycle("Harley-Davidson", "Street 750")

print(car.start_engine())  # Output: Toyota Corolla engine started.
print(motorcycle.start_engine())  # Output: Harley-Davidson Street 750 motorcycle engine started.
