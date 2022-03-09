package comakeit;

import java.util.*;
import java.util.Map.Entry;

public class Collections {
	public static void main(String[] args) {
		
		Main m2= new Main(101,"sai2");
		Main m3= new Main(102,"sai3");
		Main m4= new Main(103,"sai4");
		Main m5= new Main(104,"sai5");
		
		//collections list, set and map of objects from concrete class
		List<Main>id= new ArrayList<Main>();
		id.add(m2);
		id.add(m3);
		id.add(m4);
	
		Set<Main>name=new HashSet<Main>();
		name.add(m3);
		name.add(m4);
		name.add(m5);
		
		
		Map<String,Main>code = new HashMap<>();
		code.put("SCE100",m2);
		code.put("SCE101",m3);
		code.put("SCE102",m4);
		code.put("SCE103",m5);
		
		//Iterate and print list 
		for(Main i:id) {
			System.out.println("Student Id: "+i.id);
		}
		
		//Iterate and print set
		for(Main s:name) {
			System.out.println("Student Name: "+s.name);
		}
		
		//Iterate and print map
		for(Entry<String, Main> entry:code.entrySet()) {
			String key=entry.getKey();
			Main value=entry.getValue();
			System.out.println("college code: "+key+", college id: "+value.id);
			
		}
		
		// Stream to iterate the list
        System.out.println("****Printing List using Stream****");
        id.stream().forEach((a)->System.out.println("Name : "+a.name+", ID : "+a.id));
		
	}

}
