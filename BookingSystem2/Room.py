from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.is_booked = False
        self.extras = []

    @abstractmethod
    def book_room(self):
        pass

    @abstractmethod
    def unbook_room(self):
        pass

