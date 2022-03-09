package saikeerthana;
class Table  
{      
 void printTable(int n){    
   synchronized(this){//synchronized block    
     for(int i=1;i<=5;i++){    
      System.out.println(n*i);    
      try{    
       Thread.sleep(400);    
      }catch(Exception e){System.out.println(e);}    
     }    
   }    
 }
 //end of the method  
 synchronized void printTable1(int x) // First synchronized method.
 {
 for(int i = 1; i <= 3; i++)
 {  
  System.out.println(x * i);  
  try
  {  
    Thread.sleep(400);  
  }
 catch(InterruptedException ie)
 {
  System.out.println(ie);
  }  }
 }  
 synchronized void printTable2(int y) // Second synchronized method.
 {
 for(int j = 1; j <= 3; j++)
 {  
  System.out.println(y * j);  
  try
  {  
    Thread.sleep(400);  
  }
 catch(InterruptedException ie)
 {
  System.out.println(ie);
  }  }
 } 
}    
    
class MyThread1 extends Thread{    
Table t;    
MyThread1(Table t){    
this.t=t;    
}    
public void run(){    
t.printTable(5);    
}    
    
}    
class MyThread2 extends Thread{    
Table t;    
MyThread2(Table t){    
this.t=t;    
}    
public void run(){    
t.printTable(100);    
}    
}    
      
 class Thread1 extends Thread
{
Table t; // Declaration of variable t of class type Table.
Thread1(Table t)
{  
  this.t = t;  
}  
public void run()
{  
   t.printTable1(2); // Calling first synchronize dmethod.
 }  
}
 class Thread2 extends Thread
{
Table t;  
Thread2(Table t)
{  
   this.t = t;  
}  
public void run()
{  
   t.printTable2(10); // Calling second synchronized method.
 }  
}



public class Synchronisation {
	public static void main(String[] args) 
	{
	// Create two objects of class Table.
		Table obj=new Table();
		MyThread1 t1=new MyThread1(obj);    
		MyThread2 t2=new MyThread2(obj);    
		t1.start();    
		t2.start(); 
	  Table obj1 = new Table();
	  Table obj2 = new Table();

	Thread1 t3 = new Thread1(obj1);
	Thread2 t4 = new Thread2(obj2);
	 t3.start(); 
	 t4.start();
	 }
}

