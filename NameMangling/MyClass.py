class MyClass:
    def __init__(self):
        self.__my_attribute = 42

    def __my_method(self):
        return "Ez egy privát metódus"

# Példa használat:
obj = MyClass()
print(obj._MyClass__my_attribute)  # Hozzáférés a névváltoztatott attribútumhoz
print(obj._MyClass__my_method())    # Hívás a névváltoztatott metódusra
