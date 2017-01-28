class foo():
	class_var = 'foo var'
	def __init__(self,name):
		self.name = name
	def __hash__(self):
		return(hash(self.name))
	def __eq__(self, other):
		return(self.name==other.name)

class bar(foo):
	def __init__(self):
		self.name = 'frodo'

print(bar().class_var)