import java.util.*;

//Custom Exception
class EmptyStringException extends Exception{
	public EmptyStringException(String s) {
		super(s);
	}
}

class ConsoleIO{
	
	//NumberFormatException
	public static boolean isNumber(char c) {
		try {
			int n = Integer.parseInt(String.valueOf(c));
			return true;
		}
		catch(NumberFormatException e) {
			return false;
		}
	}
	
	 public void printSum() throws EmptyStringException{
		int sum = 0;
		Scanner s = new Scanner(System.in);
		
		//Custom Exception
		try {			
			System.out.print("Enter a string: ");
			String str = s.nextLine();
			if(str.isEmpty())
				throw new EmptyStringException("Error");			
			//Print Numbers and their Sum
			System.out.println("\nInput: " + str);					
			System.out.print("\nIntegers in input : ");
			for(int i=0; i<str.length(); i++) {
				char c = str.charAt(i);
				if(isNumber(c)) {
					System.out.print(c + "\t");
					sum += Integer.parseInt(String.valueOf(c));
				}
			}
			System.out.println("\n\nSum of Integers: " + sum);
			//Propagation to main
			System.out.println("Dividing the sum by 0...");
			int d = sum/0;
		}
		catch(EmptyStringException e) {
			System.out.println("Error: String cannot be empty!");
		}				
	}
	 
	 public static void main(String args[]) throws Exception{
		 ConsoleIO c = new ConsoleIO();
		 //handling the propagated Exception
		 try {
			 c.printSum();
		 }
		 //Runtime Exception handling
		 catch(ArithmeticException e) {
			 System.out.println("Error: Division by 0 is undefined!");
		 }
	 }
}