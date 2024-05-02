class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("A szélességnek pozitívnak kell lennie.")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("A magasságnak pozitívnak kell lennie.")

    @property
    def area(self):
        return self._width * self._height


# Példa használat:
rectangle = Rectangle(5, 10)
print("Eredeti szélesség:", rectangle.width)
rectangle.width = 20  # A property setter meghívása
print("Módosított szélesség:", rectangle.width)

print("Eredeti magasság:", rectangle.height)
rectangle.height = 15  # A property setter meghívása
print("Módosított magasság:", rectangle.height)

print("Terület:", rectangle.area)  # A property getter meghívása
