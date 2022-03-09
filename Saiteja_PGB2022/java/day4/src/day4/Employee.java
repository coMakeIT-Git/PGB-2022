package day4;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.Scanner;
class AgeRestictionException extends Exception{
	AgeRestictionException(String s){
		super(s);
	}
}
public class Employee {
	public static void main(String args[]) throws IOException
	{
		Scanner sc=new Scanner(System.in);
		//taking input from console
		int id1=sc.nextInt();
		System.out.println("u have entered input id1:"+id1);
		//printing taken input from console
		int id2=sc.nextInt();
		System.out.println("u have entered input id2:"+id2);
		//adding two ids
		System.out.println("sum of two input ids:"+(id1+id2));
		//null pointer exception
		try {
			String name=null;
			System.out.println(name.length());
		}
		catch(NullPointerException e)
		{
			System.out.println("null pointer exception occured");
		}
		
		//number format exception
		System.out.println("enter input for number format exception");
		try {
			int number;
			number = Integer.parseInt(sc.next());
			System.out.println("You entered: "
	                + number);
		}
		catch(NumberFormatException e)
		{
			System.out.println("number format exception occured");
		}
		//Custom Exception
		System.out.println("enter input for custom exception");
		try {
			int empage;
			empage = Integer.parseInt(sc.next());
			if(empage >= 18)
			System.out.println("Your age is applicable");
			else
			{
				throw new AgeRestictionException("your input is less than minimum age required : "+empage);
			}
		}
		catch(AgeRestictionException e)
		{
			System.out.println("Age Restriction exception occured");
			System.out.println(e.getMessage());
		}
		//Runtime Exception(unChecked Exception)
		try {
			int id4=100,id5=0;
			System.out.println(id4/id5);
		}
		catch(ArithmeticException e)
		{
			System.out.println("Arithemetic exception(Runtime and unchecked) occured");
		}
		
		//checked Exception
		
		FileReader file = new FileReader("C:\\test\\a.txt");
		  
        
        BufferedReader fileInput = new BufferedReader(file);
  
        
        for (int counter = 0; counter < 3; counter++)
            System.out.println(fileInput.readLine());
  
        fileInput.close();
		
		
	}

}
