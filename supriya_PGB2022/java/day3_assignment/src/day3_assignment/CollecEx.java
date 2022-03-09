package day3_assignment;
import java.util.*;
import java.util.ArrayList;
import java.util.stream.Collectors;
public class CollecEx {


		public static void main(String args[])
		{
			System.out.println("List Collection");
			ArrayList<String> l=new ArrayList<String>();
			l.add("Tom");  
			l.add("Jerry");  
			l.add("Disney");
			System.out.println("Before Sorting ");
			 for(String alpha:l)
			  System.out.println(alpha);
			 System.out.println("After Sorting ");
			 List<String> sortedList =l.stream().sorted().collect(Collectors.toList());
			 sortedList.forEach(System.out::println);  
				System.out.println("Hash Map Collection");
			 HashMap<Integer,String> map=new HashMap<Integer,String>();//Creating HashMap    
			   map.put(100,"Dhoni"); 
			   map.put(90,"Warner");    
			   map.put(91,"Kane");   
			   map.put(150,"Sachin");   
			       
			   System.out.println("Iterating Hashmap...");  
			   for(Map.Entry m : map.entrySet()){    
			    System.out.println(m.getKey()+" "+m.getValue());    
			   } 
			   
			   System.out.println("Hash Set Collection");
			   HashSet<String> s=new HashSet();  
	           s.add("Ball");    
	           s.add("Bat");    
	           s.add("Wickets");   
	           s.add("Empire");  
	           s.add("Wicketkeeper");  
	           Iterator<String> i=s.iterator();  
	           while(i.hasNext())  
	           {  
	           System.out.println(i.next());  
	           }  
			}  	
	}

