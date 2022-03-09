package day5;
import java.util.*;
class n{
	n(int input){
		System.out.println("Number Tripled"+(3*input));
	}
	public void func(Integer input){
		System.out.println("Number doubled"+(2*input));
	}
}

public class MethodReference{
	static int ans=0;
	static void func(int n){
		ans+=n;
	}
	public static void main(String[] args) {
		List<Integer>l=new ArrayList();
		l.add(1);
		l.add(2);
		l.add(3);
		n a=new n(1);
		//static method reference[1,2,3]
		l.forEach(MethodReference::func);
		//instance method reference
		l.forEach(a::func);
		//constructor method reference
		l.forEach(n::new);
		System.out.println(ans);
	}
}