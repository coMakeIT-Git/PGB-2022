package Day2.Util;
import java.util.*;
public class Factorial {
	 static int recursive(int n){
		if(n==0 || n==1)return n;
		return n*recursive(n-1);
	}
	static int non_recursive(int n)
	{
		int f=1;
		for(int i=1;i<=n;i++)
			f=f*i;
		return f;
	}
	public static void main(String args[])
	{
		System.out.println(recursive(5));
		System.out.println(non_recursive(10));	
	}
	
}
