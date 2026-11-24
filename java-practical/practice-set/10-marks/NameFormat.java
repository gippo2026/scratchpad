import java.util.Scanner;

public class NameFormat {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.print("Enter first, middle and last name: ");
    String first = scanner.next();
    String middle = scanner.next();
    String last = scanner.next();

    String mid = "";
    if (middle.length() > 0) {
      mid = middle.substring(0, 1).toUpperCase() + middle.substring(1).toLowerCase();
    }
    System.out.println(last + ", " + first + " " + mid);
    scanner.close();
  }
}
