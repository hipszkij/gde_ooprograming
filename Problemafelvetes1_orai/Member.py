class Member:
    _isVip = False

    def __init__(self, id, name, email):
        self._id = id
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

