class Member:
    def __init__(self, name, member_id, email):
        self._name = name
        self._member_id = member_id
        self._email = email

    def setEmail(self, email):
        self._email = email

    def getEmail(self):
        return self._email