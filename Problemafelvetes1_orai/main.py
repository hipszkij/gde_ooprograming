from Book import Book
from BookRental import BookRental
from Member import Member

book1 = Book("Test author", "Test title", 2000, 123456789)
member = Member("1", "Test User", "test.user@gmail.com")

#book1.public_title = "Valami"
book1.title = "Valami"
print(book1.title)

bookRental = BookRental(member, book1, '2024-04-11')

bookRental.listRents()
