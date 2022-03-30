package day5_assignment;
interface Messageable{  
    Message getMessage(String msg);  
}  
class Message{  
    Message(String msg){  
        System.out.print(msg);  
    }  
}  
public class MethodReference {
	public static void ThreadStatus(){  
        System.out.println("Thread is running...");  
    }  
	 public void printnMsg(){  
	        System.out.println("This is instance method");  
	    }  
public static void main(String[] args) {  
	        Thread t1=new Thread(MethodReference::ThreadStatus);  
	        t1.start();   
	        Thread t2=new Thread(new MethodReference()::printnMsg);  
	        t2.start();
	        Messageable hello = Message::new;  
	        hello.getMessage("Message");  
	    }  
}
