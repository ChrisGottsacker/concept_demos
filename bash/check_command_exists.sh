# Exit if foo is not installed
if [ ! -x "$(command -v foo)" ]; then
	echo "\"foo\" is not recognized as a command"
	exit
fi
