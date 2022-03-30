package day5Assignment;

import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

public class DifferentFunctionalInterfaces {
	public static void main(String[] args) {
		//Supplier
		Supplier<Double> value = ()->Math.random();
		System.out.println("Supplier value: "+value.get());
		
		//Predicate
		Predicate<Integer> x = i->(i>18);
		System.out.println("Predicate value: "+x.test(34));
		
		//consumer
		Consumer<Integer> display = a -> System.out.println("Calling consumer with input "+a);
        // Implement display using accept()
        display.accept(10);
		
		 //Function
        Function<Integer,Double> func=a->a/2.0;
        func=func.compose(a->4*a);
        System.out.println("Calling Function "+func.apply(10));
	}
}
