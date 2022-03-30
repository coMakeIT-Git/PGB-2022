package Task2;

interface A{
	public  int sq(int c);
}

interface E{
	public  int sum(int c,int d);
}

class B{
	public static int power(int c) {
		return c*c;
	}}

class Addition {
	public int Add(int f,int g) {
		return f+g;
	}
}
interface C {
	public Employee getEmployee();
}

interface D {
	public Employee getEmployee(String name, int age);
}

class Employee {
	String eName;
	int eAge;
	
	public Employee(){} 
	
	public Employee(String eName, int eAge) {
		this.eName = eName;
		this.eAge = eAge;
	}
	
	public void getInfo() {
		System.out.println("I am a method of class Employee");
	}
}

public class Referenceexample {
	public static void main(String args[]) {
	A a=B :: power;
	System.out.println("Using Static method reference  to print Square of a number:");
	System.out.println(a.sq(5));
	
	Addition obj=new Addition();
	E e=obj::Add;
	System.out.println("Printing sum using instance reference:");
	System.out.println(e.sum(6, 7));
	
	
	System.out.println("Method referencing using Constructor:");
	C c2 = Employee::new;
	c2.getEmployee().getInfo();
	D d2 = Employee::new;
	d2.getEmployee("Tony", 34).getInfo();
	
	}

}