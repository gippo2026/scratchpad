import java.util.Scanner;

abstract class Order {
  int id;
  String description;

  abstract void accept(Scanner sc);

  abstract void display();
}

class PurchaseOrder extends Order {
  String customerName;

  void accept(Scanner sc) {
    System.out.print("ID: ");
    id = sc.nextInt();
    sc.nextLine();
    System.out.print("Description: ");
    description = sc.nextLine();
    System.out.print("Customer Name: ");
    customerName = sc.nextLine();
  }

  void display() {
    System.out.println(
        "PurchaseOrder [ID =" + id + ", Description: " + description + ", Customer Name: " + customerName + "]");
  }
}

class SalesOrder extends Order {
  String vendorName;

  void accept(Scanner sc) {
    System.out.print("ID: ");
    id = sc.nextInt();
    sc.nextLine();
    System.out.print("Description: ");
    description = sc.nextLine();
    System.out.print("Vendor Name: ");
    vendorName = sc.nextLine();
  }

  void display() {
    System.out
        .println("SalesOrder [ID =" + id + ", Description: " + description + ", Vendor Name: " + vendorName + "]");
  }
}

public class AbstractOrderSubclasses {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    PurchaseOrder[] po = new PurchaseOrder[3];
    SalesOrder[] so = new SalesOrder[3];

    System.out.println("Enter 3 Purchase Orders: ");
    for (int i = 0; i < 3; i++) {
      po[i] = new PurchaseOrder();
      po[i].accept(sc);
    }

    System.out.println("\nEnter three Sales Orders: ");
    for (int i = 0; i < 3; i++) {
      so[i] = new SalesOrder();
      so[i].accept(sc);
    }

    System.out.println("\n--- Purchase Orders ---");
    for (PurchaseOrder p : po)
      p.display();

    System.out.println("\n--- Sales Orders ---");
    for (SalesOrder s : so)
      s.display();

    sc.close();
  }
}
