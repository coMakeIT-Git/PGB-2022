package Day5Assignment;
import java.util.*;
import java.util.stream.*;
public class ArrayNum {
	public static int checkPrime(int number)
	{
		int c=1;
		for(int i=1;i<number;i++)
		{
			if(number%i==0)c++;
			
		}
		if(c==2)
		return number;
		else return -1;
	}
 public static void main(String args[])
 {
	 int arr[]= {2,3,4,5,6,7,8,9,10,23,29};

	 List<Integer> arrlist=Arrays.stream(arr).boxed().collect(Collectors.toList());
	 arrlist.stream().map(number->checkPrime(number)) //Getting only prime numbers
			 .filter(x->(x>0 &&x<25))                 // Filtering the values to get in between range
			 .sorted(Comparator.reverseOrder())       // Sorting the list to get descending order
			 .collect(Collectors.toList())
			 .forEach(System.out::println);
	 System.out.println(arrlist.stream().reduce(0,(a,b) -> a+b)); //Using reduce function for sum of values in list
	 
	 
	
 }

}
