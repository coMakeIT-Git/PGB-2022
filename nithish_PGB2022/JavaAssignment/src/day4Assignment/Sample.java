package day4Assignment;
import java.util.*;

class MyException extends Exception {
	public MyException() {
		super();
	}
}

class test{
	public static void validate(int sum) throws Exception{
		throw new MyException();
	}
}

public class Sample {
	public static int sum(String s[]) {
		int sum1=0;
		for(int i=0;i<s.length;i++) {
			sum1+=Integer.parseInt(s[i]);
		}
		return sum1;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		try {
			System.out.println("Enter numbers");
			String str=sc.nextLine();
			String s[]=str.split(" ");
			int s1=sum(s);
			System.out.println("sum of integers: "+s1);
			if(s1>100) {
				throw new MyException();
			}
			
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		sc.close();
	}
}
