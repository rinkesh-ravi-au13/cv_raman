#question 6:- https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    return ' '.join(i.capitalize()  for i in s.split(' '))