class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f'Bookshelf contains {len(self.books)}'


class Books:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book {self.name}'


book1 = Books('Harry Potter')
book2 = Books('Python 101')
shelf = Bookshelf(book1, book2)
print(shelf)
