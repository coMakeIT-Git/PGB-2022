package Util;

public class Factorial {
  public static long recursive(int n)
  {
	  if(n==1)
		  return 1;
	  
	  return n*recursive(n-1);
  }
  
  public  static long nonrecursive(int n)
  {
	  if(n==1)
		  return 1;
	  int k=1;
	  for(int i=1;i<=n;i++)
	  {
		  k*=i;
	  }
	  return k;
  }
	public static void main(String[] args)
	{
		System.out.println(Factorial.recursive(5));
		System.out.println(Factorial.nonrecursive(6));
	}
}
