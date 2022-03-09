package day2;
import java.util.*;
public class Employee {
	int id;
	private int empcode;
    public String name;
    public Employee() {
		//Default Constructor;
	}
    public Employee(int id,String name) {
    	//Parmeterized constructor
		this.id=id;
		this.name=name;
	}
    //Getter method
    public int getEmpcode() {
    	return this.empcode;
    }
    //Setter method
    public void setEmpcode(int n) {
    	this.empcode=n;
    }
    //Equals Override
	@Override
	public boolean equals(Object obj) {
		// TODO Auto-generated method stub
		if(obj==this)
			return true;
		if(obj==null)
			return false;
		if(obj.getClass()!=this.getClass())
			return false;
		Employee emp=(Employee) obj;
		return (emp.name==this.name && emp.id==this.empcode);
	}
	@Override
	public int hashCode() {
		// TODO Auto-generated method stub
		 final int prime = 31;
	        // Calculates HashCode using student id
	        return ( this.id * this.name.hashCode());
		
	}
	
	private void id(int hashCode) {
		// TODO Auto-generated method stub
		
	}
	void record(int id){
        System.out.println("Employee ID (overloading 1):"+id);
	}
	 void record(int id,String name){
	        System.out.println("Employee ID (overloading 2) : "+id);
	        System.out.println("Employee Name (overloading 2) : "+name);
	    }
	 
	 
	 public static void main(String[] args){
	    	// Initialize obj
	        Employee e1 = new Employee(1,"Employee1");
	        
	        // Using Setter Method
	        e1.setNumber(100);
	        
	        // Using Getter Method
	        System.out.println("Employee code using getEmpcode() : "+e1.getEmpcode());
	        
	        // Initialize another object with same Attributes
	        Employee e2 = new Employee(1,"Employee1");
	        e2.setNumber(101);
	        
	        // Equals Check
	        System.out.println("Employee Equals (Override): "+e1.equals(e2));
	        
	        // Initialize another object with different Attributes
	        Employee e3 = new Employee(1,"Employee2");
	        e3.setNumber(100);
	        
	        // Equals Check
	        System.out.println("Employee Equals (Override): "+e1.equals(e3));
	        
	        // Hash Code Check
	        System.out.println("Hash Code of e1 : "+e1.hashCode()+"\nHash code of e2 : "+e2.hashCode());
	        
	        // Method Overloading
	        e1.record(3);
	        e1.record(4,"Tom");
	    }
	private void setNumber(int i) {
		// TODO Auto-generated method stub
		
	}

	}