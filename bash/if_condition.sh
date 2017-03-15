num=2
if [ $num -eq 1 ]; then
	echo Yay! num equals 1
else
	echo Huh, num equals $num
fi


str="Hello"
if [ $str == "Hello" ]; then
	echo $str World!
else
	echo "Fine, don't say 'Hello' to me"
