import MyMath.ArithOp;

public class TestArithOp {
  public static void main(String[] args) {
    ArithOp op = new ArithOp();
    System.out.println("Add (15 + 5) = " + op.add(15, 5));
    System.out.println("Sub (15 - 5) = " + op.sub(15, 5));
    System.out.println("Mul (15 * 5) = " + op.mul(15, 5));
    System.out.println("Div (15 / 5) = " + op.div(15, 5));
  }
}
