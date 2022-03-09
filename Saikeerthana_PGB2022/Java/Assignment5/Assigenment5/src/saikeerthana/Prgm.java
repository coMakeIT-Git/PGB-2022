package saikeerthana;
import java.util.*;
import static java.util.stream.Collectors.toList;
import java.util.stream.Collectors;
public class Prgm {
	public static void main(String[] args) {
	 int n;  
	 Scanner sc=new Scanner(System.in);  
	 System.out.print("Enter the number of elements:");  
	 //read  number of elements  
	 n=sc.nextInt();  
	 //creates an array  
	 int[] array = new int[n];  
	 System.out.println("Enter the elements of the array: ");  
	 for(int i=0; i<n; i++)  
	 {  
	 //reading array elements   
	 array[i]=sc.nextInt();  
	 }  

	 List<Integer> li = new ArrayList<Integer>();

	 for(int i: array)
	 {
		 li.add(i);
	 }

	 System.out.println("Print the prime numbers using map.stream()");


	 System.out.println(li.stream().filter(Prgm::check).collect(toList()));

	 System.out.println("Printing prime numbers less than 25 using stream.filter()");

	 li.stream().filter(number -> number<25 && check(number)).forEach(System.out::println);

	 System.out.println("Printing array numbers in descending order");

	 List<Integer> sortedList = li.stream().sorted(Collections.reverseOrder()).collect(toList());

		System.out.println(sortedList);
System.out.println("Using reduce to add all integers");
		Integer sum = li.stream()
				  .reduce(0, Integer::sum);

		System.out.println(sum);
	 

}


public static boolean check(int num) {
	 if(num==1 && num>25)
		 return false;

    for (int i = 2; i <= num / 2; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}
}
