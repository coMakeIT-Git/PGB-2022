package Day4Assignment;
import java.util.*;
import Day3Assignment.*;
public class ExceptionSample extends Exception{
	ExceptionSample(String s)
	 {
		 super(s);
	 }
 public static void main(String args[]) throws ArithmeticException
 {
	 
	 int sum=0;
	 Scanner input=new Scanner(System.in);
	 String str=null;
	 try
	 {
		 //Null Pointer Exception
		 if(str==null) throw new NullPointerException();
	 }
	 catch(NullPointerException e)
	 {
		e.printStackTrace();
	 }
	 try
	  {
	   //Taking Input in single line and separated by space	 
	   String marks[]=input.nextLine().split(" ");
	   int len=marks.length;
	   for(int i=0;i<len;i++)
	   {
		  sum+=Integer.parseInt(marks[i]);
	   }
	   System.out.println("Sum of marks of students is:"+sum);
	   //Run time Exception
	   for(int i=0;i<=len;i++)
		 {
			 System.out.println(marks[i]);
		 }
	 }
	 catch(ArrayIndexOutOfBoundsException e)
	 {
		 e.printStackTrace();
	 }
	 //Number Format Exception
	 catch(NumberFormatException e)
	 {
		 System.out.println("Exception Caught..."+e.getMessage());
	 }
	 //Custom Exception
	 try
	 {
		 if(sum<50) throw new ExceptionSample("Sum is less than 50");
	 }
	 catch(ExceptionSample e)
	 {
		 System.out.println(e.getMessage());
     }
	 //Runtime Exception
	 int number=input.nextInt();
	 System.out.println(number/0);
	
}

	
}

