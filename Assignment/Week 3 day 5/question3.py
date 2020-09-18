#Question 3: Accept number from user and calculate the sumof all number between 1 and given number

num = int(input("Enter Any Number: "))  
  
if num < 0:  
   print("Enter positive Number")  
else:  
   sum = 0   
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  

