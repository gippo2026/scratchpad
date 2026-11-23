import java.util.Scanner;

public class ReverseArray {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.print("Enter the number of elements: ");
    int n = scanner.nextInt();

    int[] array = new int[n];
    for (int i = 0; i < n; i++) {
      System.out.print("Enter element " + (i + 1) + ": ");
      array[i] = scanner.nextInt();
    }

    System.out.println("Array elements: ");
    for (int i = 0; i < n; i++) {
      System.out.print(array[i] + " ");
    }
    System.out.println();

    System.out.println("Array elements in reverse order: ");
    for (int i = n - 1; i >= 0; i--) {
      System.out.print(array[i] + " ");
    }
    System.out.println();
    scanner.close();
  }
}
