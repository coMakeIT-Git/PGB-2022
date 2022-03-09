package task3;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;
public class javastream {
	public static void main(String args[])
	{
		Scanner Sc1=new Scanner(System.in);
		String s=Sc1.next();
		Map<Character, List<Integer>> mp = new HashMap<Character, List<Integer>>();
		for(int i=0;i<s.length();i++)
		{
			char str1=s.charAt(i);
			List<Integer> l=mp.get(str1);
			if(l==null)
			{
				List<Integer> newlist=new ArrayList<Integer>();
				newlist.add(i);
				mp.put(str1, newlist);
			}
			else
			{
					l.add(i);
					mp.put(str1, l);
			}
		}
		for (Map.Entry<Character, List<Integer>> me :
            mp.entrySet()) {

           // Printing keys
           System.out.print(me.getKey() + ":");
           System.out.println(me.getValue());
       }
	}
}