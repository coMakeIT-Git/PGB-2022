package day3Assignment;

import java.util.*;

interface Person{
	public void eat();
	public void sleep();
}

abstract class Worker implements Person{
	abstract void work();
}

class Student extends Worker{
	private int studId;
	private String studName;
	public Student(int studId,String studName) {
		this.studId=studId;
		this.studName=studName;
	}
	public void work() {
		System.out.println("working");
	}
	
	public void eat() {
		System.out.println("eating");
	}
	public void sleep() {
		System.out.println("sleeping");
	}
	
	public static void main(String[] args) {
		Student obj=new Student(1,"nithish");
		obj.work();
		obj.eat();
		obj.sleep();
		
		List<Student> list=new LinkedList<Student>();
		list.add(new Student(2,"nithish"));
		list.add(new Student(3,"akhil"));
		list.add(new Student(4,"balaji"));
		
		Set<Student> set=new HashSet<Student>();
		set.add(new Student(5,"adhithya"));
		set.add(new Student(6,"ram"));
		
		Map<Student,String> map=new HashMap<Student,String>();
		map.put(new Student(7,"tarun"), "Hyderabad");
		map.put(new Student(8,"srinivas"), "Warangal");
		
		for(Student s1:list) {
			System.out.println(s1.studId+" "+s1.studName);
		}
		System.out.println();
		
		for(Student s2:set) {
			System.out.println(s2.studId+" "+s2.studName);
		}
		System.out.println();
		
		for(Map.Entry<Student,String> s3:map.entrySet()) {
			System.out.println(s3.getKey().studId+" "+s3.getKey().studName+" "+s3.getValue());
		}
		System.out.println();
		
		Collections.sort(list,new Comparator<Student>(){
			public int compare(Student a,Student b) {
				return b.studId-a.studId;
			}
		});
		
		System.out.println();
		System.out.println("printing list using stream after sorting");
		list.stream().forEach((s4)->System.out.println(s4.studId+" "+s4.studName));
		
	}	
}
