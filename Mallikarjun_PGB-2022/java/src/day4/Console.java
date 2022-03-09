package day4;

import java.util.*;

import day2.Student;
class MyCustomException extends Exception
{
	
	
}


public class Console{
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);  
		System.out.print("Enter the number: ");  
		int a  = sc.nextInt();  
		int b  = sc.nextInt();
		System.out.print("Enter the first number: "+a); 
		System.out.print("Enter the second number: "+b);  
		
		
		System.out.println("The sum of two numbers a and b is: " + Integer.sum(a, b));
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
			throw new MyCustomException();
		}
		catch (MyCustomException ex)
		{
			System.out.println("Caught the exception");
		}
		
		
	}
}

