package sreeja4;

interface FunctionalInterface {
	   void display();
	} 

public class Task_4 {
	 public static void main(String args[]) {
	      // Using Anonymous inner class
		 FunctionalInterface test1 = new FunctionalInterface() {
	         public void display() {
	            System.out.println("Display using Anonymous inner class");
	         }
	      };
	      test1.display();
	      // Using Lambda Expression
	      FunctionalInterface test2 = () -> {    
	         System.out.println("Display using Lambda Expression");
	      };
	      test2.display();
	   }

}
