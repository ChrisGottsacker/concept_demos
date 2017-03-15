from testfixtures import tempdir, compare

@tempdir()
def readWriteUsingUnicode(dir):
	'''Compare strings in entirety'''
	dir.write('test.txt', 'ab', 'utf-8')
	compare(dir.read('test.txt', 'utf-8'), 'aa')

@tempdir()
def readWriteUsingBytes(dir):
	'''Compare strings byte by byte'''
	dir.write('test.txt', b'ab')
	compare(dir.read('test.txt'), b'aa')

readWriteUsingBytes()
readWriteUsingUnicode()
