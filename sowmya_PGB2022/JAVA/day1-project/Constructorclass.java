package util;
import java.util.*;
class Newconstructor{
	String studentname;
	int studentage;
	 public Newconstructor(){
	 System.out.println("constructor");
	 }
	 public Newconstructor(String name,int age) {
		 studentname=name;
		 studentage=age;
	 }
	 void display() {
		 System.out.println(studentname+ "\n"+studentage);
	 }
}
public class Constructorclass{
	 public static void main(String args[]) {
		 Newconstructor obj=new Newconstructor();
		 Newconstructor obj1=new Newconstructor("sowmya",56);
		 obj1.display();
	}

}

