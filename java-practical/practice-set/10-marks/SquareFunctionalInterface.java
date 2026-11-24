import java.util.Scanner;

@FunctionalInterface
interface SquareOp {
  int square(int n);
}

public class SquareFunctionalInterface {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter a number: ");
    int num = sc.nextInt();

    SquareOp op = n -> n * n;
    System.out.println("Square of " + num + " = " + op.square(num));
    sc.close();
  }
}
