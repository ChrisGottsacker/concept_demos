from abc import ABCMeta, abstractmethod

class bar_abstract(metaclass=ABCMeta):
	@abstractmethod
	def eat(self):
		print('bar_implemented is instantiable, and eating s**t')

class bar_implemented(bar_abstract):
	def eat(self):
		print('bar_implemented is instantiable, and eating real food')

try:
	b = bar_abstract()
	b.eat()
except:
	print('bar_abstract not instantiable')

try:
	b = bar_implemented()
	b.eat()
except:
	print('bar_implemented not instantiable')
