#Question 2. Given a matrix print the all the horizontal rows
#1 2 3 4
#5 6 7 8
#9 10 11 12

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
row=len(matrix)
for i in range(row):
    print("Row ",i+1," :", end=" ")
    for j in matrix[i]:
        print(j, end=" ")
    print()