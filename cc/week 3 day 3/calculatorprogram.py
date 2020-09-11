#Question 1:Write the calculator program which will take input from users two numbers And will ask them to type
#0 for addition
#1 for subtraction
#2 for multiplication
#3 for division
#And will print the result

num1 = int(input(" Enter first Number "))
num2 = int(input("Enter Second Number "))
select = int(input(" Select Operation "))
if select == 0 :
    print (num1 + num2)
elif select == 1 :
    print (num1 - num2)
elif select == 2 :
    print(num1 * num2)
elif select == 3 :
    print (num1 / num2  ) 
else:
    print ("invalid input")

