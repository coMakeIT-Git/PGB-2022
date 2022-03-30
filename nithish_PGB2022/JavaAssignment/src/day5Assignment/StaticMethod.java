package day5Assignment;


interface PrintStatic{
	void print();
}
public class StaticMethod {
	public static void message() {
		System.out.println("static method");
	}
	public static void main(String[] args) {
		PrintStatic obj=StaticMethod::message;
		obj.print();
	}
}
