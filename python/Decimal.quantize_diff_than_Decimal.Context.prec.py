from decimal import *

a = Decimal('102.72')           # Initial fixed-point values
b = Decimal('3.17')

print('\nRounding using quantize()')
print(b/a)								# full result
print((b/a).quantize(Decimal('.01')))	# specifies num. decimal digits to include
setcontext( Context( prec=1))			# specifies num. sigfigs to include
print(b/a)

print('\nRounding using Context().create_decimal() ')
setcontext( Context( prec=None))
avg = sum([Decimal('.0234'), Decimal('23.3'), Decimal('2')])/3
print(avg)
print(Context(prec=3).create_decimal(avg))

print('\nExtending precision using quantize()')
setcontext( Context( prec=None))
print(Decimal('1').quantize(Decimal('.01')))
