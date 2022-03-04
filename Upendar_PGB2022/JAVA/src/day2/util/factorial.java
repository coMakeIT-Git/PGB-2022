package day2.util;

public class factorial {
	
	// Factorial with Recursion
    static int with_recursion(int n){    
        if (n == 0)    
        	return 1;    
        else    
        	return(n * with_recursion(n-1));    
        }
    
    // Factorial without Recursion
    static int without_recursion(int n){
        int i, fact = 1;
        if (n == 0)    
        	return 1;    
        else{
            for(i=1;i<=n;i++){    
                fact=fact*i;    
            } 
        }
        return fact;
    }
    
    public static void main(String []args) {
    	System.out.println("Factorial with recursion : "+factorial.with_recursion(5));
    	System.out.println("Factorial without recursion : "+factorial.without_recursion(5));
    }
}
