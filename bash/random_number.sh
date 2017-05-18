# Displays a message if the generated random number falls w/n a window
x=7	# i.e. if x=5, there is a 1 in 5 chance that the message will be displayed
if [ $RANDOM -le $((32767/$x)) ]; then	# 32767 is the max value for random numbers
	echo "There was a one in $x chance, and it happened"
fi
