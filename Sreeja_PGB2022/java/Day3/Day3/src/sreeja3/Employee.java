package sreeja3;

public class Employee extends Details implements Data {
	public void id() {
		System.out.println("1001");
		
	}

	public void name() {
System.out.println("Sreeja");		
	}
	public void age() {
		System.out.println("30");
	}
	public static void main(String args[]) {
	
	Employee e=new Employee();
	e.id();
	e.name();
	e.age();
	}
}
