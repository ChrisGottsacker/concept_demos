from decimal import *

def is_numeric(string):
	try:
		Decimal(string)
		return(True)
	except InvalidOperation:
		return(False)
		
print(is_numeric('34324.3434'))
print(is_numeric('-.343A24'))
print(is_numeric('-34324.3434'))
print(is_numeric('-.34324_'))
print(is_numeric('-34324'))
print(is_numeric('-34@324'))
print(is_numeric('-.34324'))
print(is_numeric('-.343 A24'))