package Task2;

public class factorialre {
	// factorial with recursion
    static int with_recursion(int n){    
        if (n == 0)    
        	return 1;    
        else    
        	return(n * with_recursion(n-1));    
        }

    // factorial without recursion
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
    	System.out.println("Factorial with recursion : "+factorialre.with_recursion(8));
    	System.out.println("Factorial without recursion : "+factorialre.without_recursion(8));
}
}
