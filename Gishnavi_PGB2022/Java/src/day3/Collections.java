package day3;

import java.util.*;
import java.util.stream.Collectors;


public class Collections {
	public static void main(String args[])
	{
		System.out.println("Collection");
		ArrayList<String> list=new ArrayList<String>();
		list.add("ben");  
		list.add("cop");  
		list.add("adem");
		System.out.println("Before Sorting ");
		 for(String alpha:list)
		  System.out.println(alpha);
		 System.out.println("After Sorting ");
		 List<String> sortedList =list.stream().sorted().collect(Collectors.toList());
		 sortedList.forEach(System.out::println);  
			System.out.println("Hash Map Collection");
		 HashMap<Integer,String> hashmap=new HashMap<Integer,String>();//Creating HashMap    
		 hashmap.put(1,"A"); 
		 hashmap.put(2,"B");    
		       
		   System.out.println("Hashmap");  
		   for(Map.Entry m : hashmap.entrySet()){    
		    System.out.println(m.getKey()+" "+m.getValue());    
		   } 
		   
		   System.out.println("HashSet ");
		   HashSet<String> s=new HashSet();  
           s.add("A");    
           s.add("B");    
           s.add("C");   
           Iterator<String> i=s.iterator();  
           while(i.hasNext())  
           {  
           System.out.println(i.next());  
           }  
		}  	
}
