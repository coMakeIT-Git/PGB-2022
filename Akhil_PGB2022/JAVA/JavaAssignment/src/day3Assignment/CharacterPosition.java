package day3Assignment;
import java.util.*;

public class CharacterPosition {
	public static void func(String s) {
		Map<Character,List<Integer>> hm = new HashMap<>();
		for(int i=0;i<s.length();i++) {
			if(!hm.containsKey(s.charAt(i))) {
				List<Integer> lst = new ArrayList<>();
				lst.add(i);
				hm.put(s.charAt(i),lst);
			}
			else {
				hm.get(s.charAt(i)).add(i);
			}
		}
		System.out.println("CharacterPosition");
		System.out.println(hm);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter String:");
		String s  =sc.next();
		func(s);
		System.out.println("\nEnter String:");
		String s1  =sc.next();
		func(s1);
		System.out.println("\nEnter String:");
		String s2  =sc.next();
		func(s2);
	}
}
