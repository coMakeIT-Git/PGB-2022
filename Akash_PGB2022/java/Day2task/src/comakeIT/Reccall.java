package comakeIT;

public class Reccall {
	public static void main(String[] args) {
		SumFact sf=new SumFact ();
		System.out.println("recursive fact: "+sf.rfact(8));
		System.out.println("irrecursive fact: "+sf.irrfact(5));
	}

}
