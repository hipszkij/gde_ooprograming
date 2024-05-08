class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self._password = password

    def verify_password(self, password):
        return self._password == password

