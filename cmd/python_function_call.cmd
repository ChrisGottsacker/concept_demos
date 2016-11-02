SETLOCAL
SET "str= 'words woRDS WOrds'"
cls
python -c "s = 'These are my ' + %str%; print(s)"
