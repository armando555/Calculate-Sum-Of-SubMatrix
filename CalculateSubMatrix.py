#This function calculate the sum a matrix from (0,0) to bottom right of a matrix
def sumCompleteMatrix(mat,point1,point2):
    sum=0
    for i in range(0,point1+1):
        for j in range (0,point2+1):
            sum+=mat[i][j]
#            print(mat[i][j])
    return sum
#This function calculate the sum from i to j

def sumItoJ(i,j):
    neto=0
    for m in range(i,j+1):
        neto+=m
    return neto


#This function calculate the sum from (point1L,point2L) to (point1R,point2R)
def sumCompleteSubMatrix(mat,point1L,point2L,point1R,point2R):
    sum=0
    for i in range(point1L,point1R+1):
        for j in range (point2L,point2R+1):
            sum+=mat[i][j]
#            print(mat[i][j])
    return sum
def main(mat,point1L,point2L,point1R,point2R):
    suma1=sumCompleteMatrix(mat,point1R,point2R)-sumCompleteMatrix(mat,point1R,point2L-1)-sumCompleteMatrix(mat,point1L-1,point2R)+sumCompleteMatrix(mat,point1L-1,point2L-1)
    return suma1
if __name__=="__main__":
    print(sumCompleteSubMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]],2,1,3,2)==main([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]],2,1,3,2))
    print("main=",main([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]],2,1,3,2))
    print("subMatrix=",sumCompleteSubMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]],2,1,3,2))
