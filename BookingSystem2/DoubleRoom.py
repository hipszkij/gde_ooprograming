from Room import Room


class DoubleRoom(Room):
    def __init__(self, number, price):
        super().__init__(number, price)
        self.extras.append("double bed")

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True

    def unbook_room(self):
        if self.is_booked:
            self.is_booked = False
