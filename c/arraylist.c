#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

typedef struct arraylist{
	size_t numItems;
	size_t maxNumItems;
	void** items;
} ARRAYLIST;


void appendToArraylist(ARRAYLIST* listptr, void* item);
ARRAYLIST* newArraylist();
ARRAYLIST* resizeArraylist(ARRAYLIST* listptr);
void deleteArraylist(ARRAYLIST* listptr);

int main(){
	// printf("%lu = 2*%lu + %lu\n", sizeof(a), sizeof(size_t), sizeof(void**));
	ARRAYLIST* numsptr = newArraylist();
	int foo = 27;
	appendToArraylist(numsptr, &foo);
	printf("%d == %d?\n", foo, *((int*)numsptr->items[0]));
	deleteArraylist(numsptr);
}

ARRAYLIST* newArraylist(){
	// allocate space for struct
	errno = 0;
	ARRAYLIST* listptr = malloc(sizeof(ARRAYLIST));
	if(errno != 0){
		fprintf(stderr, "%s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}

	// initialize counters
	listptr->numItems = 0;
	listptr->maxNumItems = 16;

	// allocate space for array
	errno = 0;
	listptr->items = malloc(listptr->maxNumItems*sizeof(void*));
	if(errno != 0){
		fprintf(stderr, "%s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}
	return listptr;
}

void appendToArraylist(ARRAYLIST* listptr, void* item){
	if(listptr->numItems == listptr->maxNumItems){
		resizeArraylist(listptr);
	}

	listptr->items[listptr->numItems] = item;
	listptr->numItems++;
}

void deleteArraylist(ARRAYLIST* listptr){
	free(listptr->items);
	free(listptr);
}

ARRAYLIST* resizeArraylist(ARRAYLIST* listptr){
	errno = 0;
	listptr->maxNumItems *= 2;
	void* * tmp = realloc(listptr->items, listptr->maxNumItems * sizeof(void*));
	if(errno != 0){
		fprintf(stderr, "%s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}
	else{
		listptr->items = tmp;
	}
	return listptr;
}
