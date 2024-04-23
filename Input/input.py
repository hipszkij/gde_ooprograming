input_result = input("Írj be egy számot: ")

try:
    integer_input_result = int(input_result)
except ValueError:
    print("Nem szám típusú, amit beírtál")
else:
    if integer_input_result < 10:
        raise ValueError("10-nél nagyobb számot adj meg")
    else:
        print("Megfelelő szám")