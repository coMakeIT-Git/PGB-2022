package sowmya5;
import java.util.*;
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
public class Arrayprime{
	public static void main(String args[]) {
		int n; 
		Scanner sc=new Scanner(System.in); 
		System.out.println("enter arry size:");
		n=sc.nextInt();  
		//creates an array in the memory of length 10  
		int[] array = new int[20];  
		System.out.println("Enter the elements of the array: ");  
		for(int i=0; i<n; i++) {    
		array[i]=sc.nextInt();  
		}  
		List<Integer> list = Arrays.stream(array).boxed().collect(Collectors.toList());
		list.stream()
		.map(x -> checkPrime.isPrime(x)) 	// Using .map() to get all prime numbers
		.filter(x -> (x < 25 && x > 0))  	// Using .filter() to get prime numbers less than 25
		.sorted(Comparator.reverseOrder())	// Using .sorted() to sort the above numbers in descending order
		.collect(Collectors.toList())		// Using .collect() to store the above sorted list into a list
		.forEach(System.out::println);		// Using .forEach() to print the prime numbers less than 25
		// Using .reduce() to get the sum of all the integers in list
		System.out.println("Sum Of elements in list : "+list.stream().reduce(0,(a, b) -> a + b));

	}
}