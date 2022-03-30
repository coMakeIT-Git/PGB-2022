package sreeja4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
class UserException extends Exception{
int num1=0;
UserException(int value) {
num1=value;
}
public String toString(){
return ("sum is "+ num1+" user defined exception") ;
}
}

public class Employe4 {
	public static void main(String[] args)
	    {
		String x = "123.33";  
		int sum=0,z=0;	              
		Scanner sc = new Scanner(System.in);
		 
        String s = sc.nextLine();
        System.out.println("You entered string " + s);
        char[] sarr = s.toCharArray();
        for (int i = 0; i < sarr.length; i++) {


            if(sarr[i]/1>=48 && sarr[i]/1<=57){

            		System.out.print(sarr[i]+" ");
            		sum=sum+(sarr[i]);
            		sum=sum-48; 
            }
            
        }
        System.out.println("");
        System.out.println("sum is "+ sum); 
        try {  
            int a = Integer.parseInt(x);  
   }catch(NumberFormatException ex){  
       System.err.println("Invalid string in argument");  
      
   }  
       
        
        String ptr = null;
        try
        {
            
            if (ptr.equals("gfg"))
                System.out.print("Same");
            else
                System.out.print("Not Same");
        }
        catch(NullPointerException e)
        {
            System.out.println("Null Pointer Exception Caught");
        }
        try{
        	throw new UserException(sum);
        	}
        	catch(UserException e){
        	System.out.println(e) ;
        	}
        
	
	    }

}
