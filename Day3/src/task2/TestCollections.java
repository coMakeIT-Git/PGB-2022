package task2;
import java.util.*;

public class TestCollections {
	 
	public static void main(String[] args)
	{
		List<String> list =new ArrayList<String>(); //List
	    
	   list.add("EmpOne");
		list.add("EmpTwo");
		list.add("EmpThree");
		
		System.out.println("List without sorting");
		
		for(String x : list)
		{
			System.out.println(x);
		}
		
		Collections.sort(list);
		
		System.out.println("After sorting, the list is");
		
		for(String x: list)
		{
			System.out.println(x);
		}
		
		
		Set<String> data= new LinkedHashSet<String>();
		data.add("Emp1");
		data.add("Emp2");
		data.add("Emp3");
		
		System.out.println("Collection set is");
		
		for(String a : data)
		{
			System.out.println(a);
		}
		
		Map<Integer,String> m= new HashMap<Integer,String>();
		m.put(1, "Ram");
		m.put(5,"Amit");
		m.put(6, "Pavani");
		m.put(2, "Kiran");
		
		System.out.println("Collection map is");
		//Elements traverse 
		
		for(Map.Entry ma:m.entrySet())
		{
			System.out.println(ma.getKey() + " "+ ma.getValue());
		}
		
		//List iteration through stream
		System.out.println("List iteration through stream");
		
		list.stream().forEach((temp) -> System.out.println(temp));
	}

}
