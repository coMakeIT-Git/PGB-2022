package saikeerthana;
import java.util.*;
abstract class AbstractDemo
{ 
	abstract void demo();
	void display()
	{
		System.out.println("Display method  is shown");
	}
	
}
interface Animalinterfacedemo {
	   public void eat();
	   public void travel();
	}
public class Extensions extends AbstractDemo implements Animalinterfacedemo{
	public int id;
	@Override
	public void eat() {
		System.out.println("interface implements eat method");
	}

	@Override
	public void travel() {
		System.out.println("interface implements travel method");
		
	}

	@Override
	void demo() {
		System.out.println("extensions override demo method");
		
	}
	Extensions()
	{
	    List < String > myList = new ArrayList < String > ();
	    myList.add("W");
	    myList.add("T");
	    myList.add("A");
	    myList.add("G");
	    myList.add("I");
	    myList.add("B");
	    myList.add("Z");
	    myList.add("0");
	    myList.add("U");
	    myList.add("7");
	    System.out.println("The unsorted List is:");
	    for (String myStr: myList) {
	      System.out.print(" " + myStr);
	    }
	    Collections.sort(myList);
	    System.out.println("\nThe Sorted List is");
	    for (String myStr: myList) {
	      System.out.print(" " + myStr);
	    }
	    Map<Integer,String> map=new HashMap<Integer,String>();  
	    map.put(100,"Amit");  
	    map.put(101,"Vijay");  
	    map.put(102,"Rahul");  
	    System.out.println("\nHashmap elements are:");
	    for(Map.Entry m:map.entrySet()){  
	     System.out.println(m.getKey()+" "+m.getValue());  
	    }  
	    HashSet<String> hs= new HashSet<String>();  
	    hs.add("India");  
	    hs.add("America");  
	    hs.add("Russia");  
	    hs.add("China");  
	    Iterator it=hs.iterator();                    //add an iterator to hs  
	    System.out.println("Elements using iterator:");  
	    while(it.hasNext())                          //display elements by using iterator  
	    {  
	    String s=(String)it.next();  
	    System.out.println(s);  
	    }  
	}
	
	public static void main(String[] args)
	{
		
		Extensions ex=new Extensions();
		ex.demo();
		ex.display();
		ex.eat();
		ex.travel();
	}
}

