package comakeit3;

import java.util.*;

public class program {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter your name: ");
		String name=sc.next();
		Map<Character,List<Integer>> map = new TreeMap<>();
		name=name.replace(" ", "");
		for(int i=0;i<name.length();i++) {
			if(!map.containsKey(name.charAt(i))) {
				List<Integer> l1= new ArrayList<>();
				l1.add(i);
				map.put(name.charAt(i), l1);
			}
			else {
				map.get(name.charAt(i)).add(i);
			}
		}
		System.out.println(map);
	}

}
