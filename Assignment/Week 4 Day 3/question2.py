#Q2. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
#Sample list : ['p', 'q']
#n =5
#Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

first_list = [' a ', ' b ']
n = 5
sec_list = ['{}{}'.format(a, b) for b in range(1, n+1) for a in first_list]
print(sec_list)

#output:-
#[' a 1', ' b 1', ' a 2', ' b 2', ' a 3', ' b 3', ' a 4', ' b 4', ' a 5', ' b 5']