#Question 1:Write a user driven program which will print the tables of a no given 
# by user?


num = int(input("Enter the number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num,"X",i,"=",num * i)