package day2.util;

public class Main {
    static int factorial(int num){    
        if (num == 0)    
        	return 1;    
        else    
        	return(num * factorial(num-1));    
        }
    
    static int square(int num){
        int i, fact = 1;
       fact=num*num;
        return fact;
    }
    
    public static void main(String []args) {
    	System.out.println("Factorial "+Main.factorial(5));
    	System.out.println("square : "+Main.square(5));
    }
}
