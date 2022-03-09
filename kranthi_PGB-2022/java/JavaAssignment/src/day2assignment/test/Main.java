package day2assignment.test;

import day2assignment.util.Fact;

public class Main {
	public static void main(String args[]) {
		Student st1=new Student();
		Student st2=new Student();
		st1.override("kanthi", 3);
		st1.override("kanthi", 3,21);
		
		
		System.out.println(Fact.factorialrec(5));
		System.out.println(Fact.factorial(4));
		
		
	}

}