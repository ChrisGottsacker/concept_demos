def removeCatsSliceAssignment(items):
	'''Modify items to exclude any item containg string "cat"

	Succeeds in modifying the list pointed to by items
	'''
	items[:] = [item for item in items if 'cat' not in item]
	
def removeCatsNaive(items):
	'''Modify items to exclude any item containg string "cat"

	Only changes what items points to, as expected
	'''
	items = [item for item in items if 'cat' not in item]


items = ['gecko', 'main-koon cat', 'cat', 'hamster']
removeCatsNaive(items)
print(items)	# items is unchanged, and no items are deleted

removeCatsSliceAssignment(items)
print(items)	# items is changed as expected
