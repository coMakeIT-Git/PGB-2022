import java.util.*;
class Stringg{
	public static void main(String[] args){
		String str= args[0];
		str=str.replaceAll(" ", "");
		HashMap<Character,LinkedList<Integer>> x = new HashMap();
		for(int i=0;i<str.length();i++){
			char c = str.charAt(i);
			LinkedList lt;
			if(!x.containsKey(c)){
				lt = new LinkedList();
			}
			else{
				lt = x.get(c);
			}
			lt.add(i);
			x.put(c,lt);
		}
		System.out.println(x.toString());
	}
}
