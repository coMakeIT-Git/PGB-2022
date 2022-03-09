package Day4.Task1;

import java.util.Scanner;

class myException extends Exception
{
	public myException(String s)
	{
		super(s);
	}
}
public class task1 {
		public static void main(String args[]) throws myException {
			Scanner sc= new Scanner(System.in); //System.in is a standard input stream  
			System.out.print("Enter a Positive Numbers seperated by Space: ");
			int c=0;
			try {
				String s= sc.nextLine();              //reads string  
				System.out.println("You have entered: "+s);
				String k[]=s.split(" ");
				
				for(int i=0;i<k.length;i++)
				{
					int k1=Integer.parseInt(k[i]);
					if(k1<0)
						throw new myException("Number is Negative");
					c+=k1;
				}
				System.out.println(" Sum of Numbers  is "+c);
			}
			catch(NumberFormatException e)
			{
				System.out.println(c+"\n"+"NumberFormat Exception");
			}
			catch(NullPointerException e1)
			{
				System.out.print("Null Pointer Exception");;
			}
			
			
		}
}
