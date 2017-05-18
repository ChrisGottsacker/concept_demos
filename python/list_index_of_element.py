def printIndex(color):
	if color in colors:
		print('First index of "{}" is {}'.format(color, colors.index(color)))
	else:
		print('"{}" is not in our list of colors'.format(color))


colors = ['red', 'blue', 'yellow']

printIndex('red')
printIndex('orange')
