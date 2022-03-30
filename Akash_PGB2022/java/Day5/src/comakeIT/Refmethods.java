package comakeIT;

interface Stack{
	void show();
}

interface cons{
	constr message(String msg);
}

//Reference to a constructor
class constr{
	String msg;

	public constr(String msg) {
		System.out.println(msg);
	}
	
}
public class Refmethods {
	//Reference to a Instance Method
	public void insta() {
		System.out.println("I am from instance method");
	}
	
	//Reference To a static Method
	public static void stac() {
		System.out.println("I am from static");
	}
	
	public static void main(String[] args) {
		Refmethods rm= new Refmethods();
		cons c=constr::new;
		c.message("I am from constructor");
		Stack s= rm::insta;
		Stack s1 = Refmethods::stac;
		s.show();
		s1.show();
	}
	
	
}

