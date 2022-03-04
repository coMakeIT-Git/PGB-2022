package day3;

import java.util.*;

//Interface Class
interface Person {
	// Declare 2 methods in interface
	String gender(String name);
	int age(int age);
}

//Abstract class
abstract class Human {
	
	// Add method with definition in abstract class
	public String name(String name){
		System.out.println("This won't be printed");
 		return name;
	}
	public int Height(int h) {
 	// System.out.println("Color is Red");
		return h;
	}
}


//Concrete class
class student extends Human implements Person{
	
    int id;
    private int number; // Private attribute for getter and setter
    String name;

    student(){
    	// Default Constructor, Does Nothing
    }
    
    student(int id, String name){
    	// Parameterized Constructor, Adds ID
        this.id = id;
        this.name = name;
    }

    // Getter Method
    public int getNumber(){
        // System.out.println("Student ID : "+this.id+"\nStudent Number : "+this.number);
        return this.number;
    }

    // Setter Method
    public void setNumber(int n){
        this.number = n;
    }

    // Equals Override
    @Override
    public boolean equals(Object o){
        
        if (o == this){
            // a.equals(a)
            return true;
        }

        if (o == null) {
            // NULL value check
            return false;
        }

        if (o.getClass() != this.getClass()){
            // Returns False if  different Types
            return false;
        }

        student stu = (student) o;
        // Check if Attributes are Same or not
        return (stu.name == this.name && stu.id == this.id && stu.getNumber() == this.number);

    }

    // HashCode Override
    @Override
    public int hashCode() {
        // Calculates HashCode using student ID
        return (this.id * this.name.hashCode());
    }

    // Method Overloading - Takes only one parameter
    void record(int id){
        System.out.println("Student ID (overloading 1) : "+id);
    }

    // Method Overloading - Takes two parameters
    void record(int id,int number){
        System.out.println("Student ID (overloading 2) : "+id);
        System.out.println("Student Nummber (overloading 2) : "+number);
    }

    // Implements methods of Interface class in concrete class
	public int age(int age) {
		return age;
	}
	
	// Implements methods of Interface class in concrete class
	public String gender(String g){
     // System.out.println("Car Name : "+name);
		return g;
	}
 
	// Override the methods of abstract Class in concrete class
	@Override
	public int Height(int h) {
		System.out.println("Height : "+h);
		return h;
	}

	// Override the methods of abstract Class in concrete class
	@Override
	public String name(String nme) {
		return nme;
	}
	
	// Concrete class method
	public String section(String s) {
		return s;
	}

    
    public static void main(String[] args){
    	// Initialize obj
        student s1 = new student(1,"Student1");
        
        // Using Setter Method
        s1.setNumber(123);
        
        // Using Getter Method
        System.out.println("Student Number using getNumber() : "+s1.getNumber());
        
        // Initialize another object with same Attributes
        student s2 = new student(1,"Student1");
        s2.setNumber(123);
        
        // Equals Check
        System.out.println("Student Equals (Override): "+s1.equals(s2));
        
        // Initialize another object with different Attributes
        student s3 = new student(1,"Student2");
        s3.setNumber(123);
        
        // Equals Check
        System.out.println("Student Equals (Override): "+s1.equals(s3));
        
        // Hash Code Check
        System.out.println("Hash Code of s1 : "+s1.hashCode()+"\nHash code of s2 : "+s2.hashCode());
        
        // Method Overloading
        s1.record(3);
        s1.record(4,145);
        
     	// Create objects of concrete class
        student cc = new student();
        System.out.println("Section : " + cc.section("A"));
        
        // Access the Abstract class methods
        System.out.println("Height : " + cc.Height(160));

        // Access the Concrete class methods
        System.out.println("Name by accessing concrete class method : " + cc.name("Noname"));
        
        student s4 = new student(1001, "Student1");
        student s5 = new student(1002, "Student2");
        student s6 = new student(1003, "Student3");
        student s7 = new student(1004, "Student4");
        student s8 = new student(1005, "Student5");
        
        
        // Initialize a Collections List
        List<student> studentlist=new ArrayList<>();
        studentlist.add(s4);
        studentlist.add(s5);
        studentlist.add(s6);
        studentlist.add(s7);
		
        // Initialize a Collections HashSet
		Set<student> studentset=new HashSet<>();
		studentset.add(s6);
		studentset.add(s7);
		studentset.add(s8);
		
		// Initialize a Collections Map
		Map<String, student> studentmap = new HashMap<String, student>();
		studentmap.put("A", s1);
		studentmap.put("B", s2);
		studentmap.put("B", s3);
		studentmap.put("C", s4);
		studentmap.put("B", s5);
		studentmap.put("A", s6);
		studentmap.put("C", s7);
		studentmap.put("C", s8);
		
		
        // Iterate and Print List
    	System.out.println("Printing Student's ID List :");
        for (student name : studentlist) {
            System.out.println(name.id);
        }
        
        // Iterate and Print HashSet
    	System.out.println("Printing Student's ID Set :");
        for (student s : studentset) {
            System.out.println(s.id);
        }
        
        // Iterate and Print Map
        System.out.println("Printing Student's ID and Names Using Map :");
        for (Map.Entry <String, student>m : studentmap.entrySet()) {
        	System.out.println(m.getKey() + " " + m.getValue().name);
        }
        
        // Sort the Collections of list
        Collections.sort(studentlist, new Comparator<student>(){
        	@Override
        	public int compare(student a, student b) {
        		return b.id-a.id;
        	}
        }
       );
        
        // Java Stream to iterate the list
        System.out.println("Printing List using Java Stream");
        studentlist.stream().forEach((a)->System.out.println("Name : "+a.name+", ID : "+a.id));
        
    }

}



