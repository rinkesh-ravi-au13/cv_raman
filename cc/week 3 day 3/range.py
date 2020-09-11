#Question 2:Explain range in python with various examples ..
#range() function syntax and arguments:-

#range(start, stop[, step])

#It takes three arguments.Out of the three 2 arguments are optional. I.e., start and step are the 
#optional arguments.
#A start argument is a starting number of the sequence. i.e., lower limit. By default, it starts with 0
#if not specified.
#A stop argument is an upper limit. i.e., generate numbers up to this number, The range() doesn’t include
#this number in the result.
#The step is a difference between each number in the result. The default value of the step is 1 if not 
#specified.

###range() function Examples :-

#Let see all the possible scenarios now. Below are the three variant of range() function.
#Example one – Using only one argument
# Print first 5 numbers using range function
for i in range(5):
    print(i, end=', ')
##Output will be :-0, 1, 2, 3, 4,
#Only a stop argument is passed to range() . So by default, it takes start = 0 and step = 1.
###Example Two – using two arguments (i.e., start and stop):-

# Print integers within given start and stop number using range()
for i in range(5, 10):
    print(i, end=', ')
##output is :-5, 6, 7, 8, 9,
#Note: By default, it took step value as 1.

###Example Three – using all three arguments :--

# using start, stop, and step arguments in range()
#print("Printing All even numbers between 2 and 10 using range()")
for i in range(2, 10, 2):
    print(i, end=', ')
##Output is:- Printing All even numbers between  and 10 using range() i.e 2, 4, 6, 8,
#All three arguments are specified i.e., start = 2, stop = 10, step = 2.  The step value is 2 so the 
#difference between each number is 2.