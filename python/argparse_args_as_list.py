import argparse

###############################################################################
## Run
##	demo_argparse.py -f <some text> -f <some other text>
##	['<some text>', '<some other text>']
##
## Displays error if there is not one positional argument.
###############################################################################
parser = argparse.ArgumentParser()
parser.add_argument("-f", action='append')

args = parser.parse_args()
print(args.f)
