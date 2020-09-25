#QUES- Write a Python function that takes two lists and returns True if they have at
#least one common member.

def common_list (list1, list2):
     output = False
     for x in list1:
         for y in list2:
             if x == y:
                 output = True
                 return output
print(common_list([1,2,3,4,5], [5,6,7,8,9]))
print(common_list([1,2,3,4,5], [6,7,8,9]))