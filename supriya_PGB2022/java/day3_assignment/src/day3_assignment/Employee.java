package day3_assignment;
import java.util.*;
import java.util.ArrayList;

//This is an interface.
interface Employee {
 void worktime(String entry, String exit);
	void debugger();
	void developer();
	void tester();
}
//This is an abstract class.
abstract class Manager implements Employee{
	public void developer() {
		System.out.println("Developer writes the code");
	}
   public void tester() {
		System.out.println("Tester finds the error");
	}
   public void debugger() {
		System.out.println("Degubber");
  
   }
}



// This is an concrete class
class Main extends Manager{
	
	public void worktime(String entry, String exit) {
		System.out.println("Work hours "+entry+" - "+ exit);
	}
	@Override public void debugger() {
		System.out.println("Degubber finds the bugs");
	}

//main method
	public static void main(String[] args) {
	Main obj =new Main();
	obj.developer();
	obj.tester();
	obj.debugger();
	obj.worktime("9:30","6:30" );
}
}