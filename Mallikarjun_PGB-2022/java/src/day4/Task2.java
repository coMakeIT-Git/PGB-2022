package day4;

import java.util.*;
import java.util.ArrayList;
import java.util.function.Consumer;

import day2.Student;

class Exception2 extends Exception 
{
	public static void main(String[] args) {
		System.out.println("Custom Exception");
	}
}
	public class Task2 {
		static ArrayList<Integer> numbers = new ArrayList<Integer>();
		
		public static void main(String[] args) {
			
			Scanner sc = new Scanner(System.in);  
			
			String ptr = null;
			 
			try
			{
				if(ptr.equals("Console"))
				{
					System.out.println("Same");
				}
				else
				{
					System.out.println("Not Same");
				}
			}
			catch(NullPointerException e)
			{
				System.out.println("NullPointerException Caught");
			}
			while(true)
			{
				System.out.println("Enter valid Integer : ");
				try
				{
					int number = Integer.parseInt(sc.next());
					System.out.println("You entered : "+number);
					break;
				}
				catch(NumberFormatException e) {
					System.out.println("NumberFormatException Occured");
				}
			}
			try {
				throw new Exception2();
			}
			catch (Exception2 ex)
			{
				System.out.println("Caught the exception");
			}
		
		numbers.add(7);
	    numbers.add(6);
	    numbers.add(5);
	    numbers.add(4);
		Consumer<Integer> method = (n) -> { System.out.println(n); };
	    numbers.forEach( method );
	    
	    new Thread(() -> {
	    	System.out.println("New Thread Created");
	    }).start();
	    }

}
