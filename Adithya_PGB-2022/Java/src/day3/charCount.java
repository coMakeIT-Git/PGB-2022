package day3;
import java.util.*;
class charCount{
	public static String func(String s) {
		s=s.replaceAll(" ", "");
		HashMap<Character,LinkedList<Integer>>hm=new HashMap();
		for(int i=0;i<s.length();i++){
			char c=s.charAt(i);
			
		 	LinkedList l;
			if(!hm.containsKey(c)){
				l=new LinkedList();
			}
			else{
				l=hm.get(c);
			}
			l.add(i);
			hm.put(c,l);
		}
		return hm.toString();
	}
	public static void main(String[]args){
		System.out.println("Output for Adithya "+func("Akil"));
		System.out.println("Output for Dheeraj "+func("Dheeraj"));
		System.out.println("Output for Balaji "+func("Balaji"));
	}
}