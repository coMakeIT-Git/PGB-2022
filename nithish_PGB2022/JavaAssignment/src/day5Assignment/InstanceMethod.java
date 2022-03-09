package day5Assignment;

interface PrintInstance{
	void print();
}
public class InstanceMethod {
	public void message() {
		System.out.println("instance method/non-static method");
	}
	public static void main(String[] args) {
		InstanceMethod methodReference=new InstanceMethod();
		//creating obj
		PrintInstance obj=methodReference::message;
		obj.print();
		
		//anonymous obj
		PrintInstance obj1=new InstanceMethod()::message;
		obj1.print();
	}
}
