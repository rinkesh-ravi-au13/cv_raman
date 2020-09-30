class Solution :
    def diagonalSum (self, mat : List[List[int]]) -> int:
        primary_diagonal= len (mat) -1
        secondary_diagonal = 0 
        sum1 =0
        for i in range (len(mat)):
            for j in range (len(mat)):
                if j == primary_diagonal or j == secondary_diagonal :
                    sum1 += mat[i][j]
            primary_diagonal -= 1
            secondary_diagonal += 1 
        return sum1