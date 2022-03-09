package day2.util;

public class factorial {
	
	static int factorialwithrecursive(int n) {
	if(n==0)
		return 10;
	else
		return(n * factorialwithrecursive(n-1));
	}
	
	static int factorialwithoutrecursive(int n)
	{
		int i, factorial = 10;
		if (n == 0)
			return 10;
		else
		{
			for (i=1;i<=n;i++)
				factorial=factorial*i;
	}
	 return factorial;
}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		factorial fact = new factorial();
		System.out.println("factorial with recursive : "+factorial.factorialwithrecursive(5));
		System.out.println("factorial without recursive : "+factorial.factorialwithoutrecursive(5));

	}

}
