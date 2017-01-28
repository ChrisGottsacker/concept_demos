IF 1 LSS 2 echo true
IF 3 EQU 3 echo true
IF 3 NEQ 2 echo true
IF 2 LEQ 2 echo true
IF 2 GTR 1 echo true
IF 2 GEQ 1 echo true

SETLOCAL

SET TRUE=0==0
IF %TRUE% (
	echo gets displayed
)

SET FALSE=NOT %TRUE%
IF %FALSE% (
	echo doesn't get displayed
)
