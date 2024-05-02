from Album import Album
from Image import Image
from User import User

user = User(1,"Felhasználó", "F3l4a2zn4l0")
user2 = User(2,"Felhasználó2", "1234567")

image1 = Image(1, "Kép1", user, 1024, 'jpg')
image2 = Image(2, "Kép2", user, 2048, 'png')

album = Album(1, "Album", user)
album2 = Album(2, "Album2", user2)

album.add_image(image1)
album.add_image(image2)

album.get_all_image()

#nem fogja engedni
album2.add_image(image1)
album2.get_all_image()

