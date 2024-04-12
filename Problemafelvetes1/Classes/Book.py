class Book:
    _numberOfBooks = 20

    def __init__(self, author, title, publication_year, isbn):
        self._author = author
        self._title = title
        self._publication_year = publication_year
        self._isbn = isbn

    def decreaseBookNumber(self):
        self._numberOfBooks -= 1

        