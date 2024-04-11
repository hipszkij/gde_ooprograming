fruits = ['pear', 'pineapple', 'apple', 'orange']

print(fruits)

print("------------")

fruits.sort()
print(fruits)

print("------------")
for fruit in sorted(fruits):
    print(fruit)

print("------------")

for fruit in sorted(fruits):
    if fruit.startswith("a"):
        print(fruit)