from decimal import *
a = Decimal('1.1')
b = Decimal('2')

# By Sigfig addition rule, 1.1 + 2 rounds to 3, not 3.1
print(a+b)
