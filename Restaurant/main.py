from Food import Food
from Restaurant import Restaurant
from User import User
from Orders import Orders

food1 = Food(1, "Pizza", 1000)
food2 = Food(2, "Hamburger", 2000)

restaurant = Restaurant("Teszt étterem", [food1, food2])
user = User("1", "Teszt user", "tesztuser@gmail.com", "1234 Budapest Teszt utca 1")

#print(restaurant)
#restaurant.getMenuItems()

print("Új menü elem hozzáadása")
while True:
    try:
        id = 3
        inputItemName = input("Adj meg egy ételt: ")
        inputItemPrice = int(input("Add meg az étel árát: "))

        if inputItemPrice <= 0 or inputItemPrice >= 100000:
            raise ValueError("Az étel ára csak 0 és 100000 közötti lehet")

        food = Food(id, inputItemName, inputItemPrice)
        restaurant + food
        id + 1
        break
    except ValueError as e:
        print(e)


restaurant.getMenuItems()

userOrderId = int(input("Melyik ételt szeretnéd megrendelni? Add meg a sorszámát! "))

orders = Orders("2024-04-25 12:00:00", restaurant, user, restaurant.menu[userOrderId - 1])
orders.getOrders()