# Szoba alaposztály
class Room:
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price

    def get_description(self):
        return f"Room {self.room_number}, Price: ${self.price}"

# Konkrét szoba osztályok
class SingleRoom(Room):
    def __init__(self, room_number, price):
        super().__init__(room_number, price)

    def get_description(self):
        return f"Single Room {self.room_number}, Price: ${self.price}"

class DoubleRoom(Room):
    def __init__(self, room_number, price):
        super().__init__(room_number, price)

    def get_description(self):
        return f"Double Room {self.room_number}, Price: ${self.price}"

class SuiteRoom(Room):
    def __init__(self, room_number, price):
        super().__init__(room_number, price)

    def get_description(self):
        return f"Suite Room {self.room_number}, Price: ${self.price}"

# Szoba Factory
class RoomFactory:
    @staticmethod
    def get_room(room_type, room_number, price):
        if room_type == "single":
            return SingleRoom(room_number, price)
        elif room_type == "double":
            return DoubleRoom(room_number, price)
        elif room_type == "suite":
            return SuiteRoom(room_number, price)
        else:
            raise ValueError("Unknown room type")

# Használat
factory = RoomFactory()

# Egyágyas szoba
single = factory.get_room('single', 101, 100)
print(single.get_description())  # Output: Single Room 101, Price: $100

# Kétágyas szoba
double = factory.get_room('double', 102, 150)
print(double.get_description())  # Output: Double Room 102, Price: $150

# Lakosztály
suite = factory.get_room('suite', 201, 300)
print(suite.get_description())  # Output: Suite Room 201, Price: $300
