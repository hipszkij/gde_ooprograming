class SimpleContainer:
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):
        # Az elemek számának visszaadása
        return len(self.elements)

    def __getitem__(self, index):
        # Egy adott indexű elem visszaadása
        print("getitem")
        return self.elements[index]

    def __setitem__(self, key, value):
        print("setitem")
        self.elements[key] = value


# Példányosítás
container = SimpleContainer([1, 2, 3, 4, 5])

# Konténer hosszának lekérdezése
print("A konténer hossza:", len(container))

# Egy adott elem lekérdezése index alapján
print("A konténer második eleme:", container[1])

container[1] = 10
print("A konténer második eleme:", container[1])

