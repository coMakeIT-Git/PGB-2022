package task1;
abstract class Employee // abstract class
{
	public void display1() {
	System.out.println("This is concrete method");
	}
	
	abstract public void display2(); //abstract method
}

class Manager extends Employee{
	public void display2()
	{
		System.out.println("It is overriding abstract method");
	}
	
	public void display1()
	{
		System.out.println("It is overriding concrete method");
	}
}
public class TestAbstract {
  public static void main(String[] args)
  {
	   Employee obj=new Manager();
	  obj.display2();
	  obj.display1();
  }
}
