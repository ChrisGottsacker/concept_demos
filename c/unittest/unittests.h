#include <stdio.h>

#ifndef _UNITTESTS_H_
#define _UNITTESTS_H_

// #include <stdio.h>

typedef int (*testFn)(void);

int runTests( testFn fns[], int numTests){
	if(fns == NULL){ return -1; }

	int i, ret;
	for( i = 0; i < numTests; i++) {
		if( (ret = fns[i]()) < 0) {
			goto done;
		}
	}

	done:
	i < numTests? printf("FAILURE: ") : printf("SUCCESS: ");
	printf("Passed %d of %d test(s)\n", i, numTests);

	return 0;
}

int runTest( testFn fn ){
	int ret;

	fork();
	ret = fn();
	wait();
	
	return ret;
}


#endif
