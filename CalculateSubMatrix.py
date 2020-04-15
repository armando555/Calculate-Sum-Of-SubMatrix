#This function calculate the sum a matrix from (0,0) to bottom right of a matrix


def sumCompleteMatrix(mat):
    sum=0
    for i in range(0,len(mat)):
        for j in range (0,len(mat[i])):
            sum+=mat[i][j]
    return sum
#This function calculate the sum from i to j


def sumItoJ(i,j):
    neto=0
    for m in range(i,j+1):
        neto+=m
    return neto


print(sumCompleteMatrix([[1,2,3],[4,5,6]])==sumItoJ(1,6))
