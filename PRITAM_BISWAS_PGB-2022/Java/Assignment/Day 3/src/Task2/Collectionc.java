package Task2;

import java.util.*;
import java.util.stream.Collectors;
class Product{  
	   public int id;  
	    public String name;  
	    public float price;  
	    public Product(int id, String name, float price) {  
	        this.id = id;  
	        this.name = name;  
	        this.price = price;  
	    }  
	} 
public class Collectionc {
 
	public static void main(String args[])
	{
		System.out.println("Java stream : ");
        List<Product> productsList = new ArrayList<Product>();  
        //Adding Products  
        productsList.add(new Product(1,"HP Laptop",25000));  
        productsList.add(new Product(2,"Dell Laptop",30000));  
        productsList.add(new Product(3,"Lenevo Laptop",28000));  
        productsList.add(new Product(4,"Sony Laptop",28000));  
        productsList.add(new Product(5,"Apple Laptop",90000));  
        // filtering data  
        productsList.stream()  
                             .filter(product -> product.price == 30000)  
                             .forEach(product -> System.out.println(product.name));   
		    		 
		System.out.println("List Collection"); // create list
		
		ArrayList<String> l=new ArrayList<String>();
		
		l.add("apple");   // add items
		l.add("orange");  
		l.add("gauva");
		
		System.out.println("Before Sorting "); 
		 for(String alpha:l)
		  System.out.println(alpha);
		 
		 System.out.println("After Sorting "); // sort  list of elements
		List<String> sortedList =l.stream().sorted().collect(Collectors.toList());
		 sortedList.forEach(System.out::println);  
		 
			System.out.println("Hash Map Collection"); // create hash map
		 HashMap<Integer,String> map=new HashMap<Integer,String>();  
		 
		   map.put(1,"pritam"); 
		   map.put(2,"Balaji");    
		   map.put(3,"james");   
		   map.put(4,"Drek");   
		   
		   //java stream
		   
		  
		   System.out.println("Iterating Hashmap...");  
		   
		   for(Map.Entry m : map.entrySet())
		   {    
		    System.out.println(m.getKey()+" "+m.getValue());    
		   } 
		   
		   System.out.println("Hash Set Collection");
		   
		   HashSet<String> s=new HashSet();  // create hashset
		   
           s.add("Astra");    
           s.add("Bolt");    
           s.add("Ceaser");   
           s.add("Dremerwat");  
           s.add("Erekert");  
           
           Iterator<String> i=s.iterator();  
           while(i.hasNext())  
           {  
           System.out.println(i.next());  
           }  
           
           
           
		}  	
}
