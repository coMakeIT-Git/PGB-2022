import java.util.*;

class CharOccurence{
	public static void main(String args[]) {
		HashMap<Character, ArrayList<Integer>> occur = new HashMap<Character, ArrayList<Integer>>();
		String s = args[0];
		char c;
		int index;
		ArrayList lst;
		for(int i=0; i<s.length(); i++) {
			c = s.charAt(i);
			index = s.indexOf(c);
			if(occur.containsKey(c)) {
				lst = occur.get(c);
				Object[] arr = lst.toArray();
				index = s.indexOf(c, (int)arr[arr.length - 1]+1);
				occur.get(c).add(index);
			}
			else {
				occur.put(c, new ArrayList<Integer>());
				occur.get(c).add(index);
			}			
		}
		System.out.print(occur + "\n");
	}
}

