package Day2Assignment.Util;

import java.util.Scanner;



class Factorial
{
	public static void main(String[] args)
	{
		Scanner sc=new Scanner(System.in);
		//Fact obj=new Fact();
		int n=sc.nextInt();
		int n1=sc.nextInt();
		System.out.println("Factorial of"+n+" using non_recursive is:");
		System.out.println(Fact.non_recursive(n));
		System.out.println("Factorial of"+n1+" using recursive is:");
		System.out.print(Fact.recursive(n1));
	}
}