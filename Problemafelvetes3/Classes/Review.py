from datetime import datetime


class Review:
    def __init__(self, user, restaurant, rating, comment):
        self.user = user
        self.restaurant = restaurant
        self.rating = rating
        self.comment = comment
        self.timestamp = datetime.now()