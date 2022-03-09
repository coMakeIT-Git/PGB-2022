package day3;
import java.util.*;
//Creating Interface
interface Person{
	//Declaring 2 methods in interface
	void eat();
	void sleep();
}
//Adding an abstract class
abstract class underGraduate implements Person{
	abstract void study();
	//Add method with definition in abstract class
	void learn() {
		System.out.println("Learning");
	}
}
//Implements methods of Interface class and Override the methods of abstract Class in concrete class in concrete class
class Student extends underGraduate implements Person{
	int id;
	String name;
	Student(int id,String name){
		this.id=id;
		this.name=name;
	}
	@Override
	public void eat() {
		System.out.println("eating");
	}
	@Override
	public void sleep() {
		System.out.println("Sleeping");
	}
	@Override
	void study() {
		System.out.println("Studying");
	}
	public static void main(String[] args) {
		// creating objects of concrete class
		Student st = new Student(2, "Adithya");
		//Access the Abstract class methods
		System.out.println("Accessing Abstract Class Methods");
		st.learn();
		//Access the Concrete class methods
		System.out.println("\nAccessing Concrete Class Methods");
		st.eat();
		st.sleep();
		st.study();
		//collections list, set and map of objects from concrete class
		HashMap<Student,String>hm=new HashMap();
		List<Student>l=new LinkedList();
		Set<Student>s=new HashSet();
		int[]id= {10,11,12,13,14};
		String[]name= {"akhil","Dheeraj","Balaji","kiran","ravi"};
		String[]colours= {"red","blue","green","yellow","orange"};
		for(int i=0;i<5;i++) {
			l.add(new Student(id[i],name[i]));
		}
		System.out.println("\nList output");
		for(Student stu:l) {
			System.out.println(stu.id+" "+stu.name);
		}
		for(int i=0;i<5;i++) {
			s.add(new Student(id[i],name[i]));
		}
		System.out.println("\nSet output");
		for(Student stu:s) {
			System.out.println(stu.id+" "+stu.name);
		}
		for(int i=0;i<5;i++) {
			hm.put(new Student(id[i],name[i]), colours[i]);
		}
		System.out.println("\nMap output");
		for(Map.Entry<Student, String>f:hm.entrySet()) {
			System.out.println(f.getKey().id+" "+f.getKey().name);
		}
		//Sort the collections of list 
		Collections.sort(l,new Comparator<Student>(){
			public int compare(Student a,Student b){
				return b.id-a.id;
			}
		});
		System.out.println("\nSorted output");
		for(Student stu:l) {
			System.out.println(stu.id+" "+stu.name);
		}
		//java stream to iterate
		System.out.println("\nStream output");
		l.stream().forEach((c)->System.out.println(c.id+" "+c.name));
	}
}