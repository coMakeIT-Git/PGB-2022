package day5;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
class newone{
	synchronized
	static void mymethod(String name) {
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
					//prints the initialization time for every task
				}
				else
				{
					Date d = new Date();
					SimpleDateFormat ft = new SimpleDateFormat("hh:mm:ss");
					System.out.println("Executing Time for task name - "+
							name +" = " +ft.format(d));
					// prints the execution time for every task
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
class Task implements Runnable
{
	private String name;
	
	public Task(String s)
	{
		name = s;
	}
	
	public void run()
	{
		newone.mymethod(name);
	}
}
public class threadpool
{
	// Maximum number of threads in thread pool
	static final int MAX_T = 3;			

	public static void main(String[] args)
	{
		// creates five tasks
		Runnable r1 = new Task("task 1");
		Runnable r2 = new Task("task 2");
		Runnable r3 = new Task("task 3");
		Runnable r4 = new Task("task 4");
			

		ExecutorService pool = Executors.newFixedThreadPool(MAX_T);

		pool.execute(r1);
		pool.execute(r2);
		pool.execute(r3);
		pool.execute(r4);

		
		// pool shutdown
		pool.shutdown();	
	}
}
