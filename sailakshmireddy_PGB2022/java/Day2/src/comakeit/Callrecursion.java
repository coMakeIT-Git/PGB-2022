package comakeit;

public class Callrecursion {
	public static void main(String[] args) {
		Calculate c1=new Calculate();
		System.out.println("call recursive factorial: "+c1.recfact(5));
		System.out.println("call with out recursive factorial: "+c1.irrecfact(6));
	}

}
