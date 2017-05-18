# Usage: check_file.sh filename

if [ ! -f $1 ]; then
    echo "File \"$1\" not found!"
fi
