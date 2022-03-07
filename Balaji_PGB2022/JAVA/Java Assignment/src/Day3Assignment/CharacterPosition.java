package Day3Assignment;
import java.util.*;
public class CharacterPosition {
   public static void position(String str)
   {
	   HashMap<Character,List<Integer>> hm=new HashMap<>();
	   for(int i=0;i<str.length();i++)
	   {
		   
		   char c=str.charAt(i);
		   List l;
		   if(hm.containsKey(c))
		   {
			   hm.get(c).add(i);
			   
		   }
		   else
		   {
			 l=new LinkedList();
			 l.add(i);
			 hm.put(c,l);
		   }
	   }
	   System.out.println("Character Position Of " +str+ " is: "+hm);
	   
   }
   public static void main(String args[])
   {
	   position("Akhil");
	   position("Nithish");
	   position("Balaji");
	   position("Dheeraj");
   }
}
