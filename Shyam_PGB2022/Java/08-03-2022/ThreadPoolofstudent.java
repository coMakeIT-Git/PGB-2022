import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.function.Predicate; 
public class ThreadPoolofstudent{
	public static void main(String[] args){
		Thread t2=new Thread(Messagetostudent::saySomething());  
        	t2.start();  
    
		//Initiate the Pool
		ExecutorService ex = Executors.newFixedThreadPool(2); //recycle Threads
		//Now submit task to the above ThreadPool
		Runnable processor = new Messagetostudent("CMI-T1079");
		ex.execute(processor);
		Runnable processor1 = new Messagetostudent("18331A0534");
		ex.execute(processor1);
		Runnable processor2 = new Messagetostudent("Shyam sai Dogga");
		ex.execute(processor2);
		
		ex.shutdown(); // Rejects all new tasks from being submitted.
		
		ex.shutdownNow(); //Only two are processed and the other gets collapsed.
		
		while(!ex.isTerminated()){
		}
		System.out.println("Submitted all the tasks");
	}
}
