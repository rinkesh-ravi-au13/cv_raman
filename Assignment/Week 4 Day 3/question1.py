#Q1.Write a Python program to round the numbers of a given list, print the minimumand maximum numbers 
# and multiply the numbers by 5. Print the unique numbers
#in ascending order separated by space.
#Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
#Minimum value: 4
#Maximum value: 22
#Result:
#20 25 45 55 60 70 80 90 110

numbers = [20.81, 7.1, 14.87, 8.16, 19.00, 13.29, 35.44, 2.20, 18.56]
print("Numbers In The List :-", numbers)
numbers = list ( map ( round , numbers ))
print("Minimum value In The List :- ", min ( numbers ))
print("Maximum value In Th List :- ", max ( numbers ))
numbers = list ( set ( numbers ))
numbers = ( sorted ( map (lambda n : n*5, numbers )))
print("Required Result :-")
for numb in numbers :
    print ( numb, end=' ')

