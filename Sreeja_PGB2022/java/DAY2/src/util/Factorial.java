package util;
import java.util.*;
import java.util.Scanner;

public class Factorial {
	public static int nonrecursive(int x) {
		int n=1;
		if(x==0)
			return 1;
		for(int i=1;i<=x;i++) {
			n=n*i;
		}
		return n;
		
	}
public static int recursive(int x) {
	if(x==0)
		return 1;
	else
		return (x*recursive(x-1));
}
public static void main(String args[]) {
	Scanner s=new Scanner(System.in);
	Factorial f=new Factorial();
	System.out.println("number");
	int num=s.nextInt();
	int res1=nonrecursive(num);
	System.out.println("non-recursive:"+ res1);
	int res2=recursive(num);
	System.out.println("recursive:"+ res2);
}
}
