import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.*;
import java.util.function.Supplier;
import java.util.function.Predicate;
import java.util.function.Consumer; 

 
public class StreamsDemo {
	
	public static void main(String args[])
	{
		Integer a[]= {55,96,65,61,53,20,13,11,5,93};
		List<Integer> list=Arrays.asList(a);
		System.out.println("Elements: " + list);
		System.out.println("Primes less than 25 in descending order: ");
		list.stream().map(x -> isPrime(x)).filter(x -> x<=25).sorted(Comparator.reverseOrder()).forEach(x -> System.out.println(x+ " "));	
	}
	public static int isPrime(int number) {
        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0) {
                return 99999;
            }
        }
        return number;
    }
}
