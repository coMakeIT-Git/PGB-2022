import java.io.Console;
import java.util.*;
import java.util.regex.Matcher; 
import java.util.regex.Pattern;
interface customLambda
{  
       double power(int p,int g);  
}
class ExceptionDemo
{
public static boolean isNumber(char c)
	{
	try 
		{
		int n=Integer.parseInt(String.valueOf(c));
		return true;
		}
	// NumberFormatException
	catch(NumberFormatException e)
		{
		//System.out.println("Number format Exception Handled!");
		return false;
		}
	}
   static String extractInt(String str)
    {
        str = str.replaceAll("[^\\d]", " ");
        str = str.trim();
        str = str.replaceAll(" +", " ");
        if (str.equals(""))
            return "-1";
        System.out.println("The integers are"+"\t");
        return str; 
    }
}
// user defined exception
class InputFormatException extends Exception  
{  
	   public InputFormatException(String s)
	    {
	        // Call constructor of parent Exception
	        super(s);
	    }  
}
// exception propagation
class excepPropagation
{
	Scanner s1= new Scanner(System.in);
    void input()
    {
        System.out.println("Enter a number for testing propagation:");
    	int m1=s1.nextInt();
    	int r = m1/0; 
        // unchecked exception occurred
 
    }
  
    void inputPass()
    {
        input();
     
    }
  
    void Handler()
    {
        try 
        {
            inputPass();
            // exception handled
        }
        catch (Exception e)
        {
            System.out.println("Arithematic Exception is handled:"+e);
        }
    }
}
class JavaExceptions extends ExceptionDemo
{
public static void main(String[] args)
	{
	// taking input from console
	try 
	{
		String str = args[0];
		System.out.println(extractInt(str));
	}
	catch(ArrayIndexOutOfBoundsException e)
	{
		System.out.println("Argument is missing, Enter a string {args[0]}");
		System.exit(0);
		
	}
	String str2="";
	System.out.println("Enter your name: ");  
	//console 
	Console c=System.console();  
	String n=c.readLine();    
	System.out.println("Welcome "+n);   
	
	// taking input using scanner class
	int sum=0;
	Scanner s= new Scanner(System.in);
		try 
		{
	    System.out.println("Enter a String:");
        String str1 = s.nextLine();
        if(str1.isEmpty())
        {
    	str1=null;
    	// null pointer exception
    	throw new NullPointerException("nullpointerexception");
        } 
	        try 
	        {
	          
	        	String regex = "^[a-zA-Z0-9]+$";
	        	Pattern pattern = Pattern.compile(regex);
	            Matcher matcher = pattern.matcher(str1);	           
	            boolean res = matcher.matches();
	            //System.out.println(res);
	            if(!res)
	            {
	            	throw new InputFormatException("Custom Exception Handled:\t"+ "Input string::"+str1+"\tshouldn't contain special characters!!\t");
	            
	            }
	            
	        }
	        catch(InputFormatException ex)
	        {
	            //System.out.println("Caught");
	            System.out.println(ex.getMessage());
	            System.out.println("Enter a string without any special characters:");
	            str2 = s.nextLine();   
	    	}
		        System.out.println("The newly Entered String is:"+"\t"+str2);
		        System.out.println("The Integers present in the newly string are"+"\t");
	        for( int i=0;i<str2.length();i++)
	        {
	        	char ch= str2.charAt(i);
	        	if(isNumber(ch))
		        	{
		        	System.out.println(ch);
		        	sum=sum+Integer.parseInt(String.valueOf(ch));
		        	}
	        }
	        		System.out.println("The sum of integers is:"+sum);
			}
// catching NullPointerException
catch(NullPointerException e)
		{
		System.out.println("Null Pointer Exception Handled!");
		System.out.println("Feild is empty, Enter a string!");
		System.exit(0);		}
		 if(args.length > 0)
         {
             try
               {
                    String firstNum = args[1];
                    int q = Integer.parseInt(extractInt(firstNum));
                    String secNum = args[2];
                    int xyz =secNum.length();
                    int u = Integer.parseInt(extractInt(secNum));
                    int t= q+u;            
                    System.out.println("First Number = "+q);
                    System.out.println("Second Number = "+u);
                    System.out.println("Sum of the Two Numbers is = "+t);
                }
             catch(NumberFormatException e)
               {
                   System.out.println("Number format Exception Handled: Arguments must be the integers.");
               }
             catch(NullPointerException e1)
             {
            	 System.out.println("abc****");
             }
    	excepPropagation exp= new excepPropagation();
    	exp.Handler();
        System.out.println("Back to Normal flow");
        customLambda cl=(p,g)->(Math.pow(p,g));  
    	System.out.println("Lambda without datatypes: " +cl.power(2,4));  
    	customLambda cl1=(int p,int g)->(Math.pow(p,g));  
    	System.out.println("Lambda without datatypes: " +cl1.power(2,8));
    	new Thread(()->System.out.println( "Lambda for Runnable")).start(); 
        
        }
	}
}
