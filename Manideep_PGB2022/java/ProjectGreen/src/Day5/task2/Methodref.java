package Day5.task2;
import java.util.*;
import Day5.task2.Doable;
public class Methodref {
	 public static void dosomething(){  
	        System.out.println("Hello, this is my method.");  
	    }  
	    public static void main(String[] args) {  
	        // Referring static method   
	        Doable d = Methodref::dosomething;  
	        // Calling interface method  
	        d.doo();  
	    }  

}
