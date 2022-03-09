package Task1;

public class Employee {
	public int empid,empsalary;
	public String empname;
	//default constructor
	Employee()
	{
		
	}
	//parameterized constructors
Employee(int id,int salary,String name)
{
	empid = id;
	empsalary = salary;
	empname = name;
}	


//getter and setter
	
public int getEmpid() {
		return empid;
	}

	public void setEmpid(int empid) {
		this.empid = empid;
	}

	public int getEmpsalary() {
		return empsalary;
	}

	public void setEmpsalary(int empsalary) {
		this.empsalary = empsalary;
	}

	public String getEmpname() {
		return empname;
	}

	public void setEmpname(String empname) {
		this.empname = empname;
	}
//hashcode method
@Override
public int hashCode()
{		
	return empid+empname.hashCode();
}
//equals method
@Override
public boolean equals(Object o)
{
	Employee s = (Employee)o;
	if(this.empid == s.empid && this.empname == s.empname)
		return true;
	else
		return false;
}
//Method Overloading
void display(int empid)
{
	System.out.println("Employee id :"+empid);
}
void display(int empid,String empname)
{
	System.out.println("Employee id :"+empid);
	System.out.println("Employee id :"+empname);
}

public static void main(String args[])
{
	System.out.println("Day2 Assignment");
	Employee s1 = new Employee(121,1000,"sai");
	Employee s2 = new Employee(122,1000,"ram");
	Employee s3 = new Employee(121,1000,"sai");
	//equality check
	System.out.println(s1.equals(s2));
	System.out.println(s1.equals(s3));
	//hashcode
	System.out.println("Hash code of s1:"+s1.hashCode());
	System.out.println("Hash code of s2:"+s2.hashCode());
	//call for method overloading
	s1.display(101);
	s1.display(101,"rahul");
}

}
