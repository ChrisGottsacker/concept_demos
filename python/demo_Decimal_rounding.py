from decimal import *

print('''
Demonstration of basic rounding properties:''')
getcontext().prec = 4       # specified number of digits to keep
print(+Decimal('44446E3'))  # rounds to 4.445E+7
print(+Decimal('12345678')) # rounds to 1.235E+7
print(+Decimal('123'))      # "rounds" to 123 (no rounding)
                            # does not extend sigfigs to 123.0

print('''
Demonstration of more basic rounding, especially rounding up and down:''')
getcontext().prec = 1       # specified number of digits to keep
print(+Decimal('1.0'))  # rounds to 1
print(+Decimal('1.4'))  # rounds to 1
print(+Decimal('1.5'))  # rounds to 2
print(+Decimal('1.6'))  # rounds to 2
print(+Decimal('1.9'))  # rounds to 2


print('''
Demonstration of improper behavior when rounding using a 5:''')

'''
Specification from https://docs.python.org/3.5/library/decimal.html#decimal.ROUND_HALF_EVEN
decimal.ROUND_HALF_EVEN: Round to nearest with ties going to nearest even integer.

Using this mode of rounding, the digit following a 5 is used to break ties
before even/odd becomes an issue. This is wrong. The only digits that should be
used to inform rounding decisions are the last digit to keep, and the single
digit directly following it. All digits after the 5 should be ignored.
'''
setcontext(Context(prec=4, rounding=ROUND_HALF_EVEN))
num = Decimal('34565')  # given only the 5
print(+num)                 # rounds to 3.456E+4, it rounds correctly
num = Decimal('345650') # given a 5, and an irrelevant 0 after the 5
print(+num)                 # rounds to 3.456E+5, it rounds correctly
num = Decimal('345651') # given a 5, and an irrelevant digit > 0 after the 5
print(+num)                 # rounds to 3.457E+5, it rounds incorrectly
