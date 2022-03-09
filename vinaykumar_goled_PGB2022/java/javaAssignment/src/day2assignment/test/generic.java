package day2assignment.test;

public class generic <T> {
	T value;
	generic(T value){
		this.value = value;
	}
	public T display() {
		return (this.value);
	}
	public static void main(String[] args) {
		generic<Integer>obj1 = new generic<>(123);
		generic<Boolean>obj2 = new generic<>(true);
		generic<Double>obj3 = new generic<>(76.8654);
		generic<String>obj4 = new generic<>("Harish");
		System.out.println(obj1.display());
		System.out.println(obj2.display());
		System.out.println(obj3.display());
		System.out.println(obj4.display());
	}
}
