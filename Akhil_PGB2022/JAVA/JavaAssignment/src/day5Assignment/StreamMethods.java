package day5Assignment;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;import java.util.stream.Collector;
import java.util.stream.Collectors;

public class StreamMethods {
	public static int isPrime(int x) {
		for(int i=2; i<=(x/2); i++) {
			if(x%i==0)
				return -1;
		}
		return x;
	}
	public static void main(String[] args) {
		int[] arr = {3,4,5,6,7,8,9,37,73};
		List<Integer> lst = Arrays.stream(arr).boxed().collect(Collectors.toList());
		
		List<Integer> l = lst.stream().map(x -> isPrime(x)) //stream.map() to get the list of prime numbers
			.filter(y -> (y>0 && y<25))						//tream.filter() to take out prime numbers smaller than 25
			.sorted(Comparator.reverseOrder())              //stream.sorted() method to sort the numbers in descending order
			.collect(Collectors.toList());
		System.out.println("Prime numbers in reverse order:");
		l.forEach(System.out::println);
		System.out.println("Sum of numbers using reduce:");
		System.out.println(l.stream().reduce(0,(a,b)->a+b));
		
	}
}
