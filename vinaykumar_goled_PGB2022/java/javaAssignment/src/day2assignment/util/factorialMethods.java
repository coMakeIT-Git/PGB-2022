package day2assignment.util;

public class factorialMethods {
	static int recursive(int n) {
		if(n == 0) {
			return 1;
		}
		else {
			return (n * recursive(n-1));
		}
	}
	static int nonRecursive(int n) {
		int mul = 1;
		for(int i = 1; i <= n; i++) {
			mul = mul * i;
		}
		return mul;
	}
}
