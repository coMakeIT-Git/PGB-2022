package comakeit;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ConvertingArrays {

	class Prime{
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
	int[] array = new int[]{ 1,2,3,4,5,6,7,9,11,15,17,18,19,22,26,28,29,75,73,100};
	List<Integer> list = Arrays.stream(array).boxed().collect(Collectors.toList());
	list.stream().map(x -> Prime.isPrime(x))
	.filter(x -> (x < 25 && x > 0))
	.sorted(Comparator.reverseOrder()).collect(Collectors.toList()).forEach(System.out::println);		
		
	
	System.out.println("Sum of list : "+list.stream().reduce(0, (a, b) -> a + b, Integer::sum));
	}
	
	}
