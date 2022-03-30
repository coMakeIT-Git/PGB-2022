package comakeIT;



import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Problem {

	class Primes{
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
	
	
	
	public static void main(String[] args) {
	int[] array = new int[]{ 2,7,11,13,17,5,9,8,12,19,21,26,31,45,56,65,98,89,47,55,61,33,44,66,100};
	List<Integer> list = Arrays.stream(array).boxed().collect(Collectors.toList());
	list.stream().map(x -> Primes.isPrime(x))
	.filter(x -> (x < 25 && x > 0))
	.sorted(Comparator.reverseOrder()).collect(Collectors.toList()).forEach(System.out::println);		
		
	
	System.out.println("Sum of list elements: "+list.stream().reduce(0, (a, b) -> a + b, Integer::sum));
	}
	
	}

