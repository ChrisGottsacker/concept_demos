import argparse


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
parser.add_argument('-eat', action='store_true')

flavor_parser = subparsers.add_parser('flavor')

flavor_parser.add_argument('-chocolate', action='store_true')
flavor_parser.add_argument('-vanilla', action='store_true')

args1 = parser.parse_args(['-eat', 'flavor', '-chocolate'])
print('PARSED CORRECTLY: -eat flavor -chocolate\n')

# cannot parse since -eat option occurs w/n sub-parser domain
args2 = parser.parse_args(['flavor', '-chocolate', '-eat'])
