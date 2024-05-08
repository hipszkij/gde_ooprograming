from DoubleRoom import DoubleRoom
from Suite import Suite
from SingleRoom import SingleRoom
from Hotel import Hotel


class BookingSystem:
    def __init__(self):
        self.hotel = Hotel()

    def load_data(self):
        self.hotel.add_room(SingleRoom(101, 50))
        self.hotel.add_room(DoubleRoom(102, 75))
        self.hotel.add_room(Suite(201, 120))

    def interact(self):
        while True:
            choice = input("1: Book a room, 2: Check availability, 3: Room prices, 4: Exit. Enter your choice: ")
            if choice == "1":
                room_number = int(input("Enter room number to book: "))
                print(self.hotel.book_room_by_number(room_number))
            elif choice == "2":
                print("Available rooms:", self.hotel.check_availability())
            elif choice == "3":
                print("Room prices:", self.hotel.get_room_prices())
            elif choice == "4":
                break
            else:
                print("Invalid choice, please try again.")


# Example usage
booking_system = BookingSystem()
booking_system.load_data()
booking_system.interact()
