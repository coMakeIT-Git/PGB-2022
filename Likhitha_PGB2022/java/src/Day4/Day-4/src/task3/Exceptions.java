package task3;
import java.util.*;
import java.io.*;

public class Exceptions {
	public static void main(String args[])
	   {
		FileInputStream fis = null;
		
		//Checked Exception
		try{
		    fis = new FileInputStream("B:/myfile.txt"); 
		}
		catch(FileNotFoundException fnfe){
	            System.out.println("The specified file is not present at the given path");
		 }
		int k; 
		try{
		    while(( k = fis.read() ) != -1) 
		    { 
			System.out.print((char)k); 
		    } 
		    fis.close(); 
		}
		catch(IOException ioe){
		    System.out.println("I/O error occurred: "+ioe);
		 }
		
		//Unchecked Exception
		try {
			int arr[] = {1,2,3,4,5};
			System.out.println(arr[7]);
		
		}
		catch(ArrayIndexOutOfBoundsException e)
		{
			System.out.println("Specified index is not found");
		}
	   }
}
