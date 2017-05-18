tmp="foo"

# writes lines b/n the two "EOF" strings
cat > $tmp << EOF
echo args: \$*
EOF

# executes script that was just written to file
./$tmp some args
rm $tmp
