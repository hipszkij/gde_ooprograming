number = input("Adj meg egy számot: ")

if not isinstance(number, int):
    raise TypeError("Nem szám!!")