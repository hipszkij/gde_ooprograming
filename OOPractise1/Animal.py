class Animal:
    def __init__(self, name, kor, fajta):
        self._nev = name
        self._kor = kor
        self._fajta = fajta
        print("Allat konstruktor")

    def tostring(self):
        print(f"A nevem {self._nev}")
        print(f"A korom {self._kor}")
        print(f"A fajtám {self._fajta}")

    def my_name(self):
        print(f"A nevem {self._nev}")



class Dog(Animal):
    def __init__(self, name, kor, fajta, szin):
        super().__init__(name, kor, fajta)
        self._szin = szin
        print("Dog constructor")

    def my_name(self):
        return 2 + 2

animal = Animal("Kutya", "10", "német juhász")
print(animal.tostring())

print("---------------")

dog = Dog("Buksi", 23, "bulldog", "barna")
print(dog.tostring())
print(dog.my_name())
