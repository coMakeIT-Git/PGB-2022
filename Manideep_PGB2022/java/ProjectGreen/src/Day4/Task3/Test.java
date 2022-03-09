package Day4.Task3;
 import Day4.Task3.FuncInterface;
public class Test {
	    public static void main(String args[])
	    {
	        FuncInterface fobj = (int x)->System.out.println(x);
	        System.out.println("Custom Functional Interface");
	        fobj.abstractFun(5);
	    }
}
