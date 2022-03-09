package task2;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class runtime {
	public static void main(String args[]) throws IOException
	{
		//Runtime Exception(Unchecked Exception)
	try {
		int id4=100,id5=0;
		System.out.println(id4/id5);
	}
	catch(ArithmeticException e)
	{
		System.out.println("Arithemetic exception(Runtime and unchecked Exception) occured");
	}
	
	//checked Exception
	try {
		FileReader file = new FileReader("C:\\test\\a.txt");
		  
	    
	    BufferedReader fileInput = new BufferedReader(file);

	    
	    for (int counter = 0; counter < 3; counter++)
	        System.out.println(fileInput.readLine());

	    fileInput.close();

	}
	catch(FileNotFoundException e)
	{
		System.out.println("FileNotFound Exception(Checked Exception) occured");
	}
	
	
	}
}
