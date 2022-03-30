package day4assignment;

public class RuntimeException {
	
	private static void simpleNullCheck(String str1) {
		System.out.println(str1.length());
	}
	public static void main(String args[]) {
	    String input1 = null;
	    simpleNullCheck(input1);
	}
}
