class Farm:
	def __init__(self, name):
		self.name = name
		self.animals = {}

	def farm_name(self):
		print(f"{self.name}'s farm")

	def add_animal(self, animal, quantity):
		self.animals[animal] = quantity
		print(f"{animal} : {self.animals[animal]}")

	def show_all_the_animals(self):
		for animal, quantity in self.animals.items():
			print(f"there is {quantity} {animal}'s")

mcdonalds = Farm("Mcdonald")
mcdonalds.add_animal("cow", 5)

mcdonalds.show_all_the_animals()