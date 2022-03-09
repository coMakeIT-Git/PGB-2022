package comakeit;

//interface class
interface Student {
	
	//methods in interface
	public int studentid(int id);
	public String studentname(String name);

}

//abstract class
abstract class College{
	
	//method in abstract
	public void collegename() {
		System.out.println("College Name: SCE");
	}
}

//Override and Implements methods in concrete class
class Main extends College implements Student{

	int id;
	String name;
	
	public Main(int id, String name) {
		this.id = id;
		this.name = name;
	}

	@Override
	public int studentid(int id) {
		return id;
	}

	@Override
	public String studentname(String name) {
		return name;
	}

	//Concrete method
	public String collogecode(String code) {
		return code;
	}
	
	public static void main(String[] args) {
		
		//objects of concrete class
		Main m1= new Main(100,"sai1");
		
		System.out.println("Student ID: "+m1.studentid(100));
		System.out.println("Student name: "+m1.studentname("Sai"));
		
		//Access the Concrete class methods
		System.out.println("College code: "+m1.collogecode("SCE1060"));
				
		//Access the Abstract class methods
		m1.collegename();
	}
	
}

