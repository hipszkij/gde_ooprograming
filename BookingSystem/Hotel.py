class Hotel:
    def __init__(self):
        self.room = []

    def add_room(self, room):
        self.room.append(room)

    def check_availability(self):
        available_room = []
        for room in self.room:
            if not room.is_booked:
                available_room.append(room.number)

        return available_room

    def book_room_by_number(self, number):
        for room in self.room:
            if room.number == number:
                return room.book_room()

    def get_room_prices(self):
        return {room.number: room.price for room in self.room}


