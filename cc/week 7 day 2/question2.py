# Q2. Calculate factorial using recursion

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
a=factorial(int(input("Enter Number To Get The Factorial Value :- ")))
print(a)