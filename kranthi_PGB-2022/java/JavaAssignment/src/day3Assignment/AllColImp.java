package day3Assignment;
import java.util.*;
public class AllColImp {
	public static void main(String[] args)
    {
		student s1=new student(2,22,"ravi","male","baga");
		student s2=new student(4,22,"rithu","female","Inty");
		student s3=new student(1,22,"krishnaveni","female","thota");
		student s4=new student(3,22,"Madhu","male","mata");
		
  
        //List implementation
        ArrayList<String> al = new ArrayList<String>();
        al.add(s1.getName());
        al.add(s2.getName());
        al.add(s3.getName());
        al.add(s4.getName());
        
        
  System.out.println("Befor Sorting");
        System.out.println(al);
        Collections.sort(al);
        
  System.out.println("After Sorting");
  for (int i = 0; i < al.size(); i++)
      System.out.print(al.get(i) + " ");
  System.out.println("");
  
  //Map Implementation
       Map<Integer,String> mk=new HashMap<Integer,String>();
        mk.put(1,s1.getName());
        mk.put(2,s2.getName());
        mk.put(3,s3.getName());
        mk.put(4,s4.getName());
        System.out.println(mk);
        
        HashSet<String> hs = new HashSet<String>();
        
        hs.add(s1.getLastname());
        hs.add(s2.getLastname());
        hs.add(s3.getLastname());
        
        hs.add(s4.getLastname());
        
        
  
        // Traversing elements
        Iterator<String> itr = hs.iterator();
        while (itr.hasNext()) {
            System.out.println(itr.next());
        }
        
  
        
       
    }

}