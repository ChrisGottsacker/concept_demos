import numpy as np
a = np.arange(12).reshape(4,3)

print('Array a:\n', a, '\n')

print('Ask iterator for as big a chunk as possible:')
for x in np.nditer(a, flags=['external_loop']):
	for y in x:
		print('elements: ', x, '\n')


print('Ask iterator for elements, one at a time:')
for x in np.nditer(a):
	print('element: ', x)
