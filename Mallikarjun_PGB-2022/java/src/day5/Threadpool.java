package day5_Assignment;

import java.text.SimpleDateFormat;
import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class Task{

	synchronized
	static void method(String name)
	{
		try
		{
			for(int i=0; i<=4; i++)
			{
				if(i==0)
				{
					Date d = new Date();
					SimpleDateFormat ft = new SimpleDateFormat("mm:ss");
					System.out.println("Initialization Time For " + "Task name - " + name + " = " +ft.format(d));
				}
				else {
					Date d = new Date();
					SimpleDateFormat ft = new SimpleDateFormat("mm:ss");
					System.out.println("Execution Time For " + "Task name - " + name + " = " +ft.format(d));
				}
				Thread.sleep(1000);
			}
			System.out.println(name + "Complete");
		}
		catch(InterruptedException e) {
			e.printStackTrace();
		}
	}
	
}
class Task1 implements Runnable
{
	private String name;
	
	public Task1(String s)
	{
		name = s;
	}
	public void run()
	{
		Task.method(name);
	}
}
public class Threadpool
{
	static final int MAX_T = 3;
	
	public static void main(String[] args) {
		Runnable r1 = new Task1("task 1");
        Runnable r2 = new Task1("task 2");    
        Runnable r3 = new Task1("task 3");
        Runnable r4 = new Task1("task 4");
        ExecutorService pool = Executors.newFixedThreadPool(MAX_T);  

        pool.execute(r1);
        pool.execute(r2);
        pool.execute(r3);
        pool.execute(r4);
        
        pool.shutdown();
	}
}


