package sreeja5;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Task4 {
	public static void main(String[] args) {
		  
		   // create an array
		   int[] arr = {12, 4, 5, 2, 7,19,27,76,99,91,31};
		   for(int i = 0; i < arr.length; i++) {
			     System.out.println(arr[i]);
		   }
		   System.out.println("converting array to list");
		   List<Integer> list = new ArrayList<>(arr.length);
		   
	        for (int i: arr) {
	            list.add(Integer.valueOf(i));
	        }
	 
	        System.out.println(list);
	        //list.stream().filter(x->check(x) && x<25).forEach(System.out::println);
			List<Integer> prime = list.stream().filter(x->check(x) && x<25).collect(Collectors.toList());
			prime.stream().map(n1->n1).forEach(System.out::println);
			System.out.println("Printing in Descending Order");
			List<Integer> show =
		            prime.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());
			System.out.println(show);
			System.out.println("Used Reduce function and sum is :");
			int add =list.stream().reduce(0,(ans,i)-> ans+i);
			System.out.print(add);
	        
	        
	}
	private static Boolean check(Integer x) {
		int n=(int)x;
		if(n<=1)return false;
		for(int i=2;i*i<=n;i++)
		{
			if(n%i==0)
				return false;
		}
		return true;
		
	}



}
