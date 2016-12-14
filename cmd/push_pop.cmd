:: push current address, go somewhere else
SETLOCAL

SET prevDir=%cd%
cd E:\
echo %cd%
cd %prevDir%
