#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]){
	typedef struct string{
		int size;
		char* val;
	} STRING;

	STRING s;
	s.val = "hi";
	s.size = strlen(s.val);

	printf("\"%s\" has length %d\n", s.val, s.size);
}
