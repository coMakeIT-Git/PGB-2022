package day3Assignment;
import java.util.*;
class Characterposition {
	public static void charpos(String str) {
		Map<Character,List<Integer>> m=new TreeMap<>();
		int l=str.length();
		for(int i=0;i<l;i++) {
			if(!m.containsKey(str.charAt(i))) {
				List<Integer> s=new ArrayList<>();
				s.add(i);
				m.put(str.charAt(i),s);
			}
			else {
				m.get(str.charAt(i)).add(i);
			}
		}
		System.out.println(m);
	}
	public static void main(String[] args) {
		String str="nithish";
		String str2="kranthikumar";
		String str3="akhil";
		charpos(str);
		charpos(str2);
		charpos(str3);
	}
}
