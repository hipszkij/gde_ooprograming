from datetime import datetime


class Order:
    def __init__(self, user, restaurant, items):
        self.user = user
        self.restaurant = restaurant
        self.items = items
        self.status = "New"  # lehetne többféle státusz is, például: "Feldolgozás alatt", "Kiszállítás alatt", "Kiszállítva"
        self.timestamp = datetime.now()