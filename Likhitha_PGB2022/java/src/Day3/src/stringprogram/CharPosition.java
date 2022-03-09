package stringprogram;
import java.util.*;

public class CharPosition {
  public static void main(String[] args)
  {
	  System.out.println("Enter input string");
	  
	  Scanner Sc= new Scanner(System.in);
		String s=Sc.next();
		//("System.out.printlnEnter input string");
		
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
