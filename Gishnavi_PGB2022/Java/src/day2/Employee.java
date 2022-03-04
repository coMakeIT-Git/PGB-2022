package day2;

import java.util.*;
public class Employee {
	
    int emp_id;
    private int num; 
    String name;

    public Employee(){
    	// Default Constructor
    	System.out.println("object created");
    } 
    Employee(int emp_id, String name){
    	// Parameterized Constructor
        this.emp_id = emp_id;
        this.name = name;
    }
    // Equals Override
    @Override
    public boolean equals(Object o){ 
        if (o == this){
            return true;
        }
        if (o == null || o.getClass() != this.getClass()) {
            return false;
        }
        Employee emp = (Employee) o;
        return (emp.name == this.name && emp.emp_id == this.emp_id && emp.getNumber() == this.num);
    }
 // Getter Method
    public int getNumber(){
        return this.num;
    }
    // Setter Method
    public void setNumber(int n){
        this.num = n;
    }
  // HashCode Override
    @Override
    public int hashCode() {
        final int prime = 31;
    return (prime * this.emp_id * this.name.hashCode());
    }
    // Method Overloading 
    void record(int emp_id){
        System.out.println("Employee ID is "+emp_id);
    }
    void record(int emp_id,int num){
        System.out.println("Employee ID is "+emp_id);
        System.out.println("Employee Nummber is "+num);
    }

    public static void main(String[] args){
        Employee e1 = new Employee(64,"Employee1");
        e1.setNumber(879);
        System.out.println("Employee Number (getter): "+e1.getNumber());
        Employee e2 = new Employee(64,"Employee1");
        e2.setNumber(879); 
        System.out.println("Equals Override: "+e1.equals(e2));        
        Employee e3 = new Employee(64,"Employee2");
        e3.setNumber(879);
        System.out.println("Equals Override: "+e1.equals(e3));
        System.out.println("Hash Code override e1 : "+e1.hashCode()+"\nHash code override e2 : "+e2.hashCode());
        e1.record(879);
        e1.record(880,65);
    }

}
