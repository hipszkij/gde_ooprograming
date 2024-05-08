class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_availability(self):
        available_rooms = [room.number for room in self.rooms if not room.is_booked]
        return available_rooms

    def book_room_by_number(self, number):
        for room in self.rooms:
            if room.number == number:
                return room.book_room()
        return "Room not found."

    def get_room_prices(self):
        return {room.number: room.price for room in self.rooms}