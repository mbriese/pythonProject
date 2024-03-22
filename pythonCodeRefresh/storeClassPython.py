class Store:
	def __init__(self, name):
		# You'll need 'name' as an argument to this method.
		# Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
		self.name = name
		self.items = []
	
	def add_item(self, name, price):
		# Create a dictionary with keys name and price, and append that to self.items.
		item = {"name": name, "price": price}
		self.items.append(item)
	
	def stock_price(self):
		# Add together all item prices in self.items and return the total.
		return sum([item['price'] for item in self.items])

	@classmethod
	def franchise(cls , store) :
		# Return another store, with the same name as the argument's name, plus " - franchise"
		return cls(store.name + " - franchise")
	
	@staticmethod
	def store_details(store) :
		# Return a string representing the argument
		# It should be in the format 'NAME, total stock price: TOTAL'
		return '{}, total stock price: {}'.format(store.name , int(store.stock_price()))