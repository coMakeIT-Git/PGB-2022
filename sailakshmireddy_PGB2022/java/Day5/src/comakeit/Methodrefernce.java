package comakeit;

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
public class Methodrefernce {
	//Reference to a Instance Method
	public void insta() {
		System.out.println("I am from instance method");
	}
	
	//Reference To a static Method
	public static void stac() {
		System.out.println("I am from static");
	}
	
	public static void main(String[] args) {
		Methodrefernce mr= new Methodrefernce();
		cons c=constr::new;
		c.message("I am from constructor");
		Stack s= mr::insta;
		Stack s1 = Methodrefernce::stac;
		s.show();
		s1.show();
	}
	
	
}
