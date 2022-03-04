package day3;

import java.util.*;

public class character_Count {
	public static void main(String[] args) {
		Map<Character, List<Integer>> dict = new HashMap<>();
		s = s.replaceAll(" ", "");
		for (int i = 0; i < s.length(); i++) {
			char id =  s.charAt(i);
		    if (dict.containsKey(id)) {
		        dict.get(id).add(i);
		    } else {
		        dict.put(id, new ArrayList<Integer>());
		        dict.get(id).add(i);
		    }
	        // System.out.print(s.charAt(i) + " ");
	    }
		return dict.toString();
	}
	public static void main(String[] args) {
		List<String> slist=new ArrayList<>();
		s.list.add("upendar");
		s.list.add("Mallikarjun");
		s.list.add("Varun");
		s.list.add("Saikumar");
		
		for (String name :slist) {
			System.out.println(name);
			System.out.println(count(name));
		}
	}
	
}
