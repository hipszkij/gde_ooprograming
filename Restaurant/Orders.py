class Orders:
    orders = []

    def __init__(self, orderDate, restaurant, user, food):
        self.orders.append({
            "orderDate": orderDate,
            "restaurant": restaurant,
            "user": user,
            "food": food
        })

    def getOrders(self):
        for order in self.orders:
            print("Rendelések: ")
            print(f"Étterem: {order['restaurant'].name} - {order['user'].name}: {order['food'].name}")
