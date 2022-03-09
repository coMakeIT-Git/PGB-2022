package comakeit;

public class Calculate {
	
	public static int recfact(int a) {
		if(a==0)
			return 1;
		else
			return(a*recfact(a-1));
	}
	
	public static int irrecfact(int a) {
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
		Calculate c1=new Calculate();
		System.out.println("recursive factorial: "+c1.recfact(3));
		System.out.println("with out recursive factorial: "+c1.irrecfact(4));
	}
	
}
