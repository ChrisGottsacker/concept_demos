'''
Several ways to insert string variable(s) into another string
'''

favs={'a':'mon calamari', 'b':'quarren'}

print('1st favorite species: %(a)s, 2nd favorite species: %(b)s' % favs)
print('1st favorite species: {a}, 2nd favorite species: {b}'.format_map(favs))
print('1st favorite species: ' + favs['a'] + ', 2nd favorite species: '+ favs['b'])
print('1st favorite species: {}, 2nd favorite species: {}'.format(favs['a'], favs['b']))
print('1st favorite species: %s, 2nd favorite species: %s' % (favs['a'], favs['b']))
