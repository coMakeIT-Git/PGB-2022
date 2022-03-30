import java.util.function.*;

class FunctionalInterface{
	public static void main(String args[]) {
		//Consumer
		Consumer<Integer> display = (a) -> System.out.println("Consumer: " + a);
	    display.accept(10);
	    
	    //Supplier
	    Supplier<Double> supplier = () -> Math.random();
	    System.out.println("Supplier: " + supplier.get());
	    
	    //Predicate
	    Predicate<Integer> lesserthan = i -> (i < 18); 
	    System.out.println("Predicate: " + lesserthan.test(10)); 	    
	}
}
	
