from Animal import Animal


class Cat(Animal):
    def __init__(self, name, kor, fajta, szin):
        super().__init__(name, kor, fajta)
        self._szin = szin
        print("Cat constructor")

    def speak(self):
        print("Cat is speaking")
