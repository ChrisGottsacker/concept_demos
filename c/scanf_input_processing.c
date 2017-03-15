#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

// Reads in a line of input, and stores each word in an array

int main(){
	char* nextWord = NULL;
	int numCharsRead;

	while(1){
		errno = 0;
		numCharsRead = fscanf(stdin, "%ms", &nextWord);
		if(errno != 0){
			printf("Error while reading\n");
		}
		else if(numCharsRead == EOF){
			printf("EOF reached, done reading\n");
			free(nextWord);
			exit(0);
		}
		else if(numCharsRead > 0){
			printf("Input parsed: \"%s\"\n", nextWord);
			free(nextWord);
		}
	}
	return 0;
}
