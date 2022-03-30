package Day5.task2;

import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.*;

public class streams {
	public static void main(String args[])
	{
		Integer a[]= {52,90,91,12,17,20,13,15,59,61};
		List<Integer> l=Arrays.asList(a);
		System.out.println("Converted Array into List\n"+l+"\n"+"Printing the prime numbers lessthan 25 in numbers");
		
		l.stream().filter(p->check(p) && p<25).forEach(System.out::println);
		List<Integer> prime = l.stream().filter(p->check(p)).collect(Collectors.toList());
		l.stream().map(number -> number).forEach(System.out::println);// used Map to print prime numbers
		System.out.println("Printing the prime numbers in sorted order(Descending Order) ");
		List<Integer> show =
	            prime.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());
		System.out.println(show);
		System.out.println("Used Reduce function and the sum is :");
		int add =
			       l.stream().reduce(0,(ans,i)-> ans+i);
		System.out.print(add);
		
	}

	private static Boolean check(Integer p) {
		int n=(int)p;
		if(n<=1)return false;
		for(int i=2;i*i<=n;i++)
		{
			if(n%i==0)
				return false;
		}
		return true;
		
	}
}
