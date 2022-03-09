import java.util.*;
class CharPosition
{
public static void main(String[] args)
{
		String str= args[0];
		System.out.println("The given command line argument is: "+"  " +args[0]);
		System.out.println("The positions of characters in"+"  "+args[0]+"  "+"are:");
		str=str.replaceAll(" ", "");
		HashMap<Character,LinkedList<Integer>> x = new HashMap();
		for(int i=0;i<str.length();i++)
		{
			char c = str.charAt(i);
			LinkedList lt;
			if(!x.containsKey(c))
			{
				lt = new LinkedList();
			}
			else
			{
				lt = x.get(c);
			}
			lt.add(i);
			x.put(c,lt);
		}
		System.out.println(x.toString());
}
}
