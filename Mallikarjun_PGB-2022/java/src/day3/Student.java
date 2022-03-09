package day3;

import java.util.*;

interface Person {
	String gender(String name);
	int age(int age);
}
abstract class Human {
	public String name(String name) {
		System.out.println("This won,t be printed");
		return name;
	}
	public int Height(int h) {
		return h;
	}
}
class Student extends Human implements Person {
	int id;
	private int number;
	String name;
	
	Student(){
		
	}
	Student(int id, String name){
		this.id = id;
		this.name = name;
	}
	public int getNumber() {
		return this.number;
	}
	public void setNumber(int n) {
		this.number = n;
	}
	
	public boolean equals(Object o) {
		if (o == this) {
			return true;
		}
		if (o == null) {
			return false;
		}
		if(o.getClass() !=this.getClass()) {
			return false;
		}
		Student stu = (Student) o;
		return(stu.name == this.name && stu.id == this.id && stu.getNumber()== this.number);
	}
	
	public int hashCode() {
		return(this.id * this.name.hashCode());
	}
	
	void record(int id) {
		System.out.println("Student ID (overloading 1) : " +id);
	}
	void record(int id, int number) {
		System.out.println("Student ID (overloading 2) : " +id);
		System.out.println("Student Number (overloading 2) : " +number);
	}
	
	public int age(int age) {
		return age;
	}
	
	public String gender(String g) {
		return g;
	}
	public int Height(int h) {
		System.out.println("Height : "+h);
		return h;
	}
	public String name(String nme) {
		return nme;
	}
	public String section(String s) {
		return s;
	}
	
	public static void main(String[] args) {
		Student s1 = new Student(1,"Student1");
		s1.setNumber(123);
		System.out.println("Student Number Using getNumber() : "+s1.getNumber());
		
		Student s2 = new Student(1,"Student1");
		s2.setNumber(123);
		System.out.println("Student equals (Override) : "+s1.equals(s2));
		
		Student s3 = new Student(1,"Student2");
		s3.setNumber(123);
		System.out.println("Student equals (Override) : "+s1.equals(s3));
		
		System.out.println("HashCode of s1 : "+s1.hashCode()+"\nHashCode of s2 : "+s2.hashCode());
		
		s1.record(3);
		s1.record(4,145);
		
		Student cc = new Student();
		System.out.println("Section : " + cc.section("A"));
		System.out.println("Height : " + cc.Height(120));
		System.out.println("Name by accessing concrete class method : " + cc.name("noname"));
		
		Student s4 = new Student (100, "Student1");
		Student s5 = new Student (101, "Student2");
		Student s6 = new Student (102, "Student3");
		Student s7 = new Student (103, "Student4");
		Student s8 = new Student (104, "Student5");
		
		List<Student> Studentlist=new ArrayList<>();
		Studentlist.add(s4);
		Studentlist.add(s5);
		Studentlist.add(s6);
		Studentlist.add(s7);
		
		Set<Student> Studentset=new HashSet<>();
		Studentset.add(s7);
		Studentset.add(s8);
		Studentset.add(s8);
		
		Map<String, Student> Studentmap = new HashMap<String, Student>();
		
		Studentmap.put("A", s1);
		Studentmap.put("B", s2);
		Studentmap.put("C", s3);
		System.out.println("Print students id list : ");
		
		for (Student name : Studentlist)
			System.out.println(name.id);
		System.out.println("Print students id set: ");
		for (Student s : Studentset)
			System.out.println(s.id);
		System.out.println("Print students id using map: ");
		for(Map.Entry<String, Student>m :Studentmap.entrySet()) {
			System.out.println(m.getKey() +" "+ m.getValue().name);
			
		Collections.sort(Studentlist,new Comparator<Student>() {
			public int compare(Student a,Student b) {
				return a.id-b.id;
			}
		
		}
		);
	
		System.out.println("Printing list using java stream");
		Studentlist.stream().forEach((a)->System.out.println("Name : "+a.name+", id : "+a.id));
	}

	}
}

