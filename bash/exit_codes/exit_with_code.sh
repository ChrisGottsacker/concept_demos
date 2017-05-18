# Usage: ./exit_with_code.sh <some command>

tmp="TMP_some_exit_code_tests.sh"

# write script to file
cat > $tmp << EOM
exit_on_failure(){
	exit_code=\$?
	if [ ! \$exit_code -eq 0 ]; then
		exit \$exit_code
	fi
}

\$1 >& out
exit_on_failure

exit 0
EOM

# test that a bad command returns fail code
./$tmp "cat fileDNE"
if [ $? -eq 0 ]; then
	echo "failure should have been detected"
fi

# test that a good command returns success code
./$tmp "cat $0"
if [ ! $? -eq 0 ]; then
	echo "success should have been detected"
fi

rm $tmp out
