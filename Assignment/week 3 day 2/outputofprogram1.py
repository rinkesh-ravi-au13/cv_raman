#Q2. What will be the output of the below program
age = 10
if (True):
 if (age == 10):
    print(1)
 else:
      print(2)
 if (age * 4 > 20):
     print(3)
     print(4)
 elif (age * 2 >= 20):
     print(5)
     print(6)
 else:
     print(7)
     print(8)
if (age == 10):
    print(9)
    print(10)
    print(11)

#output of the program is:-
# 1
# 3
# 4
# 9
# 10
# 11