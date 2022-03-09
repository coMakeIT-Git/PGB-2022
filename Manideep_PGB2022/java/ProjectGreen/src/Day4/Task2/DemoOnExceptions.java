package Day4.Task2;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
public class DemoOnExceptions {
public static void main(String args[]) {
		
		try {
			FileReader fr = new FileReader("C:\\Users\\Manideep\\Desktop\\test.txt");
		        int i;
		        while ((i = fr.read()) != -1)
		            System.out.print((char)i);
			int a[]=new int[2];
			System.out.println(a[2]);
			int b=10/0;
		}
		catch(IOException e)		{
			System.out.println("Checked Exception: Io Exception");
		}
		catch(ArithmeticException e)
		{
			System.out.println("UnChecked Exception:Runtime Exception");
		}
		catch(ArrayIndexOutOfBoundsException e)
		{
			System.out.println("UnChecked Exception: Runtime Exception");
		}
		
		finally
		{
			System.out.println("Iam always executed");
		}
	}
}
