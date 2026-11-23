import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;

public class CountriesDescending {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.print("Enter the number of countries: ");
    int n = scanner.nextInt();
    scanner.nextLine();

    String[] countries = new String[n];
    for (int i = 0; i < n; i++) {
      System.out.print("Enter country name " + (i + 1) + ": ");
      countries[i] = scanner.nextLine();
    }

    Arrays.sort(countries, Comparator.reverseOrder());

    System.out.println("Countries in descending order: ");
    for (int i = 0; i < n; i++) {
      System.out.println(countries[i]);
    }
    scanner.close();
  }
}
