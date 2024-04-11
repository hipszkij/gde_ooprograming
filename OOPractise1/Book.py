class Book:
    def __init__(self, author, title, publication_year, isbn):
        self.author = author
        self.title = title
        self.publication_year = publication_year
        self.isbn = isbn

    def display_info(self):
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"Publication Year: {self.publication_year}")
        print(f"ISBN: {self.isbn}")