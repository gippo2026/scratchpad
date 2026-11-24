import java.util.Scanner;

class Student {
  int roll_no;
  String name;
  double percentage;

  public Student(int roll_no, String name, double percentage) {
    this.roll_no = roll_no;
    this.name = name;
    this.percentage = percentage;
  }

  public static void sortStudent(Student[] arr) {
    for (int i = 0; i < arr.length - 1; i++) {
      for (int j = 0; j < arr.length - 1 - i; j++) {
        if (arr[j].percentage > arr[j + 1].percentage) {
          Student temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
  }

  public void display() {
    System.out.printf("Roll no: %d | Name: %-15s | Percentage: %.2f%%%n", roll_no, name, percentage);
  }
}

public class StudentSortPercentage {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter number of students: ");
    int n = sc.nextInt();
    Student[] list = new Student[n];

    for (int i = 0; i < n; i++) {
      System.out.println("\nStudent " + (i + 1) + ":");
      System.out.print("Roll no: ");
      int r = sc.nextInt();
      sc.nextLine();
      System.out.print("Name: ");
      String nme = sc.nextLine();
      System.out.print("Percentage: ");
      double per = sc.nextDouble();
      list[i] = new Student(r, nme, per);
    }

    Student.sortStudent(list);
    System.out.println("\n---- Sorted Students ----");
    for (Student s : list)
      s.display();
    sc.close();
  }
}
