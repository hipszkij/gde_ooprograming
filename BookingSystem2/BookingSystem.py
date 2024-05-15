from Hotel import Hotel
from SingleRoom import SingleRoom
from DoubleRoom import DoubleRoom
from Suit import Suit


class BookingSystem:
    def __init__(self):
        self.hotel = Hotel()

    def load_data(self):
        self.hotel.add_room(SingleRoom("101", 10000))
        self.hotel.add_room(SingleRoom("102", 10000))
        self.hotel.add_room(SingleRoom("103", 10000))
        self.hotel.add_room(DoubleRoom("201", 20000))
        self.hotel.add_room(DoubleRoom("202", 20000))
        self.hotel.add_room(DoubleRoom("203", 20000))
        self.hotel.add_room(Suit("501", 100000))
        self.hotel.add_room(Suit("502", 100000))

    def user_interact(self):
        while True:
            print("1. Book room")
            print("2. Unbook room")
            print("3. Check room availability")
            print("4. List room price")
            print("5. Exit")

            user_choice = input("Válasz a fenti opciók közül: ")

            if user_choice == "1":
                room_number = input("Add meg a szoba számát amit le szeretnél foglalni: ")
                self.hotel.book_room_by_number(room_number)
            elif user_choice == "2":
                room_number = input("Add meg a szoba számát amit le szeretnél mondani: ")
                self.hotel.unbook_room_by_number(room_number)
            elif user_choice == "3":
                print("Elérhető szobák: ", self.hotel.check_availabilty())
            elif user_choice == "4":
                print("Szoba árak: ", self.hotel.get_room_price())
            elif user_choice == "5":
                break


booking_system = BookingSystem()
booking_system.load_data()
booking_system.user_interact()
