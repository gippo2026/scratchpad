import java.util.Scanner;

public class RectangleAreaPerimeter {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter length: ");
    double length = sc.nextDouble();

    System.out.print("Enter breadth: ");
    double breadth = sc.nextDouble();

    double area = length * breadth;
    double perimeter = 2 * (length + breadth);

    System.out.printf("Area of rectangle: %.2f%n", area);
    System.out.printf("Perimeter of rectangle: %.2f%n", perimeter);

    sc.close();
  }
}
