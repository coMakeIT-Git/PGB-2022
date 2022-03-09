package day4_assignment;

interface FuncInterface {
	void print();
}
public class Main {
   public static void main(String args[]) {
      
      FuncInterface t1 = new FuncInterface() {
         public void print() {
            System.out.println("Print without lambda");
         }
      };
      t1.print();
      // Using Lambda Expression
      FuncInterface t2 = () -> { 
         System.out.println("Print using Lambda Expression");
      };
      t2.print();
}
   }