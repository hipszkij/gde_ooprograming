from Classes.Book import Book
from Classes.Member import Member
from Classes.BookRental import BookRental

# Usage example:
book1 = Book("J.K. Rowling", "Harry Potter and the Philosopher's Stone", 1997, "9780747532743")
book2 = Book("Harper Lee", "To Kill a Mockingbird", 1960, "9780061120084")

member1 = Member("John Doe", "M12345", "john@example.com")
member2 = Member("Jane Smith", "M67890", "jane@example.com")

rental1 = BookRental(member1, book1, "2024-04-11", "2024-05-11")
book1.decreaseBookNumber()

rental2 = BookRental(member2, book2, "2024-04-10", "2024-05-10")
book2.decreaseBookNumber()

rental3 = BookRental(member2, book1, "2024-04-11", "2024-06-11")
book1.decreaseBookNumber()



