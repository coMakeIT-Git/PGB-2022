package day3assignment;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

//adding a interface
interface person{
	void eat();
	void sleep();
}

//adding a abstract class
abstract class worker implements person{
	abstract void work();
}

class employee extends worker{
	private int empId;
	private String name;
	public employee(int empId, String name) {
		this.empId = empId;
		this.name = name;
	}
	
	//implementing the interface methods
	public void eat() {
		System.out.println("Employee is eating!!!");
	}
	public void sleep() {
		System.out.println("Employee is sleeping.");
	}
	void work() {
		System.out.println("Employee is working.");
	}
	public static void main(String[] args) {
		employee obj = new employee(100, "Ram");//creating the object of the employee class
		obj.eat();
		obj.sleep();
		obj.work();
		
		List<employee> li = new ArrayList<>();//creating a list
		li.add(obj);
		li.add(new employee(123,"Harish"));
		li.add(new employee(456,"Krishna"));
		li.add(new employee(789,"Shyam"));
		
		Set<employee> s = new HashSet<>();//creating a set
		s.add(new employee(123,"Harish"));
		s.add(new employee(456,"Krishna"));
		s.add(new employee(789,"Shyam"));
		
		Map<employee, String> hm = new HashMap<>();//creating a map
		hm.put(new employee(123,"Harish"),"Mumbai");
		hm.put(new employee(456,"Krishna"),"Bangalore");
		hm.put(new employee(789,"Shyam"),"Ahmedabad");
		
		System.out.println("Elements of list:");//iterating and printing the elements of the list
		for(employee emp:li) {
			System.out.println(emp.empId+" "+emp.name);
		}
		
		System.out.println("Elements of Set:");//iterating and printing the elements of the set
		for(employee emp:s) {
			System.out.println(emp.empId+" "+emp.name);
		}
		
		System.out.println("Elements of Map:");//iterating and printing the elements of the map
		for(Map.Entry<employee,String>f:hm.entrySet()) {
			System.out.println(f.getKey().empId+" "+f.getKey().name+" "+f.getValue());
		}
		
		//sorting the collections of the list
		Collections.sort(li, new Comparator<employee>() {
			public int compare(employee a, employee b) {
				return b.empId - a.empId;
			}
		});
		
		//Printing the elements of the list using stream
		System.out.println("Printing the elements of the list using Stream");
		li.stream().forEach((c)->System.out.println(c.empId+" "+c.name));
	}
}
