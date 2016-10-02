value = '1.00'
print('before',value)
def change_value(value):
	value = '3'
	return(value)

print('return value', change_value(value) )
print('after', value)
