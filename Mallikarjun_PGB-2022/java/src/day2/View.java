package day2;

public class View<T> {
	private T d;
	public void addData(T d) {
		this.d = d;
	}
	public T getData() {
		return d;
	}
	public static void main(String[] args) {
		View<Integer> integer = new View<Integer>();
		View<String> String = new View<String>();
		
		integer.addData(10);
		String.addData("This is a String");
		
		System.out.println(integer.getData());
		System.out.println(String.getData());
	}

}
