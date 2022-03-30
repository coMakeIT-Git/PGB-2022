package day5;
import java.util.*;
import java.util.function.*;
import java.util.stream.*;
public class Streams {
	public static int isPrime(int n){
		if(n==1||n==2){
			return n;
		}
		if(n<=0){
			return -1;
		}
		for(int i=3;i<=Math.sqrt(n);i++){
			if(n%i==0){
				return -1;
			}
		}
		return n;
	}
	public static void main(String[] args) {
		int[]arr={1,2,3,17,24,47};
		//number array to list
		List<Integer>l=Arrays.stream(arr).boxed().collect(Collectors.toList());
		List<Integer>arrlist=l.stream()
				.map(x->isPrime(x))//map to derive prime numbers
				.filter(x->(x>0&&x<25))//to filter numbers with value greater than 25 and less than 0
				.sorted(Comparator.reverseOrder())//sorting in reverse order
				.collect(Collectors.toList());
		arrlist.forEach(System.out::println);
		//Reduce
		System.out.println(arrlist.stream().reduce(0,(a,b)->a+b));
		//Supplier
		Supplier<Double> f = () -> Math.random();
		System.out.println(f.get());
		//predicate
		Predicate<Integer> lesserthan = i -> (i < 18); 
        System.out.println(lesserthan.test(10)); 
        //consumer
        Consumer<Integer> display = a -> System.out.println(a);
        display.accept(10);
        //function
        Function<Integer, Double> half = a -> a / 2.0;
        half = half.compose(a -> 3 * a);
        System.out.println(half.apply(5));
	}
}
