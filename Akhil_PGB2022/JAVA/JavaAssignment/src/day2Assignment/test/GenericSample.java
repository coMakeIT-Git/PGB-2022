package day2Assignment.test;

public class GenericSample<T>{
	private T data;
	
	GenericSample(T x){
		this.data = x;
	}
	
	public void display() {
		System.out.println(this.data);
	}
	
	public static void main(String[] args) {
		
		GenericSample<Integer> integer = new GenericSample<Integer>(344);
		GenericSample<String> str = new GenericSample<String>("This is a string");
		GenericSample<Boolean> bool = new GenericSample<Boolean>(true);
		GenericSample<Double> dble = new GenericSample<Double>(234.545);
		System.out.println("Displaying different types using Generic Class");
		integer.display();
		str.display();
		bool.display();
		dble.display();
	}
}