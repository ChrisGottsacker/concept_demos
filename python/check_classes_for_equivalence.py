class foo():
	def __init__(self,name):
		self.name = name

class bar(foo):
	def __init__(self):
		self.name = 'frodo'

b = bar()
ba = bar()
f = foo('dfd')
print('class: ', b.__class__.__name__, ', same class?', b.__class__ is ba.__class__)
print('class: ', b.__class__.__name__, ', same class?', b.__class__ is f.__class__)
