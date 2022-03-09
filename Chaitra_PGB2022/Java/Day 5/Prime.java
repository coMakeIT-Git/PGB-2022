import java.util.*;

class Prime{
		
	public static int isPrime(int number) {
        for (int i = 2; i <= number / 2; i++) {
            if (number % i == 0) {
                return 99999;
            }
        }
        return number;
    }
	
	public static void main(String args[]) {
		int[] arr = { 1, 45, 23, 7, 9, 100, 677, 43, 17, 19, 9 };
		 
		// Converting primitive integer array to an Integer array
		Integer[] boxedArray = Arrays.stream(arr).boxed().toArray(Integer[]::new);
		 
		// add all elements of the Integer array to a list of Integer
		List<Integer> list = new ArrayList<>();
		Collections.addAll(list, boxedArray);
		 
		// print the list
		System.out.println("Elements: " + list);
		System.out.println("Primes less than 25 in descending order: ");
		list.stream().map(x -> isPrime(x)).filter(x -> x<=25).sorted(Comparator.reverseOrder()).forEach(x -> System.out.print(x+ " "));
		//System.out.println(list);


	}
}
