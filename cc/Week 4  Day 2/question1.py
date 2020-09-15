#Q1 Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
s = "1234abcd"
print (" The Sample string  is : ",end =" ") 
print (s) 
print (" The reversed string is : ",end= " ") 
print (reverse(s)) 