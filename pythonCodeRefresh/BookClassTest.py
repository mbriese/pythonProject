class Book:
	TYPES = ('hardcover', 'paperback', 'audio')
	
	def __init__(self, name, page_count, book_type, weight):
		self.name = name
		self.book_type = book_type
		self.page_count = page_count
		self.weight = weight
		self.pages_read = 0
	
	def __repr__(self):
		return f"<Book {self.name}, {self.book_type}, {self.page_count} weighing {self.weight}grams>"

	def read(self, pages):
		self.pages_read += pages
		print(f"You have now read {self.pages_read} out of {self.page_count}")

	@classmethod
	def hardcover(cls, name, page_weight):
		return Book(name, Book.TYPES[0], page_weight+100)
	
	@classmethod
	def paperback(cls, name, page_weight):
		return Book(name, Book.TYPES[1], page_weight)


print(Book.TYPES)
book = Book("Harry Potter", 1500, "hardcover", 1000)
comicBook = Book("Archie Comic", 50, "paperback", 50)

print(book.name)
print(comicBook.name)
