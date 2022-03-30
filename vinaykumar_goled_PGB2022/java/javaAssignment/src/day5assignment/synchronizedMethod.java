package day5assignment;
class A{
	synchronized public void getLine() {
		for(int i = 0; i < 5; i++) {
			System.out.println(i);
			try {
				Thread.sleep(400);
			}
			catch(Exception e) {
				System.out.println(e);
			}
		}
	}
}
class B extends Thread{
	A a;
	B(A a){
		this.a = a;
	}
	public void run() {
		a.getLine();
	}
}
public class synchronizedMethod {
	public static void main(String[] args) {
		A obj1 = new A();
		B obj2 = new B(obj1);
		B obj3 = new B(obj1);
		obj2.start();
		obj3.start();
	}
}
