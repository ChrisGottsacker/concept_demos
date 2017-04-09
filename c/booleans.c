#include <stdio.h>

typedef char bool;
#define TRUE 1
#define FALSE 0

int main(){
	if(TRUE){
		printf("%s", "true\n");
	}
	if(!FALSE){
		printf("%s", "not false\n");
	}
	return 0;
}
