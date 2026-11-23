import java.util.Scanner;

public class MenuCylinderEvenOdd {
  public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);
    int choice;

    do {
      System.out.println();
      System.out.println("----------Menu----------");
      System.out.println("1. Volume of cylinder");
      System.out.println("2. Check even or odd");
      System.out.println("3. Exit");
      System.out.println("------------------------");
      System.out.print("Enter your choice: ");
      choice = scanner.nextInt();

      switch (choice) {
        case 1:
          System.out.print("Enter radius: ");
          double r = scanner.nextDouble();
          System.out.print("Enter height: ");
          double h = scanner.nextDouble();

          double volume = Math.PI * r * r * h;
          System.out.printf("Volume: %.2f%n", volume);
          break;

        case 2:
          System.out.print("Enter a number: ");
          int n = scanner.nextInt();
          if (n % 2 == 0)
            System.out.println(n + " is even");
          else
            System.out.println(n + " is odd");
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
