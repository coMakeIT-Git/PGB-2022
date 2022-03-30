package day5assignment;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class NumberArray {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the size of array:");
		int n = sc.nextInt();
		int arr[] = new int[n];
		System.out.println("Enter the elements of the array:");
		for(int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		List<Integer> list = new ArrayList<>(n);
		for(int i : arr) {
			list.add(Integer.valueOf(i));
		}
		System.out.println("Integer array after converting it to a list:");
		System.out.println(list);
		
		System.out.println("List of prime numbers less than 25 using map stream:");
		System.out.println(list.stream().map(x->isPrime(x))
				.filter(x->(x>0 && x<25))
				.collect(Collectors.toList()));
		
		System.out.println("Sorting in descending order: ");
		list.stream().sorted(Comparator.reverseOrder()).forEach(System.out::println);
		
		int sum = Arrays.stream(arr).reduce(0, (a, b) -> a + b);
		System.out.println("Sum using reduce: " +sum);
		
	}
	
	
	public static int isPrime(int number) {
		for(int i = 2; i <= number / 2; i++) {
			if(number % i == 0) {
			 return -1;
			}
		}
		return number;
	}
}
