numExpectedArgs=1
if [ $# -ne $numExpectedArgs ]; then
	echo Usage: $0 some_arg
	exit
else
	echo Correct num args given
fi
