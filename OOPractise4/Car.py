class Car:
    defaultPrice = 2000000

    def __init__(self, extraPrice):
        self.extraPrice = extraPrice

    def getCarPrice(self):
        return self.extraPrice + self.defaultPrice
