package comakeit;

import java.util.Objects;

public class Student {
	
	//Attributes to class
	int id;
	String name;
	int age;
	
	//Default constructor
	public Student() {
	}
	
	//parameterized constructor
	public Student(int id, String name, int age) {
		this.id = id;
		this.name = name;
		this.age = age;
	}

	//Adding getters and setters
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	//Override equals and hashCode method
	@Override
	public int hashCode() {
		return Objects.hash(age, id, name);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Student other = (Student) obj;
		return age == other.age && id == other.id && name==other.name;
	}
	
	//method overloading
	void Sum(int id) {
		System.out.println("Student Id(overloading):"+ id);
	}
	
	void Sum(int id,int age) {
		System.out.println("Student Id(overloading):"+ id);
		System.out.println("*********");
		System.out.println("Student Age(overloading):"+ age);
	}
	
	public static void main(String[] args) {
		Student s1=new Student(1,"sai",22);
		Student s2=new Student(1,"sai",24);
		System.out.println("for constructor=> "+"Id: "+s1.id+" Name: "+ s1.name +" Age: "+s1.age);
		System.out.println("*********");
		s1.setId(100);
		s1.setName("akash");
		s1.setAge(22);
		System.out.println("getID: "+s1.getId());
		System.out.println("*********");
		System.out.println("getName: "+s1.getName());
		System.out.println("*********");
		System.out.println("getAge: "+s1.getAge());
		System.out.println("*********");
		s1.Sum(2);
		System.out.println("*********");
		s1.Sum(3,24);
		System.out.println("*********");
		System.out.println("obj of students are equal: "+s1.equals(s2));
		System.out.println("*********");
		System.out.println("hash code of s1: "+s1.hashCode()+", hash code of s2: "+s2.hashCode());
		
	}
	
	
	
	

}
