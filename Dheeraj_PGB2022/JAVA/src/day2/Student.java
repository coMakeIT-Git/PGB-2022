package day2;

public class Student {
	
	// Private Attributes
    private long number;
    private String email = null;
    
    // Public Attributes
    public int id;
    public String name = null;
    public String gender = null;
    public int age;
	
    
    public Student() {
	}
    
	// Parameterized Constructor
	public Student(int id, String name){
        this.id = id;
        this.name = name;
    }


	// Getter Methods
    public long getNumber(){
        return this.number;
    }
    
    public String getEmail() {
		return email;
	}
    
    // Setter Methods
    public void setNumber(long n){
        this.number = n;
    }
    
    public void setAge(int age){
        this.age = age;
    }

	public void setEmail(String email) {
		this.email = email;
	}
	
    public void setGender(String gender) {
		this.gender = gender;
	}


    // Equals Override
    @Override
    public boolean equals(Object o){
        
    	// a.equals(a)
        if (o == this){
            return true;
        }

        // NULL value and Types check
        if (o == null || o.getClass() != this.getClass()) {
            return false;
        }

        // Check if Attributes are Same or not
        Student stu = (Student) o;
        return (stu.hashCode() == this.hashCode());

    }

    // HashCode Override
    @Override
    public int hashCode() {
        final int prime = 31;
        return ((this.id * this.name.hashCode()) % prime);
    }

    // Method Overloading - Takes three parameter
    void add_data(long number, String email, String gender){
        this.number = number;
        this.email = email;
        this.gender = gender;
    }

    // Method Overloading - Takes two parameters
    void add_data(long number, String email){
		this.number = number;
        this.email = email;
    }

    public static void main(String[] args){
    	// Initialize obj
        Student s1 = new Student(1,"Student1");
        
        // Using Setter Method
        s1.setNumber(9327598235L);
        
        // Using Getter Method
        System.out.println("Student Number using getNumber() : "+s1.getNumber());
        
        // Initialize another object with same Attributes
        Student s2 = new Student(1,"Student1");
        s2.setNumber(9327598235L);
        
        // Equals Check
        System.out.println("Student Equals (Override): "+s1.equals(s2));
        
        // Initialize another object with different Attributes
        Student s3 = new Student(1,"Student2");
        s3.setNumber(123);
        
        // Equals Check
        System.out.println("Student Equals (Override): "+s1.equals(s3));
        
        // Hash Code Check
        System.out.println("Hash Code of s1 : "+s1.hashCode()+"\nHash code of s2 : "+s2.hashCode());
        
        // Method Overloading
        s1.add_data(9234234234L,"Student1@email.com","Male");
        s1.add_data(9234234234L,"Student2@email.com");
    }

}
