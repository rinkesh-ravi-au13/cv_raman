# Q3. Write a program to calculate the power of a number using recursion in O(Log(n))complexity.
def power(num,p):
    if (p==0) :
        return 1
    elif int(p%2) == 0:
        return power(num,int(p/2)) * power(num,int(p/2))
    else:
        return num * power(num,int(p/2)) * power(num,int(p/2))
    
x = int(input("Enter Any Number :- ")) 
y = int(input("Enter power:- ")) 

print(power(x,y))