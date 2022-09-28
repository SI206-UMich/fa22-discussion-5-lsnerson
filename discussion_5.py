import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	if sentence == "" or type(sentence) != str:
		return 0
	for i in range(len(sentence) - 1):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		
		

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock_name = self.items[0]
		for item in self.items:
			if item.stock > max_stock_name.stock:
				max_stock_name = item
		return max_stock_name


	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price_item = self.items[0]
		for item in self.items:
			if item.price > max_price_item.price:
				max_price_item = item
		return max_price_item

# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)
		self.w1 = Warehouse([self.item1, self.item2, self.item3, self.item4, self.item5])


	## Check to see whether count_a works
	def test_count_a(self):      
		self.assertEqual(count_a("Lauren is my name"), 2, "Testing string with one a")
		self.assertEqual(count_a("Dog"), 0, "String with no a's")
		self.assertEqual(count_a(""), 0, "Testing an empty string")
		self.assertEqual(count_a(456), 0, "Testing an empty string")



	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.w1.add_item(self.item1)
		self.assertEqual(self.w1.items[0], self.item1)
		self.w1.add_item(self.item2)
		self.assertEqual(self.w1.items[1], self.item2)
		self.w1.add_item(self.item3)
		self.assertEqual(self.w1.items[2], self.item3)
		self.w1.add_item(self.item4)
		self.assertEqual(self.w1.items[3], self.item4)


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.assertEqual(self.w1.get_max_stock(), self.item3)


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.assertEqual(self.w1.get_max_price(), self.item1)

		
		

def main():
	unittest.main(verbosity=2)

if __name__ == "__main__":
	main()