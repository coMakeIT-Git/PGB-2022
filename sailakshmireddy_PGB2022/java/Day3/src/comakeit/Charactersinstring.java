package comakeit;

import java.util.*;

public class Charactersinstring {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter any name: ");
		String name=sc.nextLine();
		Map<Character,List<Integer>> m = new TreeMap<>();
		//Map<Character,List<Integer>> m = new HashMap<>();
		name=name.replace(" ", "");
		for(int i=0;i<name.length();i++) {
			if(!m.containsKey(name.charAt(i))) {
				List<Integer> lst= new ArrayList<>();
				lst.add(i);
				m.put(name.charAt(i), lst);
			}
			else {
				m.get(name.charAt(i)).add(i);
			}
		}
		System.out.println(m);
	}
}
