package day5assignment;
import java.util.Arrays;
import java.util.*;
import java.util.List;
import java.util.concurrent.ExecutorService;  
import java.util.concurrent.Executors;
import java.util.stream.Collector;
import java.util.stream.Collectors; 

class empname{
	String empname="vinaykumar";
	int id = 123;

	public void empname(String string){
		
		System.out.println("Employee name :"+empname);
	}
	public void empid(int i) {
		System.out.println("Employee id :"+id);
	}
}
class WorkerThread implements Runnable{
	private String message;
	public WorkerThread(String s) {
		this.message = s;
	}
	public void run() {
		System.out.println(Thread.currentThread().getName() + "(Start) message = " +message);
		processmessage();
		System.out.println(Thread.currentThread().getName()+"(End)");
	}
	private void processmessage() {
		try {
			Thread.sleep(2000);
		}
		catch(InterruptedException e) {
			e.printStackTrace();
		}
	}
}

class comparator {
	public int compare(int a,int b) {
		return a-b;
	}
}

public class TestThreadPool{
	public static void main(String[] args) {
		ExecutorService executor = Executors.newFixedThreadPool(5);
		for(int i = 0; i < 10; i++) {
			Runnable worker = new WorkerThread(""+i);
			executor.execute(worker);
		}
		executor.shutdown();
		while(!executor.isTerminated()) {}
		System.out.println("Finished all Threads");
		comparator c=new comparator();
		//Method Reference
		List<Integer> numbers = Arrays.asList(5, 3, 50, 24, 40, 2, 9, 18);
		System.out.println(numbers.stream().sorted(c::compare).collect(Collectors.toList()));
		
		//objects
		 empname p =new empname();
    	 p.empname("vinaykumar");
    	 
    	 empname p1 = new empname();
    	 p1.empid(123);
    	 
	}
}
