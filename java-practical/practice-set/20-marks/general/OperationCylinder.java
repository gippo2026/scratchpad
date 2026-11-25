import java.util.Scanner;

interface Operation {
  double PI = 3.142;

  double area();

  double volume();
}

class Cylinder implements Operation {
  double radius, height;

  public Cylinder(double radius, double height) {
    this.radius = radius;
    this.height = height;
  }

  @Override
  public double area() {
    return 2 * PI * radius * (radius + height);
  }

  @Override
  public double volume() {
    return PI * radius * radius * height;
  }
}

public class OperationCylinder {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter radius: ");
    double radius = sc.nextDouble();
    System.out.print("Enter height: ");
    double height = sc.nextDouble();

    Cylinder cy = new Cylinder(radius, height);
    System.out.printf("Area: %.2f%n", cy.area());
    System.out.printf("Volume: %.2f%n", cy.volume());
    sc.close();
  }
}
