package Day4Assignment;

import javax.naming.NameNotFoundException;

public class Exceptions {
	//checked exception
		public static void Checked() throws Exception{
				throw new NameNotFoundException();
			}
	//unchecked Exception		
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
	   
	   try
	   {
		   Unchecked();
	   }
	   catch(Exception e)
	   {
		   e.printStackTrace();
	   }
	   }
}
