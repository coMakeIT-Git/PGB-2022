package day3;

import java.util.*;

public class char_Count {
	public static void main(String[] args) {
		Map<Character, List<Integer>> dict = new HashMap<>();
		String s = "Hello World";
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
		System.out.println(dict.toString());
	}
	
}
