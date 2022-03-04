package day2;

public class recursive<T> {
	private T d;
	public void addData(T d) {
		this.d=d;
		
	}
	public T getData() {
		return d;
	}
	public static void main(String[]args) {
		recursive<Integer> integer =new recursive<Integer>();
		recursive<String> string =new recursive<String>();
		integer.addData(10);
		string.addData("this is string");
		System.out.println(integer.getData());
		System.out.println(string.getData());
	}

}
