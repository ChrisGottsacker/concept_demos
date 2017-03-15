#include <stdio.h>
#include <stdlib.h>

void foo(void* ptr){
	printf("%s", (char*)ptr);
}

int main(){
	char* bar = "Kewl, I just got promoted!\n";
	foo(bar);
}
