#Question 1: Write a loop to find the factorial of any number
#loop program to find factorial of a number
num = int(input("Enter any  number: "))
fac = 1

for i in range (1, num+1):
    fac = fac * i
    print ("Factorial of the number %d is %d" %(num, fac))
  g