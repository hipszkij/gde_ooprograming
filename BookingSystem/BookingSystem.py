from SingleRoom import SingleRoom
from DoubleRoom import DoubleRoom
from Suite import Suite
from Hotel import Hotel


class BookingSystem:
    def __init__(self):
        self.hotel = Hotel()

    def load_data(self):
        self.hotel.add_room(SingleRoom("101", "25000"))
        self.hotel.add_room(SingleRoom("102", "25000"))
        self.hotel.add_room(DoubleRoom("201", "55000"))
        self.hotel.add_room(DoubleRoom("202", "55000"))
        self.hotel.add_room(Suite("501", "100000"))

    def user_interact(self):
        while True:
            print("1. Book a room")
            print("2. Check room availabilty")
            print("3. List room prices")
            print("4. Exit")

            user_choice = input("Válasz a fenti opciók közül: ")

            if user_choice == "1":
                room_number = input("Add meg a szobaszámát amit le szeretnél foglalni: ")
                self.hotel.book_room_by_number(room_number)
                print(f"A {room_number} szoba sikeresen lefoglalva")
            elif user_choice == "2":
                print("Elérhető szobák:", self.hotel.check_availability())
            elif user_choice == "3":
                print("Szoba árak:", self.hotel.get_room_prices())
            elif user_choice == "4":
                break


booking_system = BookingSystem()
booking_system.load_data()
booking_system.user_interact()

