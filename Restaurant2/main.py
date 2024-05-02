from Restaurant import Restaurant
from Food import Food
from User import User
from Order import Order

user1 = User(1, "Teszt felhasználó", "teszt@gmail.com", "1234 Budapest Teszt utca 1")

food1 = Food(1, "Hamburger", 1234)
food2 = Food(2, "Pizza", 4567)
food3 = Food(3, "Ice cream", 9876)

restaurant = Restaurant("Teszt étterem", [food1, food2, food3])
print(restaurant)

while True:
    try:
        foodName = input("Add meg az új étel nevét: ")
        foodPrice = int(input("Add meg az új étel árát: "))

        if foodPrice <= 0 or foodPrice > 100000:
            raise ValueError("Az új étel ára nem lehet kisebb mint 0 és nagyobb mint 100 000 Huf")

        food = Food(4, foodName, foodPrice)

        restaurant + food
        break
    except ValueError as e:
        print(e)


restaurant.getMenuItem()

orderId = int(input("Add meg a rendelni kívánt étel sorszámát: "))

order = Order(restaurant, restaurant.menu[orderId - 1], user1, '2024-04-30 18:00:00')
order.getOrders()