class BookRental:
    def __init__(self, member, book, loan_date, return_date='2024-12-31'):
        self._member = member
        self._book = book
        self._loan_date = loan_date
        self._return_date = return_date
