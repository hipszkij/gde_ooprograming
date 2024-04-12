class BookRental:
    def __init__(self, member, book, startDate, endDate="2024-12-31"):
        self.member = member
        self.book = book
        self.startDate = startDate
        self.endDate = endDate