import java.util.Scanner;

public class CalculateSubMatrix{

  private int matrix [][];
  private int sum [][];
  public CalculateSubMatrix (){
    Scanner sc = new Scanner (System.in);
    System.out.print("Enter de Rows Size ");
    int rows = sc.nextInt();
    System.out.print("Enter de Colums Size ");
    int colums = sc.nextInt();
    matrix = new int[rows][colums];
    sum = new int[rows][colums];

    for (int i = 0;i<colums;i++){
        for (int j =0;j<rows;j++){
          matrix [i][j] = 1;
        }
    }

    calculateSum();
    printMatrix();
    System.out.println();
    System.out.println("enter the first Coordinate ");
    String coord1=sc.next();
    System.out.println("enter the second Coordinate ");
    String coord2=sc.next();

    int i1,j1,i2,j2;
    String cord1[]= coord1.split(",");
    String cord2[]= coord2.split(",");

    i1 = Integer.parseInt(cord1[0]);
    j1 = Integer.parseInt(cord1[1]);
    i2 = Integer.parseInt(cord2[0]);
    j2 = Integer.parseInt(cord2[1]);

    System.out.println(i1+" "+j1+" "+i2+" "+j2);
    int sumReturn = sum[i2][j2]-sum[i1-1][j2-1]-sum[i2][j1]+sum[i1][j1]-matrix[i1][j1];
    System.out.println(sumReturn);

  }
  public static void main (String args[]){
    CalculateSubMatrix csm = new CalculateSubMatrix();
  }

  public void calculateSum (){
    sum [0][0] = matrix[0][0];

    for (int i = 1;i<matrix.length;i++){
      sum[i][0]=matrix[i][0]+sum[i-1][0];
    }
    for (int i = 1;i<matrix[0].length;i++){
      sum[0][i]=matrix[0][i]+sum[0][i-1];
    }

    for (int i = 1;i<matrix.length;i++){
      for (int j = 1;j<matrix[0].length;j++){
        sum[i][j]= matrix[i][j]-sum[i-1][j-1]+sum[i-1][j]+sum[i][j-1];
      }
    }
  }
  public void printMatrix(){

    for (int i =0;i<matrix.length;i++){
      for (int j =0;j<matrix[0].length;j++){
        System.out.print(sum[i][j]+String.valueOf('\t'));
      }
      System.out.println();
    }


  }

}
