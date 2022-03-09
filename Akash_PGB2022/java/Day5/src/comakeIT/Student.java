package comakeIT;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

// Add a thread pool in your class.
// Implement the Runnable Interface.
class Student implements Runnable {

	String name;
	
	public Student(String name) {
		this.name = name;
	}

	  public void run() {
		  //synchronized block 
		  synchronized(this){
			for(int i=0;i<=3;i++) {
				System.out.println(name+i);
				Stop();
					
			}	
	}}
	  
	 //synchronized method 
	  synchronized public void Stop(){
		  try {
			  Thread.sleep(2000);
		  }
		catch(InterruptedException e) {
			System.out.println(e.getMessage());
		}
	}
	
	public static void main(String[] args) {
		//Build list of objects of your class.
		Runnable r1=new Student("Student1");
		Runnable r2=new Student("Student2");
		Runnable r3=new Student("Student3");
		
		//Use Executor framework
		ExecutorService e = Executors.newFixedThreadPool(3);
		//Print attributes of your class objects using multiple threads 
		e.execute(r1);
		e.execute(r2);
		e.execute(r3);
		
		e.shutdown();
		
	}
}

