package comakeIT;

public class SumFact {

	public static int rfact(int a) {
		if(a==0)
			return 1;
		else
			return(a*rfact(a-1));
	}
	
	public static int irrfact(int a) {
		int i , fact=1;
		if(a==0)
			return 1;
		else {
			for(i=1;i<=a;i++) {
				fact=fact*i;
			}
		}
		return fact;
	}
	
	public static void main(String[] args) {
		SumFact sf=new SumFact ();
		System.out.println("recursive fact: "+sf.rfact(9));
		System.out.println("irrecursive fact: "+sf.irrfact(5));
	}
}
