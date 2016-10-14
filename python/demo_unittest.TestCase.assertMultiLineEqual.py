'''
unittest.TestCase.assertMultiLineEqual displays how two
strings differ, with the added bonus that the strings
can span multiple lines
'''

import unittest

class Test(unittest.TestCase):

	def test_lineEndings(self):
		linefeed = 'string\n'
		carriageReturn = 'string\r'
		both = 'string\r\n'

		print('\\n vs \\r\\n')
		self.assertMultiLineEqual(linefeed, both)

		print('\\r vs \\r\\n')
		self.assertMultiLineEqual(carriageReturn, both)

		print('\\n vs \\r')
		self.assertMultiLineEqual(linefeed, carriageReturn)

	def test(self):
		string1='''
		several
		lines of a
		string are queal
		'''
		string2=string1 + ''
		self.assertMultiLineEqual(string1, string2) # equal

		string2=string1 + 'But this line is not the same'
		self.assertMultiLineEqual(string1, string2) # not equal

# Run test
# Test().test()
Test().test_lineEndings()
