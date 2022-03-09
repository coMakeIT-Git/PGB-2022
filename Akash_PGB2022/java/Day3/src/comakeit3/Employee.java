package comakeit3;

import java.util.*;
import java.util.Map.Entry;

//interface class
interface Employee {
	
	//methods in interface
	public int employeeid1(int id);
	public String employeename1(String name);

}

//abstract class
abstract class Company{
	
	//method in abstract
	public void companyname() {
		System.out.println("company Name: cmit");
	}
}

//Override and Implements methods in concrete class
class Main extends Company implements Employee{

	int id;
	String name;
	
	public Main(int id, String name) {
		this.id = id;
		this.name = name;
	}

	@Override
	public int employeeid1(int id) {
		return id;
	}

	@Override
	public String employeename1(String name) {
		return name;
	}

	//Concrete method
	public String companycode(String code) {
		return code;
	}
	
	public static void main(String[] args) {
		
		//objects of concrete class
		Main m1= new Main(100,"akash");
		
		System.out.println("Employee ID: "+m1.employeeid1(100));
		System.out.println("Employee name: "+m1.employeename1("akash"));
		
		//Access the Concrete class methods
		System.out.println("College code: "+m1.companycode("SCE1059"));
				
		//Access the Abstract class methods
		m1.companyname();
		
		Main m2= new Main(101,"a1");
		Main m3= new Main(102,"a2");
		Main m4= new Main(103,"a3");
		Main m5= new Main(104,"a4");
		
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
		code.put("cmit100",m2);
		code.put("cmit101",m3);
		code.put("cmit102",m4);
		code.put("cmit103",m5);
		
		//Iterate and print list 
		for(Main i:id) {
			System.out.println("Employee Id: "+i.id);
		}
		
		//Iterate and print set
		for(Main s:name) {
			System.out.println("Employee Name: "+s.name);
		}
		
		//Iterate and print map
		for(Entry<String, Main> entry:code.entrySet()) {
			String key=entry.getKey();
			Main value=entry.getValue();
			System.out.println("company code: "+key+", company id: "+value.id);
			
		}
		
		// Stream to iterate the list
        System.out.println("****Printing List using Stream****");
        id.stream().forEach((a)->System.out.println("Name : "+a.name+", Id : "+a.id));
		
	}
	}
	



