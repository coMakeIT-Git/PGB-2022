package day4;
import java.util.InputMismatchException;
import java.util.Scanner;

class Main {
	public static void main(String[] args) throws ClassNotFoundException {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter a Class Name : ");
		String className = sc.next();
		try {
			Class temp = Class.forName(className);
			System.out.println("Class Exists");
		}
		catch (ClassNotFoundException e) {
			System.out.println("ClassNotFound Exception Occured (Checked)");
		}
		try {
			System.out.print("Enter a Number : ");
			int num = sc.nextInt();
		} catch (InputMismatchException e){
			System.out.println("InputMismatchException Exception Occured (UnChecked)");
		}
		new Thread(() -> System.out.print("Using Built-in Functional Interface (Thread) from java library")).start();
	}
}
