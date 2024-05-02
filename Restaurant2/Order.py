class Order:
    orders = []

    def __init__(self, restaurant, food, user, order_date):
        self.orders.append({
            "restaurant": restaurant,
            "food": food,
            "user": user,
            "order_date": order_date
        })

    def getOrders(self):
        for order in self.orders:
            print("Rendelések: ")
            print(f"Étterem: {order['restaurant'].name}, {order['user'].name}: {order['order_date']}, {order['food'].name} - {order['food'].price} huf")