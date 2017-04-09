'''
Problem: using multi-line quoted-string, every character, including tabs,
		are saved to the variable. use textwrap.dedent() to remove tabs
		that had been inserted simply to align the block-quote with code above it
'''

import textwrap

if(True):
	a = '''
	line
	'''
print(a)
print(textwrap.dedent(a))
