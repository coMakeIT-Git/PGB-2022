package task3;

public class function {
	public static void main(String args[])
    {
        functionalinterface fobj = (int x)->System.out.println(x);
        System.out.println("Custom Functional Interface");
        fobj.abstractfunction(100);
    }
}
