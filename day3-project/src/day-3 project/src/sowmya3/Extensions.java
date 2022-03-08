package sowmya3;
import java.util.HashMap;
import java.util.*;
import java.util.ArrayList;
import java.util.Iterator;
abstract class AbstractDemo
{
	abstract void demo();
}
interface In1 {
	public void eat();
	public void travel();
}
public class Extensions extends AbstractDemo implements In1 {
	
	public void eat() {//method1 
	System.out.println("\nperson eats method");
	}
	public void travel() {//method2
		System.out.println("person travels method");
	}
	public void demo() {//method3
		System.out.println("demo method");
	}
	Extensions(){
		HashMap<Integer, String> hm = new HashMap<Integer, String>();//implements map interface 
		System.out.println("map in collections");
		hm.put(130, "sowmya");    
		hm.put(140, "keerthana\n");  
		Iterator <Integer> it = hm.keySet().iterator();//keyset is a method  
			while(it.hasNext()) {  
				int key=(int)it.next();  
					System.out.println("Roll no.: "+key+"     name: "+hm.get(key));  
				}  
		Set<String> languages = new HashSet<>();//implements Hashset
		System.out.println("set in collections");
	    languages.add("Java");
	    languages.add("JavaScript");
	    languages.add("Python");
	    	for(String language : languages) {
	    			System.out.print(language);
	    			System.out.print("\n");
	    		}
	 ArrayList<String> list = new ArrayList<String>();
	 System.out.println("\nlist in collections");
	 list.add("sowmya");
	 list.add("keerthana");
	 list.add("sreeja");
	 	for (int i = 0; i < list.size(); i++){  
	 		//prints the elements of the List  
	 		System.out.println(list.get(i));  
	 	}  
	 	Collections.sort(list);
	 	// Let us print the sorted list
	 	System.out.println("\nList after the use of" +" Collection.sort() :\n" + list);
}
	 
	public static void main(String args[]) {
		Extensions obj=new Extensions();//object creation
		obj.eat();//calling method using object
		obj.travel();//calling method using object
		obj.demo();
	}

}
