package day4assignment;

public class CustomFunctionalInterfaceLambda{
	public static void main(String args[]) {	
		CustomFunctionalInterface test1 = new CustomFunctionalInterface() {
			public void display() {
				System.out.println("Display using Anonymous inner class");
			}
	    };
	    test1.display();
		CustomFunctionalInterface test2 = () -> {    // lambda expression
			System.out.println("Display using Lambda Expression");
	     };
	     test2.display();
   }
}
