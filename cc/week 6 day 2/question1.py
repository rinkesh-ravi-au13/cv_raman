
#Question 1. Given a matrix print the all the vertical columns
#1 2 3 4
#5 6 7 8
#9 10 11 12

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range(len(matrix)+1): 
    print("col",i+1,":",end=" ")    
    for j in matrix:
        print(j[i],end=" ")
    print()