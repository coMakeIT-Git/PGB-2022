package day4assignment;
import java.util.Scanner;

class MyException extends Exception {
	MyException(){
		super();
	}
}

public class demo {
	public static void validateSum(int sum)throws Exception{
		if(sum > 2000) {
			throw new MyException();
		}
	}
	public static void main(String[] args) {
		try {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter numbers:");
			String str = sc.nextLine();
			String[] arr = str.split(" ");
			int sum = 0;
			for(int i = 0; i < arr.length; i++) {
				sum += Integer.parseInt(arr[i]);
			}
			validateSum(sum);
			System.out.println("Sum: " +sum);
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
}