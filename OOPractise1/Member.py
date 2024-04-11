class Member:
    def __init__(self, name, identifier, email):
        self.name = name
        self.identifier = identifier
        self.email = email

    def display_info(self):
        print(f"Author: {self.name}")
        print(f"Title: {self.identifier}")
        print(f"Publication Year: {self.email}")
