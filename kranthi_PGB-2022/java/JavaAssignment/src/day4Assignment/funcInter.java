package day4Assignment;


	import java.util.*;
	
	
	interface Sayable{  
	    public double say(int a,int b);  
	}  
	
	
	public class funcInter{  
		
		
	public static void main(String[] args) {  
		
		
	    Sayable s=(a,b)->{  
	        return (Math.pow(a, b));  
	    };  
	    
	    System.out.println(s.say(2,5));  
	    new Thread(()->System.out.println("This is the lambda for Runnable ")).start();
	    
	}  
	}  


