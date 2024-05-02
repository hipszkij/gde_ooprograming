class Book:
    def __init__(self, author, title, year, isbnNumber):
        self._author = author
        self._title = title
        self._year = year
        self._isbnNumber = isbnNumber

    def get_author(self):
        return self._author

    def set_author(self, new_author):
        self._author = new_author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    #public_title = property(get_title, set_title)

