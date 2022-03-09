package day4;
import java.io.*;
public class CheckedvsUnChecked{
	public static void Checked() throws Exception{
		throw new FileNotFoundException("Checked Exception");
	}
	
	public static void Unchecked() throws Exception{
		int[] arr = new int[4];
		System.out.println(arr[6]);
	}
	
	public static void main(String[] args){
		System.out.println("Hello");
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