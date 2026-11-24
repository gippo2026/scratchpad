class Employee {
  int id;
  String name, deptname;
  double salary;
  static int count = 0;

  public Employee() {
    this.id = 0;
    this.name = "Unknown";
    this.deptname = "None";
    this.salary = 0.0;
    count++;
  }

  public Employee(int id, String name, String deptname, double salary) {
    this.id = id;
    this.name = name;
    this.deptname = deptname;
    this.salary = salary;
    count++;
  }

  public static void displayCount() {
    System.out.println("Total employee objects created: " + count);
  }

  public void display() {
    System.out.printf("ID: %d | Name: %s | Dept: %s | Salary: %.2f%n", id, name, deptname, salary);
  }
}

public class EmployeeObjectCount {
  public static void main(String[] args) {
    Employee e1 = new Employee(101, "Amit", "IT", 50000);
    Employee.displayCount();

    Employee e2 = new Employee(102, "Rohit", "HR", 48000);
    Employee.displayCount();

    Employee e3 = new Employee(103, "Rahul", "Finance", 55000);
    Employee.displayCount();

    System.out.println("------ Employee Details ------");
    e1.display();
    e2.display();
    e3.display();
  }
}
