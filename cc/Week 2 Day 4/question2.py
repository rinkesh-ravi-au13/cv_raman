#Question 2 - Write a Python function to find the Max of three numbers?
def maximum(a, b, c): 
    list = [a, b, c] 
    return max(list) 
x = int(input("Enter First Number :- "))
y = int(input("Enter Second Number :- "))
z = int(input("Enter Third Number :- "))
print("Maximum Number Of The Three is :- " ,maximum(x, y, z)) 