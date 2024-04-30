class Restaurant:
    orders = []

    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def __str__(self):
        return f"Az étterem neve: {self.name}"

    def getMenuItems(self):
        for food in self.menu:
            print(f"{food.id}. {food.name} .............. {food.price} huf")

    def __add__(self, other):
        self.menu.append(other)