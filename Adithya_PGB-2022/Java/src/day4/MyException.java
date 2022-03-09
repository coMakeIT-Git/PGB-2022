package day4;
import java.util.*;
//Custom Functional Interface
interface average{
	float cal(int x,int y);
}


//custom exception
class MyException extends Exception{
	MyException(String s){
		super(s);
	}
	public static void func(int n) throws ArithmeticException{
		System.out.println(n/0);
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=0;
		String str=null;
		try{
			n=str.length();
		}
		//handling NullPointerException
		catch(NullPointerException npe){
			System.out.println("NullPointer exception");
		}
		try{
			//taking input from console
			String[] s=sc.nextLine().split(" ");
			//printing the input
			int ans=0;
			for(int i=0;i<s.length;i++){
				System.out.print(s[i]+" ");
				//calculating the sum of integers
				ans+=Integer.parseInt(s[i]);
			}
			if(ans<10){
				//Custom exception for sum
				throw new MyException("value sent is "+ans);
			}
			System.out.println(ans);
		}
		//handling NumberFormatException
		catch(NumberFormatException e){
			System.out.println("NumberFormatException");
		}
		catch(MyException me){
			System.out.println("Caught");
			System.out.println(me.getMessage());
		}
		try{
			func(10);
		}
		catch(ArithmeticException e){
			//propogated to main class
			System.out.println("Error found");
		}
		//RunTimeException
		try {
			System.out.println(5/0);
		}
		catch(ArithmeticException re) {
			re.printStackTrace();
		}
		//functional Interface in java library and lambda implementation
		new Thread(()->{System.out.println("New thread");}).start();
		//Implementing the method of functional interface as lambda expression
		average a=(int x,int y)->(x+y)/2;
		System.out.println(a.cal(5,6));
	}
}

