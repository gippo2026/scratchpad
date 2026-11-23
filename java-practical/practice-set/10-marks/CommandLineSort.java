import java.util.Arrays;

public class CommandLineSort {
  public static void main(String[] args) {
    if (args.length != 5) {
      System.out.println("Error: Exactly 5 numbers must be supplied as command-line arguments.");
      return;
    }

    int[] numbers = new int[5];
    try {
      for (int i = 0; i < 5; i++) {
        numbers[i] = Integer.parseInt(args[i]);
      }
    } catch (NumberFormatException e) {
      System.out.println("Error: all 5 arguments must be valid integers");
      return;
    }

    Arrays.sort(numbers);
    System.out.println("Sorted numbers(ascending):");
    for (int number : numbers) {
      System.out.println(number);
    }
  }
}
