#include <stdio.h>
#include <stdlib.h>

int main(){
	int * a;
	a = (int *) malloc(sizeof(int));
	*a = 1;
	*a = *a + *a;
	printf("%d", *a);
}
