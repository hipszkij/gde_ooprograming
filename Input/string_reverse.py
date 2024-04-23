# A felhasználótól szó bekérése
inputString = input("Kérlek, írj be egy szót: ")

# Az eredeti szöveg visszafelé kiírása 'for' ciklussal
revText = ''
for character in inputString:
    revText = character + revText

print("A szó visszafelé: ", revText)


#https://www.w3schools.com/python/python_howto_reverse_string.asp
revText = inputString[::-1]
print("A szó visszafelé: ", revText)
