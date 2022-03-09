package coMakeit;
import java.io.FileNotFoundException;

public class Handledexcep {
		public static void Check() throws Exception{
			throw new FileNotFoundException("Exception is Checked");
		}
		
		public static void Uncheck() throws Exception{
			int[] arr = new int[9];
			System.out.println(arr[12]);
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
