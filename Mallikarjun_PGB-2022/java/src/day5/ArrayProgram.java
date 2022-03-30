package day5_Assignment;

import java.util.*;
import java.util.stream.Collectors;

class checkPrime{
	static int isPrime(int n) {
		if (n == 2 || n == 1)
	        return n;

		if (n <= 1 || n % 2 == 0)
            return -1;


        for (int i = 3; i <= Math.sqrt(n); i +=2)
        {
            if (n % i == 0)
                return -1;
        }
        return n;
    }
}

public class ArrayProgram {

	static int[] ints = {1,2,3,5,6,7,13,19,73,103};

	static List<Integer> list = Arrays.stream(ints).boxed().collect(Collectors.toList());


	public static void main(String[] args) {

		list.stream()
		.map(x -> checkPrime.isPrime(x))
		.filter(x -> (x < 25 && x > 0)) 
		.sorted(Comparator.reverseOrder())
		.collect(Collectors.toList())	
		.forEach(System.out::println);

		System.out.println("Sum Of elements in list : "+list.stream().reduce(0, (a, b) -> a + b, Integer::sum));
	}

}
