class TooManyPagesReadError(ValueError):
	pass


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
		if self.pages_read + pages > self.page_count:
			raise ValueError(f"You tried to read {self.pages_read + pages} and exceeds the pages in the book {self.page_count}")
		else:
			self.pages_read += pages
			print(f"Book: {self.name} Pages read: {self.pages_read}")

	@classmethod
	def hardcover(cls, name, page_count, page_weight):
		return Book(name, Book.TYPES[0], page_count, page_weight+100)
	
	@classmethod
	def paperback(cls, name, page_count, page_weight):
		return Book(name, Book.TYPES[1], page_count, page_weight)


print(Book.TYPES)
book = Book("Harry Potter", 1500, "hardcover", 1000)
comicBook = Book("Archie Comic", 50, "paperback", 50)

print(book.name)
print(comicBook.name)
python101 = Book("Python 101", 50, "hardcover", 1000)
python101.read(35)

python102 = Book("Python 102", 150, "paperback", 200)
try:
	python102.read(75)
	python102.read(25)
	python102.read(51)
except TooManyPagesReadError as e:
	print(e)