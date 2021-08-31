class Character:

	def __init__(self, name: str, life:int = 20, attack: int = 10):
		self.name = name
		self.life = life
		self.attack = attack

		print(f"Creating the character {name} with life {life} and attack {attack}")

	def basic_attack(self, opponent):
		opponent.life -= self.attack


class Druid(Character):

	def meditate(self):
		self.life += 10
		self.attack -= 2

	def animal_help(self):
		self.attack += 5

	def fight(self, opponent):
		opponent.life -= (0.75 * self.life + 0.75 * self.attack)


class Warrior(Character):

	def brawl(self, opponent):
		opponent.life -= (2 * self.attack)
		self.life += (0.5 * self.attack)

	def train(self):
		self.life += 2
		self.attack += 2

	def roar(self, opponent):
		opponent.attack -= 3


class Mage(Character):

	def curse(self, opponent):
		opponent.attack -= 2

	def summon(self):
		self.attack += 3

	def cast_spell(self, opponent):
		opponent.life -= self.attack / self.life


war = Warrior(name='Jack', attack=100, life=200)
mage = Mage('Norm', 70, 150)
druid = Druid('Vic', 80, 140)

print(war.attack)
mage.curse(war)
print(war.attack)