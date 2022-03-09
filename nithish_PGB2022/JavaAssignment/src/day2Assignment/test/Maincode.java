package day2Assignment.test;
import day2Assignment.util.Fact;
public class Maincode{
	public static void main(String[] args) {
		Student stu1=new Student(1,"nithish",98);
		Student stu2=new Student(2,"akhil",89);
		
		System.out.println("comparing two objects :"+stu1.equals(stu2));
		
		stu1.overload(5,"nithish");
		stu1.overload(6,"kranthi",89);
		
		System.out.println();
		System.out.println("factorial using recursion: "+Fact.factorialrecursion(6));
		System.out.println("factorial without recursion: "+Fact.factorial(5));
		
	}
}