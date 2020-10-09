#question 2 :- https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    newstring=''
    for letter in s:
        if letter.isupper():
            newstring=newstring+letter.lower()
        else:
            newstring=newstring+letter.upper()
        
    return newstring