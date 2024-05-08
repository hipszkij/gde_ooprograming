from Album import Album
from User import User
from Image import Image

user1 = User(1, "Teszt user", "123456")
user2 = User(2, "Teszt user2", "password1")

image1 = Image(1, "Family pics", 1024, "jpg", user1)
image2 = Image(2, "Wedding image", 2048, "png", user1)
image3 = Image(3, "My dog", 1024, "jpg", user2)

album1 = Album(1, "Family album", user1)
album2 = Album(2, "Party album", user1)
album3 = Album(3, "My animals", user2)

album1.add_image(image1)
album2.add_image(image2)
album3.add_image(image3)

album1.get_images()
album2.get_images()
album3.get_images()