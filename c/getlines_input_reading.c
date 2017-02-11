#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(){
	size_t bufferSize = NULL;
	char* nextLine = NULL;
	int readStatus;

	while(1){
		errno = 0;
		readStatus = getline(&nextLine, &bufferSize, stdin);
		if(errno != 0){
			printf("Error while reading\n");
		}
		else if(readStatus == -1){
			printf("EOF reached, done reading\n");
			free(nextLine);
			exit(0);
		}
		else{
			printf("Input read: %s", nextLine);
		}
	}

}
