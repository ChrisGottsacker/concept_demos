import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser_name')
parser.add_argument('-eat', eaction='store_true')

flavor_parser = subparsers.add_parser('flavor')
color_parser = subparsers.add_parser('color')

flavor_parser.add_argument('-chocolate', action='store_true')
flavor_parser.add_argument('-vanilla', action='store_true')

color_parser.add_argument('-brown', action='store_true')
color_parser.add_argument('-cream', action='store_true')

print('Handle a single sub-parser in set of input, throw error for "flavor -chocoloate" color -cream\n')
print('    parse using "flavor" sub-parser:\n\t', parser.parse_args(['flavor', '-chocolate']))
print('    parse using "color" sub-parser:\n\t', parser.parse_args(['color', '-cream']))


print('''\n\nHandle multiple sub-parsers in some set of args (e.g. flavor -chocolate color -cream),
parse as much using one sub-parser, then parse the rest with the second sub-parser\n''')
args1, rest = parser.parse_known_args(['flavor', '-chocolate', 'color', '-cream'])
print('    parse up to unidentified token "color" (i.e. flavor -chocolate) \
using', args1.subparser_name, 'sub-parser\n\t', args1)
args2 = parser.parse_args(rest)
print('    parse remaining tokens (i.e. color -cream) using', args2.subparser_name, 'sub-parser \n\t', args2)


# get list of subparsers:
print(subparsers.choices.keys())
