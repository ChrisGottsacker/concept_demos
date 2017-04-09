'''
If a literal is only going to be used/not-used in one place,
this shortcut enables a more concise representation

Note that idx indexes into the list literal,
x is a string, not a list
'''

idx = 2
x = ['a', 'b', 'c'][idx]
print(x)
