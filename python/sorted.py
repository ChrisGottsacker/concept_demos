class c():
	def __init__(self, avg):
		self.avg = avg

	def keyFn(self):
		return self.avg


a = [c(.016), c(.005)]

for x in sorted(a, key=c.keyFn):
	print(x.avg)
