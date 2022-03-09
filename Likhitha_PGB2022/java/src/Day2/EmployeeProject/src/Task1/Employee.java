package Task1;


//public class Main {
//  
//
//  public static void main(String[] args) {
//    Level myVar = Level.MEDIUM; 
//    System.out.println(myVar);
//  }
//}

public class Employee {
 int empid,salary; //Attributes added
 String name, address;
 
 public Employee() { //default constructor
	 empid= 100;
 }
 
 
 public enum Gender{
	 MALE, FEMALE
 }
 
 public Gender gender;
 
 public Employee(String name, int empid, String address, int sal,Gender g) //Parameter constructor
 {
	 this.name=name;
	 this.empid=empid;
	 this.address=address;
	 this.salary=sal;
	 this.gender=g;
 }
 
 @Override
 public boolean equals(Object ob)
 {
	 if(ob==this)
		 return true;
	 
	 if(ob==null || ob.getClass()!=getClass())
		 return false;
	 
	 Employee p = (Employee) ob;
	 
	 return p.name.equals(name) && p.empid==empid && p.address.equals(address) && p.salary==salary;
 }
 
 @Override
 public int hashCode()
 {
	 int re=5;
	 re=5*re + (name==null ? 0: name.hashCode());
	 re=5*re+salary;
	 
	 return re;
 }
 
 public int getSal()
 {
	 return salary;
 }
 
 public int getEmpid()
 {
	 return empid;
 }
 
 public Gender getGender()
 {
	 return gender;
 }
 public void setEmpid(int id)
 {
	 this.empid=id;
 }
 
 public void setSalary(int sal) {
	 this.salary=sal;
 }
 
 public void setName(String name)
 {
	 this.name=name;
 }
 
 public void setAddress(String add)
 {
	 this.address=add;
 }
 
 public void setGender(Gender g)
 {
	 this.gender=g;
 }
 
 
 public static void main(String[] args)
 {
	 Employee emp= new Employee(); //object created
	 emp.setEmpid(101); //setters
	 emp.setName("Rama");
	 emp.setSalary(20000);
	 emp.setAddress("Delhi");
	 emp.setGender(Gender.MALE);
	 
	 Employee emp1= new Employee("John", 1 , "Mumbai", 15000,Gender.MALE);
	 Employee emp2= new Employee("John", 1, "Mumbai", 15000,Gender.MALE);
	 Employee emp3= new Employee("Rama", 2, "Delhi", 25000,Gender.FEMALE);
	 
	 int getsal = emp.getSal(); //Getters
	 int getempid = emp.getEmpid();
	 
	 System.out.println(emp.empid);
	 System.out.println(emp.name);
	 System.out.println(emp.salary);
	 System.out.println(emp.address);
	 System.out.println(emp.gender);
	 
	 System.out.println(getsal);
	 System.out.println(getempid);
	 
	 System.out.println(emp1.equals(emp2));
	 System.out.println(emp2.equals(emp3));
	 
	
	 
	 
 }
}
