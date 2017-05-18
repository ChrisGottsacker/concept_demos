import sys

def openFile(filename):
	try:
		f = open(filename)
	except IOError:
		raise Exception('Caught exception while trying to open "{}"'.format(filename))
	else:
		print('First word of {}: "{}"'.format(filename, f.readline().split()[0]))
	finally:
		pass

try:
	openFile('this_file_doesnt_exist')
except Exception as e:
	print(e)

try:
	openFile(sys.argv[0])
