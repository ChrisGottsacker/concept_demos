import io

'''
Demonstrate iterating over lines of a String
'''
implicitNewline = '''
line one
line two
'''
implicitNewlineStream = io.StringIO(implicitNewline)
for line in implicitNewlineStream:
	print(line)

explicitNewlineStream = io.StringIO("line three\nline four\n")
for line in explicitNewlineStream:
	print(line)
