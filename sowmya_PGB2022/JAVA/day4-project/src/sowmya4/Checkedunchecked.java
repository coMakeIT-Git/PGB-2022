package sowmya4;

import java.io.*;
import java.util.*;
 
public class Checkedunchecked {
	public static void main(String[] args){
    try {  
    	
        try {
        int a = 30, b = 0;
        int c = a/b;  // cannot divide by zero
        System.out.println ("Result = " + c);
        
        }
        catch(ArithmeticException e1) {
            System.out.println ("Unchecked Exceptuion caught:Can't divide a number by 0");
        }

        FileInputStream  GFG = new FileInputStream(
            "/home/mayur/GFG.txt"); 
    }

    // Catch block to handle exceptions
    catch (FileNotFoundException e) {

        // Display message when exception occurs
        System.out.println("Checked Exception caught:File does not exist");
    }
    
	  }
}
    
