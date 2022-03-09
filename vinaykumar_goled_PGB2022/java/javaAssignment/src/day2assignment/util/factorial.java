package day2assignment.util;
import java.util.*;

import day2assignment.util.factorialMethods;
public class factorial extends factorialMethods {
	public static void main(String[] args) {
		Scanner s1 = new Scanner(System.in);
		System.out.println("Enter a number:");
		int number = s1.nextInt();
		int f = 1;
		f = recursive(number);
		System.out.println("Factorial of a number using a recursive function: " +f);
		int nr = 1;
		nr = nonRecursive(number);
		System.out.println("Factorial of a number using a non recursive function: " +nr);
		s1.close();
	}
}
