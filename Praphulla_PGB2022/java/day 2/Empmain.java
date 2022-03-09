import java.io.*;
class Employee
{
      
    public String empname;
    public int empid;
    public int empsalary;
    public int dob;
    Employee()
    {
    	System.out.println("welcome to the class Employee");
    }
          
    Employee(String empname, int empid) 
    {       
        this.empname = empname;
        this.empid = empid;
    }
    
    public String getName()
    {
    	return this.empname;
    	
    }
    public void setName(String empname)
    {
    this.empname = empname;
    	
    }
    
    public int getID()
    {
    	return this.empid;
    	
    }
    public void setID(int empid)
    {
    this.empid = empid;	
    }
  
    public boolean equals(Object obj)
    {
    if(this == obj)
            return true;
        if(obj == null || obj.getClass()!= this.getClass())
            return false;
        Employee emp=(Employee) obj;
        return (emp.empname == this.empname && emp.empid == this.empid);
    }
    public void displaydetails(String empname, int empid)
    {
    	System.out.println("the details of the employee are "+empname+ " "+empid+" ");
    }
    public void displaydetails(String empname, int empid,int empsalary)
    {
    	System.out.println("the details of the employee are "+empname+" " +empid+ " " +empsalary);
    }

    public int hashCode()
    {
    	return this.empid;
    }
      
}
class Empmain
{
      
    public static void main (String[] args)
    {
    	Employee e1=new Employee("Praph",1);
    	Employee e2=new Employee("Praph",1);
    	

        if(e1.hashCode() == e2.hashCode())
        {
  
            if(e1.equals(e2))
                System.out.println("Both Objects are equal");
            else
                System.out.println("Both Objects are not equal");
      
        }
        else
        System.out.println("Both Objects are not equal. "); 
        
        Employee e3=new Employee();
        
        e3.setName("Praphulla");
        e3.setID(53);
        e3.displaydetails(e3.empname,e3.empid);
        e3.displaydetails("praphulla",53,20000);
       Employee e4=new Employee();
        
        e4.setName("Raphy");
        e4.setID(55);
        e4.displaydetails(e3.empname,e3.empid);
        e4.displaydetails("Raphy",47,30000);
       
        
    } 
}
