package day5Assignment;
import java.util.*;
import java.util.stream.Collectors;

public class ArrayNumber {
	public static int prime(int n) {
		for(int i=2;i<=n/2;i++) {
			if(n%i==0) {
				return -1;
			}
		}
		return n;
	}
	public static void main(String[] args) {
		int ar[]= {3,5,7,9,12,14,13,16};
		List<Integer> list=new ArrayList<Integer>();
		for(int i=0;i<ar.length;i++) {
			list.add(ar[i]);
		}
		List<Integer> l=list.stream().map(x->prime(x))
							.filter(y->(y>0 && y<25))
							.sorted(Comparator.reverseOrder())
							.collect(Collectors.toList());
		System.out.println("Prime numbers in reverse order:");
		l.forEach(System.out::println);
		
		System.out.println("Sum of numbers using reduce:");
		System.out.println(l.stream().reduce(0,(a,b)->a+b));
		
	}
}
