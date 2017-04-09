#include <stdio.h>

typedef int (*testFn)(void);

int runTests( testFn fns[] ){
	if(fns == NULL){ return -1; }

	int i, ret;
	int numTests = sizeof(fns)/sizeof(fns[0]);
	for( i = 0; i < numTests; i++) {
		if( (ret = fns[i]()) < 0) {
			goto done;
		}
	}

	done:
	i < numTests? printf("FAILURE: ") : printf("SUCCESS: ");
	printf("Passed %d test(s), Failed %d test(s)\n", i, numTests - i);

	return 0;
}

int runTest( int (*fn)(void)){
	int ret;
	fork();
	ret = fn();
	wait();
	return ret;
}

int testTemplate(){
	// set up
	// run test
	// tear down
	// only get here if test succeeded
	return 0;

	bad:
	return -1;
}

int main(int argc, char *argv[])
{
	testFn tests[] = {
		&testTemplate,
	};
	runTests(tests);
	return 0;
}
