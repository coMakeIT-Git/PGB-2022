package Day3.Task3;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;
public class Index {
	public static void main(String args[])
	{
		Scanner Sc=new Scanner(System.in);
		String s=Sc.next();
		Map<Character, List<Integer>> mp = new HashMap<Character, List<Integer>>();
		for(int i=0;i<s.length();i++)
		{
			char s1=s.charAt(i);
			List<Integer> l=mp.get(s1);
			if(l==null)
			{
				List<Integer> newl=new ArrayList<Integer>();
				newl.add(i);
				mp.put(s1, newl);
			}
			else
			{
					l.add(i);
					mp.put(s1, l);
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
