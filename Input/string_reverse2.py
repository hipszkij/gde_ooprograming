while True:
    try:
        # Felhasználótól szó bekérése
        inputString = input("Adj meg egy szót: ")

        # Ellenőrizzük, hogy a szöveg csak betűket tartalmaz-e
        if not inputString.isalpha():
            raise ValueError("Csak szöveges bemenetet lehet megadni!")

        # Ha minden rendben, kilépünk a ciklusból
        break

    except ValueError as e:
        # Hiba esetén kiírjuk a hibaüzenetet
        print(e)

# Sikeres adatbevitel után a szöveg megfordítása és kiíratása
revText = inputString[::-1]

print("A szó visszafelé: ", revText)
