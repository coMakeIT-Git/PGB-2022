package Day5.task1;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
public class pool {
	public static void main(String[] args){
		//Initiate the Pool
				ExecutorService ex = Executors.newFixedThreadPool(2); //recycle Threads
				//Now submit task to the above ThreadPool
				Runnable t1 = new Transaction("EMP-1");
				ex.execute(t1);
				Runnable t2 = new Transaction("EMP-2");
				ex.execute(t2);
				Runnable t3 = new Transaction("EMP-3");
				ex.execute(t3);
				
				ex.shutdown(); // Rejects aby new tasks from being submitted.
				
				//ex.shutdownNow(); //Only two are processed and the other gets collapsed.
				
				while(!ex.isTerminated()){
				}
				System.out.println(" all the transactions are done !!");
}
}