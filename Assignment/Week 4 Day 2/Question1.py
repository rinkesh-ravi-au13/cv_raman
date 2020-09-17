#Q1. Write a Python function that accepts a string and calculate the number ofupper case letters and 
# lower case letters.

def upper_lower(s):      
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for i in s if i.islower())
    print( "The number of Upper case characters is  %s and the number of Lower case characters is  %s ." % (upper ,lower ))
upper_lower(" My Name Is rinkesh Kumar Ravi ")

#output:-
#he number of Upper case characters is  5 and the number of Lower case characters is  19 