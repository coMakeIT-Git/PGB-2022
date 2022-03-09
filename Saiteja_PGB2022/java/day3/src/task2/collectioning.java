package task2;
import java.util.*;
import java.util.stream.Collectors;
public class collectioning {
	public static void main(String args[]) {
		System.out.println("List");
	ArrayList<String> l1=new ArrayList<String>();
	l1.add("ram");
	l1.add("sam");
	l1.add("sai");
	Iterator<String> it=l1.iterator();  
	System.out.println("Before sorting");
	while(it.hasNext()){  
	System.out.println(it.next());  
	}
	
	System.out.println("After sorting");
	List<String> sortedList =l1.stream().sorted().collect(Collectors.toList());
	 sortedList.forEach(System.out::println);  
	 System.out.println("Hashset");
	HashSet<String> h1=new HashSet<String>();  
    h1.add("ram");    
    h1.add("sam");    
    h1.add("sai"); 
    Iterator<String> i=h1.iterator();  
    while(i.hasNext())  
    {  
    System.out.println(i.next());  
    }  
    System.out.println("Hashmap");
	HashMap<Integer,String> mp=new HashMap<Integer,String>();//Creating HashMap    
	   mp.put(1,"Mango");  //Put elements in Map  
	   mp.put(2,"Apple");    
	   mp.put(3,"Banana");   
	   mp.put(4,"Grapes");   
	       
	   System.out.println("Hashmap");  
	   for(Map.Entry m : mp.entrySet()){    
	    System.out.println(m.getKey()+" "+m.getValue());    
	   }  }}
