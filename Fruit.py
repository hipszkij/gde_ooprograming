fruits = ['pear', 'pineapple', 'apple', 'orange']

print(fruits)

print("------------")

fruits.sort()
print(fruits)

print("------------")
for fruit in fruits:
    print(fruit)

print("------------")

for fruit in fruits:
    if fruit.startswith("a"):
        print(fruit)