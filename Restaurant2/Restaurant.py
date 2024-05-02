class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def __str__(self):
        return f"Az étterem neve: {self.name}"

    def getMenuItem(self):
        for food in self.menu:
            print(f"({food.id}): {food.name} ........... {food.price}")

    def __add__(self, food):
        self.menu.append(food)
