import java.io.*;
import java.util.concurrent.ExecutorService;  
import java.util.concurrent.Executors; 
import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.*;
import java.util.function.Supplier;
import java.util.function.Predicate;
import java.util.function.Consumer; 
interface Resources
{  
void download();    
} 
interface Resources1
{
	Employee getEmployee(String msg);	
}
class Employee implements Runnable
{  
    public String empname;
    public int empid;
    public int empsalary;
    public int dob;
    Employee(String msg)
    {
    	System.out.println("welcome to the class Employee!Your assigned id is: "+msg);
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
    public synchronized void displaydetails(String empname, int empid)
    {
		System.out.println("The details of the employee are:"+empname+ " "+empid+" "+Thread.currentThread().getId()+" ");
	    try
	    {
	      Thread.sleep(400);
	    }
	    catch (Exception e)
	    {
	        System.out.println(e);
	    }
    }
	    public void run()
	    { 
	    	this.displaydetails(this.empname, this.empid);
	    	
	    } 
		    public static void EmployeeThreadStatus()
	    {  
	        System.out.println("Thread is running: Reference to a static method");  
	    }  
	    public static void downloadResources()
	    {
	    	System.out.println("Reference to a Static method: Msg: Resources Downloaded.");
	   	}
	    static void uploadFiles(String name)
	    {  
	    	System.out.println("Reference to a Static method: Msg: Uploading file:"+name);  
		}  
	    public void retrieve()
	    {
	    	 System.out.println("Reference to a Instance method: Msg: Retrieving files!(Testing instance method ref");  
	    }
}
class ThreadPool
{  
    public static void main (String[] args)
    {
		Thread t2=new Thread(Employee::EmployeeThreadStatus);  
        t2.start(); 
    	ExecutorService pool=Executors.newFixedThreadPool(2);
    	Runnable r1= new Employee("praphulla",1);
    	pool.execute(r1);
    	Runnable r2= new Employee("chaitra",2);
    	pool.execute(r2);
    	Runnable r3= new Employee("shyam",3);
    	pool.execute(r3);
    	Runnable r4= new Employee("vinay",4);
    	pool.execute(r4);
    	pool.shutdown();
    	
    	while(!pool.isTerminated())
    	{
		}
		System.out.println("Submitted all the tasks!");
		Resources1 re = Employee::new;  
        re.getEmployee("CMIT-1072");  
		
		Employee e1=new Employee("1");
		Resources rs = e1::retrieve;
	
	    // Creating consumer
	    Consumer<String> consumer = Employee::uploadFiles;  
	    consumer.accept("Praphulla.java");  
	    // Creating predicate
	   	Predicate<String> pr = message -> (message == "Hi"); 
	  	System.out.println(pr.test("Hey"));	
	  	
    	Resources r = Employee::downloadResources;
		r.download();
		
		Supplier<Double> randomValue = () -> Math.random();
		// Creating Supplier
		System.out.println("Creating and Testing a Supplier:"+randomValue.get());
	} 
}
