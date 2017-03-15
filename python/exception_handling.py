import sys

def openFile(filename):
	try:
		open(filename)
	except IOError:
		print('Caught exception while trying to open "{}"'.format(filename))
	else:
		print('Opened "{}" successfully'.format(filename))
	finally:
		print('Done\n')

openFile('this_file_doesnt_exist')
openFile(sys.argv[0])
