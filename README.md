# Description
This repository was created to demonstrate my understanding of 
important problems/algorithms and pytest.

## Set Up
To add new algorithms all you have to do is import them into the test_sort file
and then add them to the available dictionary as a key: value pair where the key
is a string name for the algorithm and the value is the function itself. This will
automatically be imported into the run_test file.

## Instructions
There is one test file with three test classes that can be used by
any sorting algorithm. There are two ways to run the tests.

1. ### Using terminal
If you call pytest from terminal in the directory it will run whichever 
algorithm is currently saved in the config file. 

2. ### Using run_test
If you run the run_test module you will be prompted to choose which 
algorithm you want to test based on a dictionary of available algorithms 
in the test_sort file. After running a test you will be able to change
the algorithm and run more tests. 

 