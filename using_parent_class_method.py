class Parent():
	def __init__(self,name):
		self.name = name

class Child(Parent):
	def __init__(self,name):
		super().__init__(name)
		self.last = 'Baggins'
		
print(Child('Bilbo').last)
print(Child('Bilbo').name)
