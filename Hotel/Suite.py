from Room import Room


class Suite(Room):
    def __init__(self, number, price):
        super().__init__(number, price)
        self.extras.extend(["double bed", "sofa", "minibar"])