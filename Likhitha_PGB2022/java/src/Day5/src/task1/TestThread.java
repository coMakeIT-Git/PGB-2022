package task1;

import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

 class Task implements Runnable {
    private String name;
    private int taskNumber=15;
    
    public Task(String name) {
        this.name = name;
    }
 
    public String getName() {
        return name;
    }
    
    public int gettaskNumber()
    {
    	return taskNumber;
    }
 
    public void run() {
        try {
            Long duration = (long) (Math.random() * 10);
            System.out.println("Executing : " + name);
            TimeUnit.SECONDS.sleep(duration);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class TestThread {
   public static void main(String[] args)
   {
	   ThreadPoolExecutor exe= (ThreadPoolExecutor) Executors. newFixedThreadPool(2);
	   
	   for (int i = 1; i <= 5; i++) 
       {
		   //Build list of objects
           Task task = new Task("Task " + i);
           //Accessing attributes
           System.out.println("Created : " + task.getName());
         if(i==5)
        	 {System.out.println(task.gettaskNumber());
        	 }
        	 
           exe.execute(task);
       }
//	   System.out.println(task.gettaskNumber());
       exe.shutdown();
	   
   }
}
