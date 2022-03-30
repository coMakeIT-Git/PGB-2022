package saikeerthana;

import java.util.Scanner;

class InvalidException extends Exception
{
	public InvalidException (String line)  
    {  
        
        super(line);  
    }  
}
public class Program {
	void productCheck(int weight) throws InvalidException{
		if(weight<100){
			throw new InvalidException("Product Invalid");
		}
	   }
	public static void main(String[] args)
{	
		Program obj = new Program();
        try
        {
            obj.productCheck(60);
        }
        catch (InvalidException ex)
        {
            System.out.println("Caught the  custom exception");
            System.out.println(ex.getMessage());
        }
	Scanner scanner=new Scanner(System.in);
	System.out.println("Enter a string");
	String line = scanner.nextLine();
	String[] numberStrs = line.split(",");
	int[] numbers = new int[numberStrs.length];
	for(int i = 0;i < numberStrs.length;i++)
	{
	  
	   try
	   {numbers[i] = Integer.parseInt(numberStrs[i]);
	   }
	   catch(NumberFormatException exe)
	   {
		   System.out.println("exception caught"+exe);
	   }
	}
	int sum=0;
	for(int i=0;i<numbers.length;i++)
	{
		sum=sum+numbers[i];
	}
	System.out.println("Sum of the numbers is:"+sum);


	//NullPointer EXception
	String str=null;
	try
	{
		if(str.equals("hello"))
		{
			System.out.println("Both are equal");
		}
		else
		{
			System.out.println("Both are not equal");
		}
	}
	catch(NullPointerException e)
	{
		System.out.println("NUllpointer exception caught");
	}
	//Runtime exception
	 try

	  {
	  int array[] = { 6, 16, 26,36,46,56,66,76 };
	  
	  System.out.println(array[9]);  

	  }

	   catch( ArrayIndexOutOfBoundsException e ) 

	  { 
	   System.out.println( "Runtime Exception caught:Valid indexes are 0, 1,2,3, 4,5,6 or 7" );

	  }
	   
	finally
	{
		System.out.println("End of program");
	}
}
}



