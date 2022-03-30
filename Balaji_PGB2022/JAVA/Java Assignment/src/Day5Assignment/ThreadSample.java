package Day5Assignment;
import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Executors.*;
import java.util.concurrent.Executor;

import Day2Assignment.Task.Student;
class ThreadTask implements Runnable{
	List<Student> std;
	ThreadTask(List<Student> s){
		this.std = s;
	}
	@Override
	//implement the runnable interface
	synchronized public void run() {
		for(Student se:std) {
			System.out.println(" stuId"+se.getStid()+" stName"+se.getStname()+" empMail"+se.getStage());
		}
	}
}
public class ThreadSample {
 public static void main(String args[])
 {
	 // Build list of objects of your class.
	 List<Student> stuobj1=new ArrayList<>();
	 for(int i=1;i<100;i++)
	 {
		 stuobj1.add(new Student(101-i,"Name"+i,i+15));
	 }
	 List<Student> stuobj2=new ArrayList<>();
	 for(int i=1;i<100;i++)
	 {
		 stuobj1.add(new Student(101-i,"Name"+i,i+15));
	 }
	 ExecutorService ex = Executors.newFixedThreadPool(4);
		ex.execute(new ThreadTask(stuobj1));
		ex.execute(new ThreadTask(stuobj2));
		
		ex.shutdown();
 }
}
