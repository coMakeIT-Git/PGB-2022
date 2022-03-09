package Task1;

public class Overloading {

	public static int add(int a,int b)
	{
		return a+b;
	}
	
	public static int add(int a, int b, int c)
	{
		return a+b+c;
	}
	
	public static void main(String[] args)
	{
		System.out.println(Overloading.add(11,12));
		System.out.println(Overloading.add(11,12,13));
	}
}
