#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>	// for getpid()
#include <sys/wait.h>	// for getpid()

/*
 * Demonstrates that execvp() makes a copy of program arguments, and does not
 * merely point to the existing strings
 */
int main(int argc, char** argv){
	if(argc == 1){	// only fork the first time this program runs
		// string is available to both parent and child processes
		char* args[] = {"./execvp_args", "sup, I'm your kid!"};

		pid_t id = fork();
		if(id < 0){
			printf("Fork failed\n");
		}
		else if(id == 0){	// child process
			printf("Before execvp(), 1st arg: \"%s\" is at address: %p\n", args[1], &args[1]);
			execvp(args[0], args);
		}
		else{	// parent process
			int status;
			wait(&status);
			printf("In parent process, 1st arg: \"%s\" is at address: %p\n", args[1], &args[1]);
		}
	}
	else{	//
		printf("After execvp(), 1st arg: \"%s\" is at address: %p\n", argv[1], &argv[1]);
	}
}
