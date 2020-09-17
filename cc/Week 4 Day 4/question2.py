#Write a Python script to generate and print a dictionary that contains a number(between 1 and n) 
# in the form (x, x*x)

a = int(input("Input Any Number :- "))
d2= dict() 

for x in range( 1, a+1 ): 
    d2 [x] = x * x 
    print(d2) 

# output :-
#Input Any Number :- 4
#{1: 1}
#{1: 1, 2: 4}
#{1: 1, 2: 4, 3: 9}
#{1: 1, 2: 4, 3: 9, 4: 16}
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}