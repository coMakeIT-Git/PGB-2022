class Recursion{
	public static int factorial(int num) {
		if(num==1 || num==0)
			return 1;
		else
			return num * factorial(num-1);	
	}
	
	public static void multiples(int num) {
		System.out.println("\n**Multiples of " + num + "**");
		for(int i=1;i<=10;i++) {
			System.out.println(num + " X " + i + " = " + num*i);
		}
	}
	
	public static void main(String args[]) {
		System.out.println("**Factorial of 8**\n" + Recursion.factorial(8));
		Recursion.multiples(10);
	}
}

