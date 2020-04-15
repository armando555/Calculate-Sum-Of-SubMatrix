#This function calculate the sum a matrix from (0,0) to bottom right of a matrix
def sumCompleteMatrix(mat,point1,point2):
    sum=0
    if point1==len(mat):
        point1++
    for i in range(0,point1):
        if point2==len(mat[i]) and i==0:
            point2++
        for j in range (0,len(point2):
            sum+=mat[i][j]
    return sum
#This function calculate the sum from i to j
def sumItoJ(i,j):
    neto=0
    for m in range(i,j+1):
        neto+=m
    return neto

def generarMatriz():
	colum = input("Enter the colum size")


if __name__=="__main__":
	generarMatriz()

print(sumCompleteMatrix([[1,2,3],[4,5,6],[7,8,9]])==sumItoJ(1,6))
