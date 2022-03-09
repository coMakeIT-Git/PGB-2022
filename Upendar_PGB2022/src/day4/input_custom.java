package day4;

import java.util.*;

import day2.student;
class MyCustomException extends Exception  
{  
    
}  
public class input_custom extends student{

	public static void main(String[]args) 
	{
	Scanner sc = new Scanner(System.in);
	System.out.println("enter the numbers");
	 int a = sc.nextInt();
	 int b = sc.nextInt();
     System.out.println("integer1 " + a);
     System.out.println("integer2 " + b);
     System.out.println("The sum is =" + Integer.sum(a, b));
	String ptr = null;
	try
	{
		if (ptr.equals("console"))
		{
			System.out.print("Same");
		}
		else {
			System.out.print("Not Same");
		}
	}
	catch(NullPointerException e)
	{
		System.out.print("NullPointerException Caught");
	}
	while (true) 
		{
        System.out.println("Enter any valid Integer: ");
        try {
            int number = Integer.parseInt(sc.next());
            System.out.println("You entered: "+number);
            break;
        }
        catch (NumberFormatException e) {
            System.out.println("NumberFormatException occurred");
        }
    }   
		 try  
	        {  
	            throw new MyCustomException();  
	        }  
	        catch (MyCustomException ex)  
	        {  
	            System.out.println("Caught the exception");  
	              
	        }    
	    }  
 
}
