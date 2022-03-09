package util;
import java.util.Scanner;

public class Factorial {

	public static int nonrecursivefactorial(int num) {
		 int n=1;
		 if(num==0)
			 return 1;
		 for(int i=1;i<=num;i++) {
			 n=n*i;
		 }
		 return n;
	 }
	 public static int recursivefactorial(int num) {
		 if(num==0)
			 return 1;
		 else
			 return(num*recursivefactorial(num-1));
		 }
	 public static void main(String args[]) {
	 Scanner input =new Scanner(System.in);
		Factorial obj=new Factorial();
		System.out.println("enter number:");
		int num=input.nextInt();
		int result=nonrecursivefactorial(num);
		System.out.println("factorial non recursive:" +result);
		int ans=recursivefactorial(num);
		System.out.println("factorial recursive:" +ans);
}
}
