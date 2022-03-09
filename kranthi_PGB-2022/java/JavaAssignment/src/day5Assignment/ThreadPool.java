package day5Assignment;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadPool {
	public static void main (String args[]) {
	ExecutorService executor= Executors.newFixedThreadPool(5);//Executorservice to execute threads of the thread pool
	for(int i=0;i<10;i++) {
		Runnable worker =new WThread(""+i);
		executor.execute(worker);
	}
	executor.shutdown();  
    while (!executor.isTerminated()) {   }  

    System.out.println("Finished all threads");  
	
	}

}
