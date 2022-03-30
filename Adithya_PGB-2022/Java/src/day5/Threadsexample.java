package day5;
import java.util.*;
import java.util.concurrent.*;

import day2.Student;
class MyThread implements Runnable{
	ArrayList<Student>stu;
	MyThread(ArrayList<Student>l){
		this.stu=l;
	}
	//synchronized method
	synchronized public void run() {
		for(Student l:stu) {
			System.out.println("Student ID "+l.rollno+" StudentName "+l.name);
		}
	}
	public void print() {
		synchronized(this) {
			System.out.println("Hi");
		}
	}
}
public class Threadsexample {
	public static void main(String[]args) {
		ArrayList<Student>al=new ArrayList();
		for(int i=0;i<100;i++) {
			al.add(new Student(100-i,"Employee "+i));
		}
		ArrayList<Student>bl=new ArrayList();
		for(int i=150;i<300;i++) {
			al.add(new Student(1000-i,"Employee "+(i+1000)));
		}
		//Executor 
		ExecutorService e=Executors.newFixedThreadPool(2);
		e.execute(new MyThread(al));
		e.execute(new MyThread(bl));
		e.shutdown();
	}
}
//execute(new ThreadTask())