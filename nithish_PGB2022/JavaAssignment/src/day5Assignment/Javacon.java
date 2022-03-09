package day5Assignment;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
public class Javacon {
	public static void main(String[] args) {
        //Suppliers
        Supplier<Double> randomValue = () -> Math.random();
        
        // Print the random value using get()
        System.out.println(randomValue.get());
    
        // predicate
        Predicate<Integer> lesserthan = i -> (i < 18); 
      
        // Calling Predicate method
        System.out.println(lesserthan.test(20)); 
        
        // consumers
        Consumer<Integer> display = a -> System.out.println(a);
        
        // Implement display using accept()
        display.accept(15);
        
        //Function
        Function<Integer,Double> func=a->a/2.0;
        func=func.compose(a->3*a);
        System.out.println(func.apply(15));    
	}
}
