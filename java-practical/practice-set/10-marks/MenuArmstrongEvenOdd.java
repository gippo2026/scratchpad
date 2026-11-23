import java.util.Scanner;

public class MenuArmstrongEvenOdd {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int choice;

    do {
      System.out.println();
      System.out.println("----------Menu----------");
      System.out.println("1. Armstrong Check");
      System.out.println("2. Even or odd");
      System.out.println("3. Exit");
      System.out.println("------------------------");

      System.out.print("Enter your choice: ");
      choice = sc.nextInt();

      switch (choice) {
        case 1:
          System.out.print("Enter a number: ");
          int n = sc.nextInt();
          int temp = n;
          int sum = 0;
          while (temp > 0) {
            int d = temp % 10;
            sum = sum + d * d * d;
            temp = temp / 10;
          }
          if (sum == n) {
            System.out.println(n + " is an Armstrong number");
          } else {
            System.out.println(n + " is not an Armstrong number");
          }
          break;

        case 2:
          System.out.print("Enter a number: ");
          int x = sc.nextInt();

          if (x % 2 == 0) {
            System.out.println("The number " + x + " is even");
          } else {
            System.out.println("The number " + x + " id odd");
          }
          break;

        case 3:
          System.out.println("Exiting...");
          break;

        default:
          System.out.println("Invalid option");
      }
    } while (choice != 3);
    sc.close();
  }
}
