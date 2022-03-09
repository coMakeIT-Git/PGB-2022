package day5Assignment;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;
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

public class PrimeCom {
public static void main(String args[]) {
	Scanner sc= new Scanner(System.in);
	Integer arr[]=new Integer[6];
	 
	System.out.println("Enter any 6 numbers:");
	for(int i=0;i<6;i++) {
		arr[i]=sc.nextInt();
		//al.add(arr[i]);
	}
	List<Integer> al = Arrays.asList(arr);
	System.out.println("Numbers  after converting in to list");
	System.out.println(al);
	System.out.println("Prime numbers less than 5:");
	      al.stream()
			.map(x->checkPrime.isPrime(x))
			.filter(x->(x<25 && x>0))
			.sorted(Comparator.reverseOrder())
            .collect(Collectors.toList())
	        .forEach(System.out::println);
	      System.out.println("Sum of the numbers using Reduce:");
	      System.out.println(al.stream().reduce(0,
                (t1, t2) -> t1 + t2));
}
}
