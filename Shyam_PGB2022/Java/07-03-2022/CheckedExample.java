import java.io.*;
class CheckedExample{  
   public static void main(String args[]) throws IOException
   {
      FileInputStream fis = null;
      fis = new FileInputStream("Read.txt"); 
      int k; 

      while(( k = fis.read() ) != -1) 
      { 
	   System.out.print((char)k); 
      } 
      fis.close(); 	
   }
}
