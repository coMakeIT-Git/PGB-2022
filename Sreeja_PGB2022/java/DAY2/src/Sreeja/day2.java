package Sreeja;
import java.util.*;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class day2 {
	private String name;
	private int id;
	public void day2() {
	System.out.println("default");
}
public void day2(String name,int id) {
	System.out.println("name:"+ name+"id:"+id);
}	
	public String getName() {
		return name;
	}
	public void setName(String N) {
		this.name=N;
	}
	
	public boolean equals(Object o) {
		if(this==o) {
			return true;
		}
	
		if(o==null||o.getClass()!=this.getClass()) {
			return false;
		}
		
			day2 d2=(day2)o;
			return (d2.name==this.name && d2.id==this.id);
			
		}
		public int hashCode(){
			return this.id;
		}
		
}

class task2{
public static void main(String args[]) {
	day2 d1=new day2();
	day2 d2=new day2();
	d1.day2();
	d1.day2("sreeja",1080);
	d2.day2("sreeja",1080);
	d1.setName("SREEJA");
	System.out.println(d1.getName());
	System.out.println(d1.equals(d2));
	Set<day2>hashSet=new HashSet<>();
	hashSet.add(d1);
	hashSet.add(d2);
	System.out.println("Hash elements:"+hashSet);
	Map<day2,String> hashMap=new HashMap<>();
	hashMap.put(d1,"first");
	hashMap.put(d2,"second");
	System.out.println("Hash  map elements:"+hashMap);
	
	
	}
}
