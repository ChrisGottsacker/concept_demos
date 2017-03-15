class hash_by_default():
	def __init__(self,name):
		self.name = name

class hash_by_name():
	def __init__(self,name):
		self.name = name
	def __hash__(self):
		return( hash(self.name) )
	def __eq__(self, other):
		return(self.name == other.name)

names = {}		
name1 = hash_by_default("Corran")
name2 = hash_by_default("Corran")
names[name1] = "Horn"		# added as unique key
names[name2] = "Horny"		# added as unique key

print(names[name1])
print(names[name2])

names = {}		
name1 = hash_by_name("Corran")
name2 = hash_by_name("Corran")
names[name1] = "Horn"		# added as unique key
names[name2] = "Horny"		# overwrites name1

print(names[name1])
print(names[name2])
