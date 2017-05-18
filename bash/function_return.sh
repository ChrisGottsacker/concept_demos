# Counts the occurences of 2nd string in the 1st string
function count {
	# Note: observe that this function does not display anything to stdout
	# the first call to echo is the mechanism for returning a value from the
	# function
	echo $(echo $1 | grep -o -e $2 | wc -w)
}

str="I’m the Dude. So that’s what you call me. You know, that or, uh,
His Dudeness, or uh, Duder, or El Duderino if you’re not into the whole brevity thing."

# Note: the quotes around $str ensure that the string is passed as a single
# argument instead of as a separate argument per whitespace-separated word
c=$(count "$str" Dude)

echo 'Jeffrey Lebowski, "The Dude", once uses "Dude"' $c 'times in a couple of breaths.'
