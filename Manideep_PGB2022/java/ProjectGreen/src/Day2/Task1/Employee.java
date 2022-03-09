package Day2.Task1;

public class Employee {
	String Company="CoMakeIt";
	String Batch,name;
	int emp_id;
	public String getname()
	{
		return this.name;
	}
	public void setname(int id,String Name)
	{
		this.emp_id=id;
		this.name=Name;
	}
	Employee()
	{
		this.Batch="PGB-2022";
	}
	Employee(String Batch)
	{
		this.Batch=Batch;
	}
	@Override
    public boolean equals(Object obj)
    {
    if(this == obj)
            return true;
        if(obj == null || obj.getClass()!= this.getClass())
            return false;
        Employee emp = (Employee) obj;
        return (emp.name == this.name && emp.Batch == this.Batch && emp.emp_id==this.emp_id);
    }
	@Override
    public int hashCode()
    {
        return this.emp_id;
    }
	public static Boolean check(Employee e1,Employee e2)
	{
		if(e1.hashCode() == e2.hashCode())
        {
  
            if(e1.equals(e2))
                return true;
            else
                return false;
      
        }
        return false;
	}
	public void print(Employee e)
	{
		System.out.println(e.getname());
	}
	public void print()
	{
		System.out.println("This is Not a Parameterised Method");
	}
	public static void main(String args[])
	{
		Employee e1=new Employee();
		Employee e2=new Employee();
		e1.setname(1,"Manideep");
		e2.setname(1,"Mani");
		if(check(e1,e2))
			System.out.println("Objects are Same");
		else
			System.out.println("Objects are Different");
		e1.print();
		e1.print(e2);
		
	}

}
