from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def tostring(self):
        pass

    @abstractmethod
    def my_name(self):
        pass

    @abstractmethod
    def speak(self):
        pass
