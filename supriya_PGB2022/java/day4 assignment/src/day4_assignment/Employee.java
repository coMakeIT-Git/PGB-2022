package day4_assignment;
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
import java.util.Scanner;
class SrException extends Exception{
	public SrException (String str)  
    {  
         
        super(str);  
    }  
}  


public class Employee {
	static String name = null;
	// method to check the experience 
    static void validate (int yrsworked) throws SrException{    
       if(yrsworked < 5){  
  
        // throw an object of user defined exception  
        throw new SrException("\nLess years of experience");    
    }  
       else {   
        System.out.println("\nHas experience of minimum years");   
        } 
    }
	public int add(int emp1, int emp2) {
     
		return (emp1+emp2);

	}

	public static void main(String args[]) throws Exception {

		Scanner sc = new Scanner(System.in);
		// Read user input
		System.out.println("Enter emp1 & emp2:");
		int emp1  = sc.nextInt();
		//System.out.println("Enter emp2:");
		int emp2 = sc.nextInt();
		System.out.println("Emp1 & Emp2 is: " + emp1+" "+emp2);
		//System.out.println("Emp2 is: " + emp2);
		System.out.println("Sum of integers is:" + (emp1+emp2));
		sc.nextLine();
		System.out.println("Enter name:");
		String nme = sc.nextLine();
           // NullPointerException
		try {

			System.out.println(name.equals(nme));

		} catch (NullPointerException e) {
			System.out.print("NullPointerException");
		}
		//CustomException
		try  
        {  
             
            validate(7);  
           
        }  
        catch (SrException ex)  
        {  
            System.out.println("Caught the exception");  
    
           
           System.out.println("Exception occured: " + ex);  
        }  
  
        System.out.println("rest of the code...");    
     
		//RuntimeException
        try{
            int num1=30, num2=0;
            int output=num1/num2;
            System.out.println ("Result: "+output);
         }
         catch(ArithmeticException e){
            System.out.println ("You Shouldn't divide a number by zero");
         }
      //CheckedException
      		try {
      			Class test = Class.forName("abc"); 
      		} catch (ClassNotFoundException e) {
      			// block executes when mention exception occur
      			System.out.println("ClassNotFoundException occured");
      		}
		
		//NumberFormat Exception
		//System.out.println("\nEnter emp:");
		//int emp=sc.nextInt();
		while(true) {
			System.out.println("\nEnter any valid Integer: ");
			 try {
				  int emp = Integer.parseInt(sc.nextLine());
              
              System.out.println("You entered: "+ emp);
              break;
            }
                catch (NumberFormatException e) {
			 System.out.print("NumberFormatException occurred");
            }
			 
		}
			}
}
	    
	

