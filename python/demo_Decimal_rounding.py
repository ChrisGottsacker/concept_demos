from decimal import *

getcontext().prec = 4
print(+Decimal('44446E3'))
print(+Decimal('12345678'))
print(+Decimal('123'))	# does not extend sigfigs
