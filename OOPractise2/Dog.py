from Animal import Animal


class Dog(Animal):
    def __init__(self, name, kor, fajta, szin):
        super().__init__(name, kor, fajta)
        self._szin = szin
        print("Dog constructor")

    def tostring(self):
        print(f"A nevem {self._nev}")
        print(f"A korom {self._kor}")
        print(f"A fajtám {self._fajta}")
        print(f"A szinem {self._szin}")

    def my_name(self):
        print(f"A kutya neve: {self._nev}")

    def speak(self):
        print("Dog is speaking")