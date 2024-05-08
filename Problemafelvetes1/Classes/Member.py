
class Member:
    def __init__(self, name, member_id, email):
        self._name = name
        self._member_id = member_id
        self._email = email


    email = property(get_email, set_email)
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

