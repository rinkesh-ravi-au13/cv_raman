#Question 3. Given a square matrix print all the anti diagnol elements
#1 2 3 4
#5 6 7 8
#9 10 11 12
#1 2 3 4

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[1,2,3,4]]
count = len(matrix)-1 
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if j == count:
            print(matrix[i][j],end=" ")
    count-=1