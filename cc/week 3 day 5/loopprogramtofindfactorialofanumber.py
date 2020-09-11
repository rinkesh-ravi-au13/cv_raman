#Question 1: Write a loop to find the factorial of any number
#loop program to find factorial of a number

num = int(input("enter Any number: "))
 
factorial = 1
 
for i in range(1, num + 1):
	factorial = factorial * i
 
print("factorial of ", num, " is ", factorial)
  