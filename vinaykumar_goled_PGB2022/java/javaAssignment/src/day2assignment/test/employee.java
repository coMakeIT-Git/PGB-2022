package day2assignment.test;

public class employee {
	String name;
	int age;
	int id;
	employee(){
		System.out.println("This is a default constructor");
	}
	employee(String name, int age, int id){
		this.name = name;
		this.age = age;
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public int getAge() {
		return age;
	}
	public int getId() {
		return id;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public void setId(int id) {
		this.id = id;
	}
	//overriding equals method
	public boolean equals(Object obj) {
		if(obj == this) {
			return true;
		}
		if(obj == null || obj.getClass() != this.getClass()) {
			return false;
		}
		employee eobj = (employee)obj;
		return (eobj.name.equals(name) && eobj.age==age);
	}
	//overriding hashCode method
	public int hashCode() {
		return this.id;
	}
	public void printSalary(int salary) {
		System.out.println("Salary: " +salary);
	}
	public void printSalary(int salary, int bonus) {
		System.out.println("Salary with bonus: " +(salary+bonus));
	}
}
class Main{
	public static void main(String[] args) {
		employee e1 = new employee("Ram", 25, 5432);
		employee e2 = new employee("Krishna", 30, 1234);
		employee e3 = new employee("Ram", 25, 5432);
		System.out.println(e1.equals(e2));
		System.out.println(e2.equals(e3));
		System.out.println(e1.equals(e3));
		employee e4 = new employee();
		e4.printSalary(38000);
		e4.printSalary(38000, 10000);
	}
}

