#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define ARRAYLIST_TYPE int
typedef struct arraylist{
	size_t numItems;
	size_t maxNumItems;
	ARRAYLIST_TYPE* items;
} ARRAYLIST;

void appendToArraylist(ARRAYLIST* listptr, ARRAYLIST_TYPE item);
ARRAYLIST* newArraylist();
ARRAYLIST* resizeArraylist(ARRAYLIST* listptr);
void deleteArraylist(ARRAYLIST* listptr);

int main(){
	// printf("%lu = 2*%lu + %lu\n", sizeof(a), sizeof(size_t), sizeof(ARRAYLIST_TYPE*));
	ARRAYLIST* numsptr = newArraylist();
	appendToArraylist(numsptr, 27);
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
	listptr->items = malloc(listptr->maxNumItems*sizeof(ARRAYLIST_TYPE));
	if(errno != 0){
		fprintf(stderr, "%s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}
	return listptr;
}

void appendToArraylist(ARRAYLIST* listptr, ARRAYLIST_TYPE item){
	if(listptr->numItems == listptr->maxNumItems){
		resizeArraylist(listptr);
	}

	// add line to array
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
	ARRAYLIST_TYPE * tmp = realloc(listptr->items, listptr->maxNumItems * sizeof(ARRAYLIST_TYPE));
	if(errno != 0){
		fprintf(stderr, "%s\n", strerror(errno));
		exit(EXIT_FAILURE);
	}
	else{
		listptr->items = tmp;
	}
}
