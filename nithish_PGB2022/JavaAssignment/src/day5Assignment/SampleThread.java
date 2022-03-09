package day5Assignment;
import day2Assignment.test.Student;
import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


class ThreadTask implements Runnable{
	List<Student> stu;
	ThreadTask(List<Student> s){
		this.stu=s;
	}
	
	synchronized public void run() {
		for(Student s:stu) {
			System.out.println("id:"+s.getid()+" Name:"+s.getname()+" Marks:"+s.getmarks());
		}
	}
}
public class SampleThread {
	public static void main(String[] args) {
		List<Student> s1=new ArrayList<>();
		for(int i=1;i<=50;i++) {
			s1.add(new Student(i,"name"+i,i*2));
		}
		List<Student> s2=new ArrayList<>();
		for(int i=1;i<=50;i++) {
			s2.add(new Student(100+i,"name"+(100+i),i*3));
		}
		
		ExecutorService ex=Executors.newFixedThreadPool(4);
		ex.execute(new ThreadTask(s1));
		ex.execute(new ThreadTask(s2));
		
		ex.shutdown();
	}
}
