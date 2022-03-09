package day4Assignment;

import java.io.FileNotFoundException;

public class CheckedUnchecked {
	
	public static void checked() throws Exception{
		throw new FileNotFoundException("Checked Exception");
	}
	public static void unchecked() {
		int[] a=new int[4];
		System.out.println(a[6]);
	}
	
	public static void main(String[] args) {
		try {
			checked();
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		try {
			unchecked();
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}

}
