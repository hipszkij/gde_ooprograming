class Room:
    def __init__(self, number, price):
        self.number = number
        self.is_booked = False
        self.price = price
        self.extras = []

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            return f"Room {self.number} has been booked."
        else:
            return f"Room {self.number} is already booked."

    def unbook_room(self):
        if self.is_booked:
            self.is_booked = False
            return f"Room {self.number} has been unbooked."
        else:
            return f"Room {self.number} is not currently booked."