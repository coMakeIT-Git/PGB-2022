package day5;

import java.util.*;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.concurrent.ThreadLocalRandom;

//nextInt is normally exclusive of the top value,
//so add 1 to make it inclusive


class checkPrime{
	static int isPrime(int n) {
		if (n == 2 || n == 1)
	        return n;
		
		if (n <= 1 || n % 2 == 0)
            return -1;

 
        for (int i = 3; i <= Math.sqrt(n); i += 2)
        {
            if (n % i == 0)
                return -1;
        }
        return n;
    }
}

public class Program {
	static int min = 1;
	static int max = 30;
	static int[] ints = new int[10];
	
	public static void main(String[] args) {

		// Using Consumer To Print the given number
		Consumer<? super Integer> printConsumer = n -> System.out.println(n);
		
		// Using Supplier To Generate a Random Integer
		Supplier<Integer> doubleSupplier1 = () -> (int) ThreadLocalRandom.current().nextInt(min, max + 1);
		
		for (int i = 0;i < 10; i++) {
			int s = doubleSupplier1.get();
			//  System.out.println(s);
			ints[i] = doubleSupplier1.get();
		}
		
		// Converting number array to list
		List<Integer> list = Arrays.stream(ints).boxed().collect(Collectors.toList());
		
		// Using Predicate To Get all numbers >25 and <0
		Predicate<Integer> numlessthan25 = num -> num < 25;
		Predicate<Integer> numgreaterthan0 = num -> num > 0;
		
		System.out.println("Given List :" +list+"\nPrinting Prime Numbers in Descending Order : ");;
		
		list.stream()
			.map(x -> checkPrime.isPrime(x)) 	// Using .map() to get all prime numbers
			.filter(numlessthan25.and(numgreaterthan0))  	// Using .filter() to get prime numbers less than 25
			.sorted(Comparator.reverseOrder())	// Using .sorted() to sort the above numbers in descending order
			.collect(Collectors.toList())		// Using .collect() to store the above sorted list into a list
			.forEach(printConsumer);		// Using .forEach() to print the prime numbers less than 25
 		
		// Using .reduce() to get the sum of all the integers in list
		System.out.println("Sum Of elements in list : "+list.stream().reduce(0, (a, b) -> a + b, Integer::sum));
	}

}
