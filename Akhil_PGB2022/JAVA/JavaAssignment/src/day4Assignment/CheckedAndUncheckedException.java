package day4Assignment;

import java.io.FileNotFoundException;

public class CheckedAndUncheckedException {
	public static void Checked() throws Exception{
		throw new FileNotFoundException("Checked Exception");
	}
	
	public static void Unchecked() throws Exception{
		int[] arr = new int[4];
		System.out.println(arr[6]);
	}
	
	public static void main(String[] args){
		try{
			Checked();
		}catch(Exception e) {
			e.printStackTrace();
		}
		try{
			Unchecked();
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
}
