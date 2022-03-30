package Day5.task1;

public class Transaction implements Runnable{
	private String msg;
	//constructor of the class
	public Transaction(String m){
		this.msg = m;
	}
	public void run(){
		synchronized (this) {
			System.out.println(Thread.currentThread().getName() + "Intialised Transaction for = " + msg);
			dosometasks(); //make the thread sleep to simulate doing some work
			System.out.println(Thread.currentThread().getName() + " Transaction is done for = " + msg);
		}
		}
	private synchronized void dosometasks()
	{
		try
		{
			Thread.sleep(2000);
		}
		catch(InterruptedException e)
		{
			System.out.println("Unable to process Transaction");
		}
	}
}
