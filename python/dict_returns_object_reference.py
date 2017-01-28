# Proves that dictionary returns reference to object, not value of object

class foo():
	class_var = 'individual_var'
	def __init__(self,name):
		self.name = name
	def __hash__(self):
		return(hash(self.name))
	def __eq__(self, other):
		return(self.name==other.name)

frogs = {'kermit':foo('kermy')}

print(frogs['kermit'].name)
char = frogs['kermit']
char.name = 'kary'
print(frogs['kermit'].name)
