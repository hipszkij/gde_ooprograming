while True:
    try:
        inputszam = int(input("Adj meg egy számot: "))
        break
    except ValueError:
        print("Nem szám")


print(inputszam)