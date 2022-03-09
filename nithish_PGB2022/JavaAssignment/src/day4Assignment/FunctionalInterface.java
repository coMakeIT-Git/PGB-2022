package day4Assignment;


interface functional {
	//Single abstract Method
	public int avg(int x,int y);
}

public class FunctionalInterface{
	public static void main(String args[]){
	  
	  //implementing using lambda expression
	  functional average=(int x,int y)->(x+y)/2;
	  System.out.println(average.avg(10, 15));
	  
	  //functional interface from Runnable interface
	  new Thread(()->{System.out.println("New Thread");}).start();
  }
}
