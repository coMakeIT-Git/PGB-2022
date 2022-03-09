package day3;

import java.util.*;

public class PositionOfCharacter {
	
	public static void main (String[] args) {
		Scanner sc = new Scanner (System.in);
		System.out.println("Enter The Name : ");
		String s = sc.next();
		Map<Character, List<Integer>> cp = new HashMap<>();
		
		for (int i = 0; i< s.length(); i++)
		{
			if(!cp.containsKey(s.charAt(i))) {
				List<Integer> lst = new ArrayList<>();
				lst.add(i);
				cp.put(s.charAt(i), lst);
			} else {
				
				cp.get(s.charAt(i)).add(i);
			}
		}
		System.out.println(cp);
	}

}
