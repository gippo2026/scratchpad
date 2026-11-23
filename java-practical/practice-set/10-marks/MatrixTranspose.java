import java.util.Scanner;

public class MatrixTranspose {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.print("Enter the number of rows: ");
    int rows = scanner.nextInt();

    System.out.print("Enter the number of columns: ");
    int cols = scanner.nextInt();

    int[][] matrix = new int[rows][cols];
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        System.out.print("Enter element [" + i + "][" + j + "]: ");
        matrix[i][j] = scanner.nextInt();
      }
    }
    System.out.println("Original matrix: ");
    printMatrix(matrix, rows, cols);

    System.out.println("transpose of matrix: ");
    printMatrixTranspose(matrix, rows, cols);

    scanner.close();
  }

  private static void printMatrix(int[][] matrix, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        System.out.print(matrix[i][j] + "\t");
      }
      System.out.println();
    }
  }

  private static void printMatrixTranspose(int[][] matrix, int rows, int cols) {
    for (int j = 0; j < cols; j++) {
      for (int i = 0; i < rows; i++) {
        System.out.print(matrix[i][j] + "\t");
      }
      System.out.println();
    }
  }
}
