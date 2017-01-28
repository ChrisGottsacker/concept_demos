import argparse

###############################################################################
## Run
##	demo_argparse.py <some text>
##	<some text>
##
##	demo_argparse.py <some text> -optionalArg <some other text>
##	<some text>
##	<some other text>
##
## Displays error if there is not one positional argument.
###############################################################################
parser = argparse.ArgumentParser()
parser.add_argument("somePositionalArg")
parser.add_argument("-optionalArg")

args = parser.parse_args()
print(args.somePositionalArg)
if args.optionalArg:
	print(args.optionalArg)
