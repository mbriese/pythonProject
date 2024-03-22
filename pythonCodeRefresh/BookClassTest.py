class Book:
	# variable - this is a tuple
	TYPES = ("hardcover", "paperback", "audio")
	
	def __init__(self, name, book_type, weight):
		self.name = name
		self.book_type = book_type
		self.weight = weight
		
	def __repr__(self):
		return f"<Book {self.name}, {self.book_type}, weighing {self.weight}grams>"
	
	@classmethod
	def hardcover(cls, name, page_weight):
		return Book(name, Book.TYPES[0], page_weight + 100)
	
	@classmethod
	def paperback(cls, name, page_weight):
		return Book(name, Book.TYPES[1], page_weight)
	
print(Book.TYPES)
book = Book("Harry Potter", "hardcover", 1500)
comicBook = Book("Archie Comic", "paperback", 50)



print(book.name)
print(comicBook.name)
