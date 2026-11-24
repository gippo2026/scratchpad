import java.io.*;
import java.util.Scanner;

public class ReadIntegersSum {
  public static void main(String[] args) {
    int sum = 0;
    try (Scanner sc = new Scanner(new File("numbers.txt"))) {
      System.out.println("Numbers in numbers.txt: ");
      while (sc.hasNextInt()) {
        int num = sc.nextInt();
        System.out.println(num);
        sum += num;
      }
      System.out.println("Sum of all integers = " + sum);
    } catch (FileNotFoundException e) {
      System.out.println("File numbers.txt not found: " + e.getMessage());
    }
  }
}
