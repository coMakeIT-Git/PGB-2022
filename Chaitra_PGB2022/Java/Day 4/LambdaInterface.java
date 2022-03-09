import java.util.*;

@FunctionalInterface 
interface Wave {
    void wave(String Name);
}

class  LambdaInterface {
    public static void main(String args[])
    {
    	Scanner s = new Scanner(System.in);
    	System.out.print("Enter name: ");
    	String name = s.nextLine();
    	
        // lambda expression
        Wave w = (String n) -> {System.out.println("Hello " + n + "!"); };
        w.wave(name);
        
        //In-built Functional Interface: Runnable
        new Thread(()->System.out.println("\n***Runnable as Lambda expression***")).start();  
    }
}
