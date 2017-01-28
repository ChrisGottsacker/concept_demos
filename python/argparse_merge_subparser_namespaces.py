import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers()

flavor_parser = subparsers.add_parser('flavor')
color_parser = subparsers.add_parser('color')

flavor_parser.add_argument('-chocolate', action='store_true')
flavor_parser.add_argument('-vanilla', action='store_true')

color_parser.add_argument('-brown', action='store_true')
color_parser.add_argument('-cream', action='store_true')

print('Given the list of arguments: flavor -chocolate color -cream')
args, rest = parser.parse_known_args(['flavor', '-chocolate', 'color', '-cream'])
print('    Parse first batch of args, put in "args" namespace\n\t', args)

# put newly-parsed tokens in existing namespace
args = parser.parse_args(rest, namespace=args)
print('    Parse remaining args, put in "args" namespace\n\t', args)
