package day2Assignment.util;

public class Fact {
	public static int factorialrecursion(int n) {
		if(n==1) {
			return 1;
		}
		else {
			return n*factorialrecursion(n-1);
		}
	}
	
	public static int factorial(int n) {
		int f=1;
		for(int i=1;i<=n;i++) {
			f=f*i;
		}
		return f;
	}
}