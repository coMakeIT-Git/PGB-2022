package task2.java;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import task3.functionalinterface;

public class checkndunchecexp {
public static void main(String args[])
{
	// runtime exception and unchecked exception
	
	 System.out.println("Runtime EXception and Unchecked Exception:"); 
		
		try {	int num1=10;
			int num2=0;
			int res=num1/num2;
			System.out.println(res);
		}
		catch(ArithmeticException e)
		{
			System.out.println("Runtime and unchecked exception occured");
		}
	  //Checked Exception
	 System.out.println("Checked EXception:");
	 FileInputStream fis = null;
		try{
		    fis = new FileInputStream("C:/myfile.txt"); 
		}catch(FileNotFoundException fnfe){
	            System.out.println("The specified file is not " +
				"present at the given path");
		 }
		int k; 
		try{
		    while(( k = fis.read() ) != -1) 
		    { 
			System.out.print((char)k); 
		    } 
		    fis.close(); 
		}catch(IOException ioe){
		    System.out.println("I/O error occurred: "+ioe);
		 }
		
}
}






