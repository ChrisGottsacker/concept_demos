# Compiling from within package is not allowed
SRC = pack/

# Demonstration of compiling, and also use of variables in Makefile
$(SRC)hello.class: $(SRC)hello.java pack/Goodbye.class
	javac $(SRC)hello.java

pack/Goodbye.class: pack/Goodbye.java
	javac pack/Goodbye.java

test:
	java pack/hello

clean:
	rm pack/*.class
