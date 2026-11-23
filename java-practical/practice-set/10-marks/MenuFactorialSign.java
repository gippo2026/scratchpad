import java.util.Scanner;

public class MenuFactorialSign {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int choice;

    do {
      System.out.println();
      System.out.println("----------Menu----------");
      System.out.println("1. Factorial of a number");
      System.out.println("2. Check positive or negative");
      System.out.println("3. Exit");
      System.out.println("------------------------");
      System.out.print("Enter your choice: ");
      choice = scanner.nextInt();

      switch (choice) {
        case 1:
          System.out.print("Enter a number: ");
          int n = scanner.nextInt();
          long fact = 1;
          for (int i = 1; i <= n; i++) {
            fact *= i;
          }
          System.out.println("Factorial: " + fact);
          break;

        case 2:
          System.out.print("Enter a number: ");
          int x = scanner.nextInt();
          if (x > 0) {
            System.out.println("The number is positive");
          } else if (x == 0) {
            System.out.println("The number is zero");
          } else {
            System.out.println("The number is negative");
          }
          break;

        case 3:
          System.out.println("Exiting...");
          break;

        default:
          System.out.println("Invalid choice");
      }
    } while (choice != 3);
    scanner.close();
  }
}
