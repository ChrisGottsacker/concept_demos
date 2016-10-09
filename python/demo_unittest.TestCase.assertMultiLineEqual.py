'''
unittest.TestCase.assertMultiLineEqual displays how two 
strings differ, with the added bonus that the strings
can span multiple lines
'''

import unittest

class Test(unittest.TestCase):
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
Test().test()
