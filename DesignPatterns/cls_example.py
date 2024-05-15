class Example:
    count = 0  # osztály szintű változó

    def __init__(self, value):
        self.value = value  # példány szintű változó
        Example.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

obj1 = Example(10)
obj2 = Example(20)
obj3 = Example(30)

print(obj3.count)


print(Example.get_count())  # Kiírja a létrehozott példányok számát, ami 2
