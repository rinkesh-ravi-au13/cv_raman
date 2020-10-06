
# Q1. Reverse a string using recurssion

def reverse_string(string):
    if len(str(string))==0:
        return string
    else:
        return reverse_string(string[1:])+string[0]
    

a= str(input("Enter String To Reverse:  "))
print(reverse_string(a))