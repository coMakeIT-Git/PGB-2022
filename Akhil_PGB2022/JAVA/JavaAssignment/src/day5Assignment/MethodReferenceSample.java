package day5Assignment;

interface Sayable{
	void say();
}
class Test{
	Test(){
		System.out.println("Constructor reference");
	}
	public void display() {
		System.out.println("Instance Method Reference");
	}
}
public class MethodReferenceSample {
	public static void print() {
		System.out.println("Static Method Reference");
	}
	public static void main(String[] args) {
		//instance method reference
		Sayable t = new Test()::display;
		//static method reference
		Sayable s = MethodReferenceSample::print;
		//Constructor reference
		Sayable c = Test::new;
	}
}
