#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[]){
	typedef struct {
		size_t numItems;
		size_t maxNumItems;
		char** ptr;
		// char* ptr[];	causes error below

	} ARRAY;

	ARRAY lines;
	lines.numItems = 0;
	lines.maxNumItems = 16;
	
	// error: invalid use of flexible array member
	lines.ptr = malloc(lines.maxNumItems*sizeof(char));

}
