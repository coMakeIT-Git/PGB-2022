package task1;
interface checkfun   //creating interface
{
	void empid();     //method1 in interface
	void empname();   //method2 in interface
}
abstract class empsalary    //creating abstract class
{
	abstract void salary();   //adding abstract method
}

	

public class Employee extends empsalary implements checkfun {
	public void empid()      //Implements methods of Interface class in concrete class
	{
		System.out.println("1000");
	}
	public void empname()     
	{
		System.out.println("ram");
	}
	public void salary()     //Override the methods of abstract Class in concrete class
	{
		System.out.println("10000");
	}
public static void main(String args[])
{
	checkfun obj=new Employee();   //create objects of concrete class
	obj.empid();
	obj.empname();
	empsalary obj1=new Employee();
	obj1.salary();
}
}
