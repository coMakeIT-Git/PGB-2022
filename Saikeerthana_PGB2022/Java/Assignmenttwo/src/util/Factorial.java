package util;
import java.util.*;
public class Factorial {

	public static int nonrecursivefactorial(int num) {
	     int f=1;
	     if(num==0)
	         return 1;
	     for(int i=1; i<=num; i++) {
	         f=f*i;
	      }
	         return f;
	    }


	
	public static int recursivefactorial(int num) {
		if(num==0)
	        return 1;

	    else
	        return num * recursivefactorial(num - 1);

	}
	   
	public static void main(String[] args) {
	
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter a number:");
		int num=sc.nextInt();
		int res=nonrecursivefactorial(num);
		System.out.println("Non recursive Factorial:"+res);
		int ans=recursivefactorial(num);
		System.out.println("recursivefactorial:"+ans);
	
}
}