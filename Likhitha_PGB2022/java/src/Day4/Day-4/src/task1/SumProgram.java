package task1;
import java.util.*;


public class SumProgram {
   
	public static void main(String[] args)
	   {
		   Scanner s= new Scanner(System.in);
		   System.out.println("Enter the text");
		   
		   try {
		   String str=s.next();
		   
		   ArrayList<Integer> list =new ArrayList<Integer>();
		   
		   int i,j,k,l=0;
		   char ch;
		   for(i=0;i<str.length();i++)
		   {
			   ch=str.charAt(i);
			   if(Character.isDigit(ch))
			   {
				   k=Character.getNumericValue(ch);
				   list.add(k);
				   l+=k;
			   }
		   }
		   
		   for(int num : list)
		   {
		   System.out.println(num);
		   }
		   
		   System.out.println("Addition of integers in text:");
		   
		   System.out.println(l);
		   
		   s.close();
		   }
		   catch (NumberFormatException e)
		   {
			   System.out.println("Numberformat exception occurred");
		   }
		   
		   
	}
}
