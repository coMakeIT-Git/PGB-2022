package Day4.Task2;

public class runtimeExceptions {
public static void main(String args[]){
		
		try {
			int k=10/0;
		}
		catch(ArithmeticException e)
		{
			System.out.println("Dividing number By zero is not possible ");
		}
		finally
		{
			System.out.println("Iam always executed");
		}
	}
}
