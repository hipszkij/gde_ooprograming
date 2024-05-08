from Room import Room


class DoubleRoom(Room):
    def __init__(self, number, price):
        super().__init__(number, price)
        self.extras.append("double bed")