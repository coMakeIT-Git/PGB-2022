import java.util.*;
import java.util.Map;

public class CharPos {
	
	public static void main(String args[]) {
		//Scanner sc =new Scanner(System.in);
		//System.out.println("Enter String");

		//String s=sc.next();
		String s = args[0];
		Map<Character ,List<Integer>> hm= new HashMap<>();
		for(int i=0;i<s.length();i++) {
		if(!hm.containsKey(s.charAt(i))) {
			List<Integer> lis=new ArrayList<>();
			lis.add(i);
			hm.put(s.charAt(i), lis);
			
		}
		else {
			hm.get(s.charAt(i)).add(i);
		}
		}
		        
		        TreeMap<Character, List<Integer>> sorted = new TreeMap<>();
		 
		        
		        sorted.putAll(hm);
		 
		        
		        for (Map.Entry<Character, List<Integer>> entry : sorted.entrySet())
		            System.out.print( entry.getKey() +"="+entry.getValue()+"  ");       
		    
		
		
		
	}

}
