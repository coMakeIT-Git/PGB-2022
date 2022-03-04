package day3;

public interface Emp {
	void deptCode(String code);
	void deptPlace();
	void deptName();
}
		//abstract class.
abstract class Department implements Emp{
	public void deptName() {
		System.out.println("Name of the Department");
		}
	public void deptPlace() {
		System.out.println("Department");
		}
}
		//concrete class
class Main extends Department{
	public void deptCode(String code) {
		System.out.println("Department code is "+code);
	}
	@Override 
	public void deptPlace() {
		System.out.println("Place of the Department");
	}

	//main method
	public static void main(String[] args) {
	Main obj =new Main();
	obj.deptName();
	obj.deptPlace();
	obj.deptCode("12344ASD");
	}
}
		
