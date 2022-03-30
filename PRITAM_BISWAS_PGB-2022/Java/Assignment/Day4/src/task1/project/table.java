package task1.project;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;
@SuppressWarnings("unused")
public class table {
    public static String tname;
    public static int id,a,b;
	
	public static void main (String args[]) throws IOException
	{ 
		// scan input 
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter a name :");
		tname=sc.nextLine();
		System.out.println("Enter ID:");
		id=sc.nextInt();
		// add 2 numbers
		System.out.println("Enter number 1:");
		a=sc.nextInt();
		System.out.println("Enter number 1:");
		b=sc.nextInt();
		System.out.println("Name:"+tname+"\t"+"ID:"+id);
		System.out.println("Add number 1 and 2:"+(a+b));
		
		// null pointer Exception
		System.out.println("Null Point EXception:");
		
	 try {    
		 String name =null;
             System.out.println(name.length());
	     }
   catch(NullPointerException e)
	     {
		    System.out.println("Null pointer Exception Occurred");
	     }
	 
	   // Number format Exception
	   System.out.println("Number Format EXception:");
	   System.out.println("Number Format :");
	try{
		String str;
		str=sc.next();
		int number;
		number=Integer.parseInt(str);
		System.out.println("Number Entered :"+number);
		}
		catch(NumberFormatException e)
		{
			System.out.println("Number Format Exception Occured");
		}
		
		//custom exception
		
		System.out.println("Custom EXception:");
		 System.out.println("Enter Number :");
		 try  
	        {  
	           
			 int a;
			 a=sc.nextInt();
			 if(a>100)
			 {
				 System.out.println("Number :"+a);
			  }
			 else
			 {
				 throw new Exception("Your Input is less than 100 :"+a);
			 }
	             
	        }  
	        catch (Exception ex)  
	        {  
	            System.out.println("Custom exception occured ");  
	           
	        }  		 
	}
}