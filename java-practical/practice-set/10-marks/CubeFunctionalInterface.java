import java.util.Scanner;

@FunctionalInterface
interface CubeOp {
  int cube(int n);
}

public class CubeFunctionalInterface {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter a number: ");
    int num = sc.nextInt();

    CubeOp op = n -> n * n * n;
    System.out.println("Cube of " + num + " = " + op.cube(num));
    sc.close();
  }
}
