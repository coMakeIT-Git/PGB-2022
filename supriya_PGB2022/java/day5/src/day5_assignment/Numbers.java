package day5_assignment;


import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
//import java.util.stream.IntStream;


public class Numbers {
public static void main(String[] args) {
	int[] num= {2,4,6,3,17,19,23,29,53,59,22,24,16,18};
	
	List<Integer> list = Arrays.stream(num).boxed().collect(Collectors.toList());
	 System.out.println(list);
    
	list.stream().map(primenumber->Numbers.isPrime(primenumber))
    
   .filter(primenumber -> (primenumber < 25 && primenumber > 0))
    																	
	.sorted(Comparator.reverseOrder()) 

	.collect(Collectors.toList()) 
	 
	.forEach(System.out::println);  
   
    System.out.println("The Total Sum of elements in list : " + list.stream().reduce(0, (a, b) -> a + b, Integer::sum));
}
//to check if the number is prime or not 
 static int isPrime(int number) {
	 int i, m = 0;
		m = number / 2;
		if (number == 0 || number == 1) {
			return 0;
		} else {
			for (i = 2; i <= m; i++) {
				if (number % i == 0) {
					return 0;
				}
			}
			return number;
		}
	}
	}








	

