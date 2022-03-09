package day2Assignment.test;
public class Student{
	private String name;
	private int id;
	private int marks;
	public Student(){
	}
	public Student(int id,String name,int marks){
		this.name=name;
		this.id=id;
		this.marks=marks;
	}
	public void setname(String name){
		this.name=name;
	}
	public String getname(){
		return name;
	}
	public void setmarks(int marks){
		this.marks=marks;
	}
	public int getmarks(){
		return marks;
	}
	public void setid(int id){
		this.id=id;
	}
	public int getid(){
		return id;
	}
	
	public boolean equals(Object x) {
		if(x==null || x.getClass()!=this.getClass() ) {
			return false;
		}
		final Student y=(Student)x;
		if(y.getname()!=this.getname() || y.getid()!=this.getid() || y.getmarks()!=this.getmarks()) {
			return false;
		}
		return true;
	}
	
	public int hashcode(){
		return this.id;
	}
	
	public void overload(int id,String name) {
		System.out.println("name is: "+name+" rollno: "+id);
	}
	public void overload(int id,String name,int marks) {
		System.out.println("name is: "+name+" id: "+id+" marks: "+marks);
	}
	
}
