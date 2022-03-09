package task1;
import java.text.SimpleDateFormat; 
import java.util.Date;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
//add implement the runnable interface.

class printempname{
	String empname="ram";

	public void printempname(String string){
		
		System.out.println("Table name :"+empname);
	}
}
class Task implements Runnable   
{

    private String name;

    public Task(String s)
    {
        name = s;
    }
    //create a synchronized method
    public synchronized void run()
    {  
        try
        {
            for (int i = 0; i<=5; i++)
            {
                if (i==0)
                {
                    Date d = new Date();
                    SimpleDateFormat ft = new SimpleDateFormat("hh:mm:ss");
                    System.out.println("Initialization Time for"
                            + " task name - "+ name +" = " +ft.format(d));   
                }
                else
                {
                    Date d = new Date();
                    SimpleDateFormat ft = new SimpleDateFormat("hh:mm:ss");
                    System.out.println("Executing Time for task name - "+
                            name +" = " +ft.format(d));   
                }
                Thread.sleep(1000);
            }
            System.out.println(name+" complete");
        }
        catch(InterruptedException e)
        {
            e.printStackTrace();
        }
    }
}



public class Employee
{
	//create thread pool in class
    static final int MAX_T = 3;             
    public static void main(String[] args)
    {
    	 printempname p =new printempname();
    	 p.printempname("Work Table");
    	 
        Runnable r1 = new Task("Task 1");
        Runnable r2 = new Task("Task 2");
        Runnable r3 = new Task("Task 3");
        Runnable r4 = new Task("Task 4");
        Runnable r5 = new Task("Task 5");   
        
       //create executor framework
        ExecutorService pool = Executors.newFixedThreadPool(MAX_T);  

        pool.execute(r1);
        pool.execute(r2);
        pool.execute(r3);
        pool.execute(r4);
        pool.execute(r5); 
        pool.shutdown();    
        
    }
}