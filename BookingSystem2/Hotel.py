class Hotel:
    def __init__(self):
        self._room = []

    def add_room(self, room):
        self._room.append(room)

    def check_availabilty(self):
        available_rooms = []

        for room in self._room:
            if not room.is_booked:
                available_rooms.append(room.number)

        return available_rooms

    def book_room_by_number(self, number):
        for room in self._room:
            if room.number == number:
                room.book_room()

    def unbook_room_by_number(self, number):
        for room in self._room:
            if room.number == number:
                room.unbook_room()

    def get_room_price(self):
        return {room.number: room.price for room in self._room}

