package Day3.Task2;
import java.util.*;
import java.util.stream.Collectors;
public class Collections {
	public static void main(String args[])
	{
		System.out.println("List Collection");
		ArrayList<String> l=new ArrayList<String>();
		l.add("B");  
		l.add("A");  
		l.add("C");
		System.out.println("Before Sorting ");
		 for(String alpha:l)
		  System.out.println(alpha);
		 System.out.println("After Sorting ");
		 List<String> sortedList =l.stream().sorted().collect(Collectors.toList());
		 sortedList.forEach(System.out::println);  
			System.out.println("Hash Map Collection");
		 HashMap<Integer,String> map=new HashMap<Integer,String>();//Creating HashMap    
		   map.put(65,"A"); 
		   map.put(66,"B");    
		   map.put(67,"C");   
		   map.put(68,"D");   
		       
		   System.out.println("Iterating Hashmap...");  
		   for(Map.Entry m : map.entrySet()){    
		    System.out.println(m.getKey()+" "+m.getValue());    
		   } 
		   
		   System.out.println("Hash Set Collection");
		   HashSet<String> s=new HashSet();  
           s.add("A");    
           s.add("B");    
           s.add("C");   
           s.add("D");  
           s.add("E");  
           Iterator<String> i=s.iterator();  
           while(i.hasNext())  
           {  
           System.out.println(i.next());  
           }  
		}  	
}
