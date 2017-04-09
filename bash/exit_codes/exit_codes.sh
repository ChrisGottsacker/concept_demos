EXIT_SUCCESS=0
OUT=blah

displayExitStatus(){
	exit_code=$?
	if [ ! $exit_code -eq $EXIT_SUCCESS ]; then
		echo failed with exit code: $exit_code
	fi
}

python bad_import.py >& $OUT
displayExitStatus

cat fileDNE >& $OUT
displayExitStatus

# python experiments
python bare_exit.py
displayExitStatus

python succeed_forced.py
displayExitStatus

python succeed_natural.py
displayExitStatus

rm $OUT

# NOTES
	# use of '&' runs process in background
	# use of '>&' redirects stderr
