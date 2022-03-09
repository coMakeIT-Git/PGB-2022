package task3;

import java.util.*;
import static java.util.stream.Collectors.toList;
import java.util.function.Predicate;

public class ArrayProgram {
 public static void main(String[] args)
 {
	 //int[] arr =new int[] {1,2,3,4,5,6,7,8,9,10};
	 
	 int n;  
	 Scanner sc=new Scanner(System.in);  
	 System.out.print("Enter the number of elements you want to store: ");  
	 //reading the number of elements  
	 n=sc.nextInt();  
	 //creates an array in the memory of length 10  
	 int[] array = new int[n];  
	 System.out.println("Enter the elements of the array: ");  
	 for(int i=0; i<n; i++)  
	 {  
	 //reading array elements from the user   
	 array[i]=sc.nextInt();  
	 }  
	 
	 List<Integer> li = new ArrayList<Integer>();
	 
	 for(int i: array)
	 {
		 li.add(i);
	 }
	 
	 System.out.println("Print the prime numbers using map.stream");
	 
	 
	 List<Integer> l=li.stream().filter(ArrayProgram::isPrime).collect(toList());
	 l.stream().map(n1->n1).forEach(System.out::println);
	 
	 System.out.println("Printing prime numbers less than 25 using stream filter");
	 
	 li.stream().filter(number -> number<25 && isPrime(number)).forEach(System.out::println);
	 
	 System.out.println("Printing array numbers in descending order");
	 
	 List<Integer> sortedList = li.stream().sorted(Collections.reverseOrder()).collect(toList());

		System.out.println(sortedList);
System.out.println("Using reduce to add all integers");
		Integer sum = li.stream()
				  .reduce(0, Integer::sum);
		
		System.out.println(sum);
	 //li.sorted(Comparator.reverseOrder()).forEach(System.out::println);
	 
	 //li.stream().map(number -> isPrime(number)).forEach(System.out::println);
	 
	 
 }
 
 public static boolean isPrime(int number) {
	 if(number==1 && number>25)
		 return false;
	 
     for (int i = 2; i <= number / 2; i++) {
         if (number % i == 0) {
             return false;
         }
     }
     return true;
 }
}
