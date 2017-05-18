num=1
if [ $num -eq 1 ]; then
	echo Integers use \"-eq\" and syntactically-similar operators
else
	echo Will not print
fi

if [ ]; then
	echo Will not print
fi

if [ 0 ]; then
	echo 0 evaluates to true
fi

if [ 1 ]; then
	echo 1 also evaluates to true
fi

str="Hello"
if [ $str == "Hello" ]; then
	echo Strings are compared with \"==\"
else
	echo Will not print
fi


if [[ 0 && 0 ]]; then
	echo "Use double-brackets, [[ ]] when using logical operators lik &&"
fi
