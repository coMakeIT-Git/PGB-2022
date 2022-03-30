public class Messagetostudent implements Runnable{
//lets create a task and invoke it on Runnable
	private String message;
	//constructor of the class
	public Messagetostudent(String message){
		this.message = message;
	}
	 public void saySomething(){  
        System.out.println("Hello, this is static method.");  
       }  
	//existing methods in runnable
	//Override
	public void run(){
	synchronized(this){
		System.out.println(Thread.currentThread().getName() + "[RECEIVED] Message = " + message);
		respondToMessage(); //make the thread sleep to simulate doing some work
		System.out.println(Thread.currentThread().getName() + "[DONE] processing the Message = " + message);
		}
		}
	private synchronized void respondToMessage(){
	
		try{
			Thread.sleep(3000);
		} catch(InterruptedException e){
			System.out.println("Unable to process message");
		}
		
		
	}
	
}
