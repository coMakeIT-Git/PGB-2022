package sreeja4;

public class Task_2 {
	public static void main(String[] args)
	{
		 
		   try

		  {
		  int array[] = { 6, 16, 26,36,46,56,66,76 };
		  
		  System.out.println(array[9]);  

		  }

		   catch( ArrayIndexOutOfBoundsException e ) 

		  { 
		   System.out.println( "Runtime Exception caught:Valid indexes are 0, 1,2,3, 4,5,6 or 7" );

		  }	   
	 try{  
	      //code that may raise exception  
	      int data=100/0;  
	   }catch(ArithmeticException e)
	 {
		   System.out.println(e);
		   }  
	   //rest code of the program   
	   System.out.println("rest of the code...");  
	  } 

}
