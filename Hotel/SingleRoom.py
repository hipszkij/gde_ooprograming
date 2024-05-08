from Room import Room


class SingleRoom(Room):
    def __init__(self, number, price):
        super().__init__(number, price)
        self.extras.append("single bed")