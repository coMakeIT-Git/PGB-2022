package day2;

class g<t>{
	t data;
	void set(t d){
		this.data=d;
	}
	t get(){
		return data;
	}
}
public class Generic{
	public static void main(String[]args) {
		g <Integer>a=new g();
		g <String> b=new g();
		a.set(1);
		b.set("a");
		System.out.println(a.get()+" "+b.get());
	}
}