package sreeja5;

import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

public class Task1 {
	 public static void main(String[] args) 
	    {
	        ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(2);
	        Runnable x=new Task("thread-1");
	        executor.execute(x);
	        Runnable y=new Task("thread-2");
	        executor.execute(y);
	        Runnable z=new Task("thread-3");
	        executor.execute(z);
	        for (int i = 1; i <= 5; i++) 
	        {
	            Task task = new Task("Task " + i);
	            System.out.println("Created : " + task.getName());
	            
	 
	            executor.execute(task);
	        }
	        executor.shutdown();
	    }

}
