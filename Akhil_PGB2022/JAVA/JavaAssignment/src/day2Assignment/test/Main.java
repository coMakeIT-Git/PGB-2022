package day2Assignment.test;
import day2Assignment.util.Factorial;
public class Main {
	public static void main(String[] args) {
		Employee e1 = new Employee(1,"Kumar","kumar@mail.com");
		Employee e2 = new Employee(1,"Kumar","kumar@mail.com");
		System.out.println("Employee details: ");
		e1.display(1, "kumar");
		e2.display(1, "kumar","kumar@mail.com");
		System.out.println("\ncomparing 2 objects using equal method");
		System.out.println(e1.equals(e2));
		

		//Factorial 

		System.out.println("\nFactorial using recursion: "+Factorial.recursiveFunction(4));
		System.out.println("Factorial without recursion: "+Factorial.nonRecursiveFunction(7));
		

	}
}