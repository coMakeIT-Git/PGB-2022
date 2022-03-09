package day2Assignment.test;

public class Employee {
	private int empId;
	private String empName;
	private String email;

	public Employee(){
	
	}
	public Employee(int empId, String empName, String email) {
		this.empId = empId;
		this.empName = empName;
		this.email = email;
	}
	
	public int getEmpId() {
		return empId;
	}
	public void setEmpId(int empId) {
		this.empId = empId;
	}
	public String getEmpName() {
		return empName;
	}
	public void setEmpName(String empName) {
		this.empName = empName;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	
	@Override
	public boolean equals(Object x) {
		if(x==null || x.getClass() != this.getClass())
			return false;
		
		final Employee y = (Employee)x;
		if(y.getEmpId()!=this.getEmpId() || y.getEmpName()!=this.getEmpName() || y.getEmail()!=this.getEmail()) {
			return false;
		}
		return true;
		
	}
	
	@Override
	public int hashCode() {
		return this.empId;
	}
	
	public void display(int id,String name) {
		System.out.println(id+" "+name);
	}
	
	public void display(int id,String name,String email) {
		System.out.println(id+" "+name+" "+email);
	}
}
