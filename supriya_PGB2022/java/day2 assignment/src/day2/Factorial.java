package day2;
import java.util.Scanner;
public class Factorial {
static int recFactorial(int n) {
	
	if(n==0) 
		return 1;
	else {
		return (n*recFactorial(n-1));
	}
}
static int nrFactorial(int n) {
	
	int fact=1;
	if(n==0)
		return 1;
		else
		{
			for(int i=1;i<=n;i++)
			fact=fact*i;
			//System.out.println("factorial of"+num+"using Non-Recursion is"+fact);
		}
	return fact;
}
public static void main(String args[]) {
	Scanner sc=new Scanner(System.in);
	System.out.println("enter number:");
	int num=sc.nextInt();
	int res1=recFactorial(num);
	System.out.println("non recursive:"+res1);
	int res2=nrFactorial(num);
	System.out.println("recursive:"+res2);
	
	//System.out.println("factorial of"+num+"using Recursion"+recFactorial(num));
}
}
