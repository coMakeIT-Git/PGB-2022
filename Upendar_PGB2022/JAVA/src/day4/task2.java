package day4;
import java.util.*;
import java.util.function.Consumer;
class Exception2 extends Exception  
{  
   public static void main(String[]args) {
	   System.out.println("custom exception");
   }
}  
public class task2
	{
	static ArrayList<Integer> numbers = new ArrayList<Integer>();

	public static void main(String[]args) 
	{
	Scanner sc = new Scanner(System.in);
	String ptr = null;
	try
	{
		if (ptr.equals("console"))
		{
			System.out.print("Same");
		}
		else {
			System.out.print("Not Same");
		}
	}
	catch(NullPointerException e)
	{
		System.out.print("NullPointerException Caught");
	}
	while (true) 
		{
        System.out.println("Enter any valid Integer: ");
       
        try {
            int number = Integer.parseInt(sc.next());
            System.out.println("You entered: "+number);
            break;
        }
        catch (NumberFormatException e) {
            System.out.println("NumberFormatException occurred");
        }
    }   
		 try  
	        {  
	            throw new Exception2();  
	        }  
	        catch (Exception2 ex)  
	        {  
	            System.out.println("Caught the exception");   
	        }    
    numbers.add(3);
    numbers.add(9);
    numbers.add(8);
    numbers.add(1);
    Consumer<Integer> method = (n) -> { System.out.println(n); };
    numbers.forEach( method );
    
    new Thread(() -> {
        System.out.println("New thread created");
    }).start();
	}
}
