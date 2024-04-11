import string
import math

a: int = 10
b: int = 15
c: float = 20.5

print(a + b)
print(a + c)

text: string = "Hello Word!"
print(text)
print(text.upper())

text = 5
print(a + text)


def add(numberA: int, numberB: int) -> int:
    return numberA + numberB


print(add(a, b))

print(math.floor(c))
print(math.ceil(c))
print(round(math.pi, 2))
