# question 3:- https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# solution :-
def split_and_join(line):
    # write your code here
    line=line.split(" ")
    line="-".join(line)
    return line