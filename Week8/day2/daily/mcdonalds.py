#MCDonald's farm

class Farm:
	def __init__(self, farm_name: str):
		self.farm_name = farm_name
		self.animals = {}

	def add_animal(self, name: str, count: int = 1) -> None:
		self.animals[name] = self.animals.get(name, 0) + count

	def get_info(self) -> None:
		print(f"{self.farm_name}'s farm\n")
		for animal_name, animal_count in self.animals.items():
			print(f"{animal_name}: {animal_count}")

		print("\tE-I-E-I-0!")

	def get_animal_types(self) -> list:
		return sorted(self.animals.keys())

farm = Farm('McDonald')
farm.add_animal('cow',5)
farm.add_animal('sheep')
farm.add_animal('sheep')
farm.add_animal('goat', 12)

farm.get_info()
print(farm.get_animal_types())