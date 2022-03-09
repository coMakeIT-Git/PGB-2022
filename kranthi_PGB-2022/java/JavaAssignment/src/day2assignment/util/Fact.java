package day2assignment.util;

public class Fact {
	public static int factorialrec(int n)
    {
        if (n == 0)
          return 1;
          
        return n*factorialrec(n-1);
    }
    
// non recursive fact 
 public static int factorial(int n)
    {
        int res = 1, i;
        for (i=2; i<=n; i++)
            res *= i;
        return res;
    }
}