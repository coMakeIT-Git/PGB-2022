package comakeit;

import java.io.FileNotFoundException;

public class uncheck {
	public static void Check() throws Exception{
		throw new FileNotFoundException("Checked Exception");
	}
	
	public static void Uncheck() throws Exception{
		int[] arr = new int[6];
		System.out.println(arr[9]);
	}
	
	public static void main(String[] args){
		try{
			Check();
		}catch(Exception e) {
			System.out.println(e.getMessage());
		}
		try{
			Uncheck();
		}catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}
	
}