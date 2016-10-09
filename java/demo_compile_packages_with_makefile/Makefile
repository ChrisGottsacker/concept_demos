SRC = pack/

$(SRC)hello.class: $(SRC)hello.java pack/Goodbye.class
	javac $(SRC)hello.java

pack/Goodbye.class: pack/Goodbye.java
	javac pack/Goodbye.java

test:
	java pack/hello

clean:
	rm pack/*.class
