# 4170-Trading-Challenge
Coding challenge for 4170 Trading

There are 3 files containing the solutions to each of the problems in the exercise: Problem1.py, Problem2.py, and Problem3.py.

Problem1 can be run using command "python Problem1.py". The target value is filled in as 500, as per the problem description. However, it is possible to test this dynamic programming algorithm with any target value. The result is printed at the end. The expected answer is 120536. The expected runtime is less than a second.

Problem 2 uses the built-in itertools module. There is a helper function called permuations that uses the product method from itertools to calculate the number of permuations for each sum made by the two types of dice. The program can be run using the command "python Problem2.py". The result is printed at the end. The expected answer is ~58.3%. The expected runtime is ~75 seconds.

Problem 3 can be run using the command "python Problem3.py". The result is printed at the end. The expected answer is 13938. The expected runtime is less than a second.
Note: I was asked to not use the munkres library. My solution without the library is in Problem3_.py, which is unfinished but implements (most of) the Hungarian algorithm.

Each exercise was done in Python 3.
