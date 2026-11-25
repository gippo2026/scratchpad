import AdvMath.NumericOp;

public class TestNumericOp {
  public static void main(String[] args) {
    NumericOp op = new NumericOp();
    System.out.println("Max(25, 49) = " + op.max(25, 49));
    System.out.println("Min(25, 40) = " + op.min(25, 40));
  }
}
