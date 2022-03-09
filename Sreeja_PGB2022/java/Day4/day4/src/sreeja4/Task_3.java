package sreeja4;

import java.io.FileInputStream;
import java.io.IOException;

public class Task_3 {
	public static void main(String args[]) throws IOException
	   {
		try{  
		      //code that may raise exception  
		      int data=100/0;  
		   }catch(ArithmeticException e)
		 {
			   System.out.println(e);
			   }  
		   //rest code of the program   
		   
	      FileInputStream fis = null;
	      fis = new FileInputStream("B:/myfile.txt"); 
	      int k; 

	      while(( k = fis.read() ) != -1) 
	      { 
		   System.out.print((char)k); 
	      } 
	      fis.close(); 
	      
	     
	      
	   }

}
