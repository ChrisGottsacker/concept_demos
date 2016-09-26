from enum import Enum

class ships(Enum):
	millenium_falcon = (12, 'matte')
	jade_shadow = (10, 'gray')
	errant_venture = (17, 'red')

	def __init__(self, value, color):
		self.val = value
		self.color = color
		self.cool_factor = None

	def add_coolness(self, cool_factor):
		self.cool_factor = cool_factor

for ship in ships:
	print(ship.name, ship.val, ship.color, ship.cool_factor)

ships.millenium_falcon.add_coolness('smug-lier')
ships.jade_shadow.add_coolness('extravagant')
ships.errant_venture.add_coolness('sick')

print('\n')
for ship in ships:
	print(ship.name, ship.val, ship.color, ship.cool_factor)

print('\n')
for key in ships.__members__.keys():
	print(key)
