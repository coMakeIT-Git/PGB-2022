package day2;

public class student {
	
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
        final int prime = 31;
        // Calculates HashCode using student id
        return (prime * this.id * this.name.hashCode());
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
    }

}
