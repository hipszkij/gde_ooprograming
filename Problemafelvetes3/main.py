from datetime import datetime

from Classes.User import User
from Classes.Restaurant import Restaurant
from Classes.Order import Order
from Classes.Review import Review
from Classes.Delivery import Delivery

user1 = User("John Doe", "john@example.com", "123 Main St, Anytown", "123-456-7890")
restaurant1 = Restaurant("Pizza Palace", "456 Elm St, Anytown", {"Pizza Margherita": 10, "Pepperoni Pizza": 12})

order1 = Order(user1, restaurant1, ["Pizza Margherita"])
delivery1 = Delivery(order1, "123 Elm St, Anytown", datetime(2024, 4, 11, 17, 30))


review1 = Review(user1, restaurant1, 5, "Fantasztikus pizza!")
