package task4;

interface CustomFunctionalInterface
{
	public void display();
}
public class FunctionalInterfaces {
 
	public static void main(String[] args)
	{
		CustomFunctionalInterface t1=new CustomFunctionalInterface() {
			public void display()
			{
				System.out.println("Displaying with anonymous class");
			}
		};
		
		t1.display();
		
		//with lambda expression
		CustomFunctionalInterface d1=()->{
			System.out.println("Display with the lambda expression");
		};
		d1.display();
	}
}
