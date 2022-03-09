package day3Assignment;

import java.util.*;
interface Person {
	public void eat();
	public void sleep();
}

abstract class Worker implements Person{
	abstract void work();//abstract method
	
}
class Employee extends Worker{

	private int empId;
	private String empName;
	
	public Employee(int empId, String empName) {
		this.empId = empId;
		this.empName = empName;
	}
	
	//implementing abstract method in interface
	public void eat() {
		System.out.println("Eating");
	}
	//implementing abstract method in interface
	public void sleep() {
		System.out.println("Sleeping");
	}
	@Override //overriding abstract method in abstract class
	void work() {
		System.out.println("working");
	}
	 
	public static void main(String[] args) {
		Employee e = new Employee(1,"anvesh");
		System.out.println("Calling overriding methods:");
		e.eat();
		e.sleep();
		e.work();
		
		List<Employee> lst = new ArrayList<>();
		lst.add(e);
		lst.add(new Employee(2,"Shyam"));
		lst.add(new Employee(3,"Ram"));
		lst.add(new Employee(4,"Nithish"));
		
		Set<Employee> set = new HashSet<>();
		set.add(new Employee(2,"Shyam"));
		set.add(new Employee(3,"Ram"));
		set.add(new Employee(4,"Nithish"));
		
		Map<Employee,String> hm = new HashMap<>();
		hm.put(new Employee(2,"Shyam"),"Hyderabad");
		hm.put(new Employee(3,"Ram"),"Hyderabad");
		hm.put(new Employee(4,"Nithish"),"Chennai");
		System.out.println();
		System.out.println("list elements: ");
		for(Employee emp:lst) {
			System.out.println(emp.empId+" "+emp.empName);
		}
		System.out.println();
		System.out.println("Set elements: ");
		for(Employee emp:set) {
			System.out.println(emp.empId+" "+emp.empName);
		}
		System.out.println();
		System.out.println("Map elements: ");
		for(Map.Entry<Employee, String>f:hm.entrySet()) {
			System.out.println(f.getKey().empId+" "+f.getKey().empName+" "+f.getValue());
		}
		
		Collections.sort(lst,new Comparator<Employee>() {
			public int compare(Employee a,Employee b) {
				return b.empId-a.empId;
			}
		});
		
		System.out.println();
		System.out.println("Printing list using Stream after sorting");
		lst.stream().forEach((c)->System.out.println(c.empId+" "+c.empName));
	}
	
}



