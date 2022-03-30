package day5Assignment;

public class WThread implements Runnable{
	private String message;
	WThread(String  s){
		this.message=s;
	}
	//overiding the run method of Runnable interface
public void run() {
	System.out.println(Thread.currentThread().getName()+"(Start) Message="+message);
	processmessage();
	System.out.println(Thread.currentThread().getName()+"(Start) End");

}
//Method that makes the thread to sleep for 2 seconds
private void  processmessage(){
	try {
		Thread.sleep(2000);
	} catch (InterruptedException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
}

}
