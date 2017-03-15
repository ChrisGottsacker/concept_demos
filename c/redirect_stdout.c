#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){
	int savedStdout = dup(STDOUT_FILENO);
	int output = open("new.out", O_WRONLY | O_CREAT | O_TRUNC, 0644);
	if(output == -1){
		exit(1);
	}
	if(dup2(output, STDOUT_FILENO) == -1){
		exit(1);
	}
	close(output);

	printf("this goes to file via file descriptor %d\n", output);
	fflush(stdout);	// needed, otherwise ends up printing to stdout

	if(dup2(savedStdout, STDOUT_FILENO) == -1){
		exit(1);
	}
	printf("this goes to stdout\n");
	return 0;
}
