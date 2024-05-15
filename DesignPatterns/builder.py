class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.color = None
        self.engine = None

    def __str__(self):
        return f"Car(brand={self.brand}, model={self.model}, color={self.color}, engine={self.engine})"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def build(self):
        return self.car

# Usage example:
builder = CarBuilder()
car = (builder.set_brand("Toyota")
            .set_model("Corolla")
            .set_color("Red")
            .set_engine("1.8L")
            .build())

print(car)
