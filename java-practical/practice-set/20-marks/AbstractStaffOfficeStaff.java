import java.util.Scanner;

abstract class Staff {
  protected int id;
  protected String name;

  public Staff(int id, String name) {
    this.id = id;
    this.name = name;
  }

  public abstract void display();
}

class OfficeStaff extends Staff {
  String department;

  public OfficeStaff(int id, String name, String department) {
    super(id, name);
    this.department = department;
  }

  @Override
  public void display() {
    System.out.println("ID: " + id + " | Name: " + name + " | Department: " + department);
  }
}

public class AbstractStaffOfficeStaff {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter number of office staff: ");
    int n = sc.nextInt();

    OfficeStaff[] arr = new OfficeStaff[n];

    for (int i = 0; i < n; i++) {
      System.out.print("ID: ");
      int id = sc.nextInt();
      sc.nextLine();
      System.out.print("Name: ");
      String name = sc.nextLine();
      System.out.print("Department: ");
      String department = sc.nextLine();

      arr[i] = new OfficeStaff(id, name, department);
    }
    System.out.println("\n------ Office Staff Members ------");
    for (OfficeStaff os : arr)
      os.display();
    sc.close();
  }
}
