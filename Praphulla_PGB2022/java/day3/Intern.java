import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.Map;
import java.util.Set;
interface Resources
{
    void learnCoding();
    void materials();
    void publicContribution();
}
  
abstract class Employee implements Resources
{
  
    // Overriding the methods of the interface with our own implementation

	public void learnCoding()
	{
	System.out.println("Learn to code with us.");
	}
	   	 
        @Override
    	 public void materials()
  	 {
          System.out.println("Refer the following links to access the materials.");
   	 }
   	 
	String Name;
	int id;
	abstract void message();
	
	public String getName() 
		{
		return Name;
		}
		
	public void setName(String Name)
		{
		this.Name=getName();
		}

	public void printDetails()
		{
		    System.out.println("details"+getName());
		}
}
  
// Extending the Employee class
class Intern extends Employee implements Resources, Comparable<Intern>
{
    @Override 
    public void publicContribution()
	    {
		System.out.println("You can add your contributions to the public pool.");
	    }
    void message()
	    {
		System.out.println("Hello!!");
	    }
    String iname;
    int id;
    // constructor
    Intern()
	    {
	    	System.out.println("welcome to the concreate class Intern! that extends class Employee and implements interface Resources");
	    }
    // parameterised constructor      
    Intern(String iname, int id) 
	    {       
		this.iname = iname;
		this.id = id;
		System.out.println(" The name of the  Intern employee is: "+"\t" +iname); 
		System.out.println(" The name of the  Intern employee is: "+"\t" +id); 
	    }
	    
    public String getInternName()
	    {
	    	return this.iname;
	    }
    public void setInternName(String iname)
	    {
	    this.iname = iname;
	    }
    
    public int getInternId()
	    {
	    	return this.id;
	    }
    public void setInternId(int id)
	    {
	    this.id = id;	
	    }
    public int compareTo(Intern intern)
	    {
	     int c=((Intern)intern).getInternId();
	     return this.getInternId() - c;
	    }
public static void main(String args[])
{
       
       Intern i = new Intern();
       i.message();
       System.out.println("Hey, How are you?");
       i.learnCoding();
       i.materials();
       i.publicContribution();
       
       // object for setting names
        Intern i1=new Intern("Praphulla",10);
        i1.setInternName("Dolly");
        i1.setInternId(53);
        
        Intern i2=new Intern("Shyam",20);
        i2.setInternName("Shawty");
        i2.setInternId(58);
        
        Intern i3=new Intern("Chaitra",30);
        i3.setInternName("Raphy");
        i3.setInternId(51);

        // array list
        ArrayList<Intern> IDs=new ArrayList<Intern>();
		IDs.add(i1);
		IDs.add(i2);
		IDs.add(i3);
		
		//sorting the arraylist
		System.out.println("\nSorting interns using their Intern ids:");
		Collections.sort(IDs);
		for(Intern intern : IDs) 
			{
			System.out.println(intern.getInternId() + "\t" + intern.getInternName());
			}
	List<String> myList = new ArrayList<String>();
        List<Integer> list = Arrays.asList(2, 4, 6, 8, 10);
        System.out.println("Adding elements to a List");
        // Adding elements to the List
        myList.add("praph");
        myList.add("raphy");
        myList.add("luna");
        myList.add("dolly");
        Iterator<String> it = myList.iterator();
        System.out.println("Printing the values of a List using Iterator");
        while (it.hasNext())
         {
            // Print all elements of List
            System.out.println(it.next());
         }
        System.out.println("Printing the values of a List using ListIterator");
        ListIterator<String> it1 = myList.listIterator();
        while (it1.hasNext())
         {
            // Print all elements of List
            System.out.println(it1.next());
        }
        System.out.println("Performing sorting using sort method");
        Collections.sort(myList);
        // printing the sorted list
        System.out.println("List after the use of" +
                           " Collection.sort() :\n" + myList);
        // Using java stream forEach  to iterate
        System.out.println("Iterating list elements using java streams:");
        list.stream().sorted(Comparator.reverseOrder()).forEach(System.out::println);
		//set
		 Set<Intern> setid = new HashSet<Intern>();
		 setid.add(i1);
		 setid.add(i2);
		 setid.add(i3);
		 System.out.println("Set: " + setid);
		 // iterating set
			 Iterator value = setid.iterator();
		     System.out.println("set iteration values are: ");
		        // printing the values of the list using a loop
		     while (value.hasNext()) 
		        {
		            System.out.println(value.next());
		        }
	        // map
	        System.out.println("Adding elements to a Map");
	        Map<String,String> map = new HashMap<String,String>();
	        map.put("Praphulla", "53");
	        map.put("Ronnie", "43");
	        map.put("Claire", "46");
	        map.put("queenie", "57");
	        System.out.println("Printing the values of a map using for loop");
	        // iterating elemnets in the map using for loop.
		        for (Map.Entry<String,String> entry : map.entrySet())
		            System.out.println("Key = " + entry.getKey() +
		                             ", Value = " + entry.getValue());
		    // iterating a map using a Iterator
	        System.out.println("Printing the values of a map using Iterator");

	        Iterator<Map.Entry<String, String>> itr = map.entrySet().iterator();
		        while(itr.hasNext())
		        {
		        Map.Entry<String, String> entry = itr.next();
		        System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
	        }
} 
}
