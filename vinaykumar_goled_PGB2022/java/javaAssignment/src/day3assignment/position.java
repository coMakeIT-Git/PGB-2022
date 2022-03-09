package day3assignment;
import java.util.*;
import java.util.HashMap;
import java.util.Map;

public class position {
	public static void main(String[] args) {
		Scanner s1 = new Scanner(System.in);
		System.out.println("Enter a string: ");
		String str = s1.nextLine();
		HashMap<Character, List<Integer>> hm = new HashMap<>();
		for(int i = 0; i < str.length(); i++) {
			char c = str.charAt(i);
			List l;
			if(hm.containsKey(c)) {
				hm.get(c).add(i);
			}
			else {
				l = new LinkedList();
				l.add(i);
				hm.put(c, l);
			}
		}
		System.out.println(hm);
		s1.close();
	}
}
