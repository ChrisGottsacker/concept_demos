/* This line was redirected from file
...another line redirected from file */

#include <fcntl.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void readInput();

int main(){
	int savedStdin = dup(STDIN_FILENO);

	int input = open("redirect_stdin.c", O_RDONLY);
	if(input == -1){
		printf("Error while opening file\n");
		exit(1);
	}
	if(dup2(input, STDIN_FILENO) == -1){
		exit(1);
	}
	close(input);
	readInput();

	// ideally this would restore stdin to normal...not sure why it doesn't
	if(dup2(savedStdin, STDIN_FILENO) == -1){
		exit(1);
	}
	readInput();

	return 0;
}

void readInput(){
	char* nextWord = NULL;
	int numCharsRead;
	errno = 0;
	numCharsRead = fscanf(stdin, "%m[^\n]%c*", &nextWord);
	if(errno != 0){
		printf("Error while reading\n");
	}
	else if(numCharsRead == EOF){
		printf("EOF reached, done reading\n");
		free(nextWord);
		return;
	}
	else if(numCharsRead > 0){
		printf("Input read: \"%s\"\n", nextWord);
		free(nextWord);
	}
}
