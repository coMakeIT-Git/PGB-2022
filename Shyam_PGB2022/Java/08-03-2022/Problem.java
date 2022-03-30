import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.*;
import java.util.function.Supplier;
import java.util.function.Predicate;
import java.util.function.Consumer; 

interface Sayable{  
    void say();  
}  
public class Problem {
	static void printMessage(String name){  
        	System.out.println("Hello "+name);  
   	}  
   	public static void saySomething(){
   	 	System.out.println("HEYYY");
   	 }
	public static void main(String args[])
	{
		Sayable s = Problem::saySomething; //Method Reference
		s.say();
		Consumer<String> consumer = Problem::printMessage;  //Creating consumer
        	consumer.accept("SHYam");  
		Predicate<String> pr = message -> (message == "Hi"); // Creating predicate  
        	System.out.println(pr.test("Hey"));
		Supplier<Double> randomValue = () -> Math.random();// Creating Supplier
		System.out.println(randomValue.get());
		Integer a[]= {52,90,91,12,17,20,13,15,59,61};
		List<Integer> list=Arrays.asList(a);
		System.out.println("Elements: " + list);
		System.out.println("Primes less than 25 in descending order: ");
		list.stream().map(x -> isPrime(x)).filter(x -> x<=25).sorted(Comparator.reverseOrder()).forEach(x -> System.out.print(x+ " "));	
	}
	public static int isPrime(int number) {
        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0) {
                return 99999;
            }
        }
        return number;
    }
}
