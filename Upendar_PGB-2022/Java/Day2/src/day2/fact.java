package day2;
public class fact {
	static int with_recursion(int n) {
		if(n == 0)
			return 1;
		else
			return(n * with_recursion(n-1));
	}
	static int without_recursion(int n) {
		int i,fact =1;
		if(n==0)
			return 1;
		else {
			for(i=1;i<=n;i++) {
				fact=fact*i;
			}
		}
		return fact;
	}
	public static void main(String[]args) {
		System.out.println("factorial withrecursion:"+fact.with_recursion(5));
		System.out.println("factorial without recursion:"+fact.without_recursion(5));
	}

}
