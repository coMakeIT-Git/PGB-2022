package task3;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
public class primefun {
	
public static boolean isPrime(int number) {
        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
public static void main(String args[])
{
	int num[] = {1,2,3,4,5,6,8,9,10,22,30,7,13,17,19,31,51,97,73};
	
	List<Integer> list = Arrays.stream(num).boxed().collect(Collectors.toList());
	System.out.println("Convert numbers array to list in Java :"+list);
	
	//stream map
	 System.out.println("Prime numbers:"+list.stream()
             .filter(primefun::isPrime)
             .collect(Collectors.toList()));
	
	 
	//stream filter
	 System.out.println("Prime numbers less than 25:"+list.stream()
     .filter(primefun::isPrime).filter(prime -> prime < 25)
     .collect(Collectors.toList()));
	 
   //sort in descending order
	 Collections.sort(list, Collections.reverseOrder());
	 System.out.println("sort in descending order :"+list);
	 
  //Use Reduce to add all the numbers in numbers list
	 System.out.println("REduce:"+list.stream()
  .reduce(0, (subtotal, element) -> subtotal + element));
	 
	 System.out.println("Prime less than 25 and reduce :"+list.stream().filter(primefun::isPrime).filter(prime -> prime < 25)
	 .reduce(0, (subtotal, element) -> subtotal+ element));
}
}