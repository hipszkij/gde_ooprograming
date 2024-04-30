class BookRental:
    _rental = []

    def __init__(self, member, book, startDate, endDate="2024-12-31"):
        self._rental.append({
            'member': member,
            'book': book,
            'startDate': startDate,
            'endDate': endDate
        })

    def listRents(self):
        for item in self._rental:
            print(f"{item['member'].get_name()} .... {item['book'].title}")
