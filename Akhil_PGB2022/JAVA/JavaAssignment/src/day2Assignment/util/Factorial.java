package day2Assignment.util;

public class Factorial {
	public static int  recursiveFunction(int x) {
		
		if(x==1)
			return 1;
		else
			return x*recursiveFunction(x-1);
	}
	
	public static int nonRecursiveFunction(int n) {
		int fact = 1;
		for(int i=1;i<=n;i++) {
			fact *= i;
		}
		return fact;
	}
	
}
