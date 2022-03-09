package sreeja3;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.*;
import java.util.stream.Collectors;

import javax.swing.text.html.HTMLDocument.Iterator;

public class Collection {
	public static void main(String args[]){  
		 //Creating a List  
		System.out.println("LIST");
		 List<String> list=new ArrayList<String>();  
		 //Adding elements   
		 list.add("M");  
		 list.add("A");  
		 list.add("B");  
		 list.add("G");  
		 //Iterating the List element using for-each loop  
		 System.out.println("before sorting");
		 for(String fruit:list)  
		  System.out.println(fruit);  
		 System.out.println("after sorting");
		 List<String> sortedList =list.stream().sorted().collect(Collectors.toList());
		sortedList.forEach(System.out::println);
		System.out.println("SET");
		Set<String> hash_Set = new HashSet<String>();
		 
        // Adding elements to the Set
        
        hash_Set.add("G");
        hash_Set.add("A");
        hash_Set.add("B");
        hash_Set.add("M");
        hash_Set.add("G");
 
        // Printing elements
        System.out.println(hash_Set);
        System.out.println("MAP");
        Map<Integer,String> map=new HashMap<Integer,String>();  
        //Adding elements to map  
        map.put(1,"A");  
        map.put(5,"X");  
        map.put(2,"D");  
        map.put(6,"Z");  
        //Traversing Map  
        for(Map.Entry m:map.entrySet()) {
        	System.out.println(m.getKey()+" "+m.getValue());
        	
        }
        
		}  
}
