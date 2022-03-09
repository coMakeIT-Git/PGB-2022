package task3;

public class sampletest {
	public static void main(String args[])
    {
        functional_interface fobj = (int x)->System.out.println(x);
        System.out.println("Custom Functional Interface");
        fobj.abstract_function(100);
    }

}
