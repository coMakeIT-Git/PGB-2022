public class student{
	private String name;
	private int rollno;
	private int marks;
	public student(){
		name="nithish";
		rollno=1;
		marks=60;
	}
	public student(String name,int rollno,int marks){
		this.name=name;
		this.rollno=rollno;
		this.marks=marks;
	}
	public void setname(String name){
		this.name=name;
	}
	public void getname(){
		System.out.println(name);
	}
	public void setmarks(int marks){
		this.marks=marks;
	}
	public void getmarks(){
		System.out.println(marks);
	}
	public void setrollno(int rollno){
		this.rollno=rollno;
	}
	public void getrollno(){
		System.out.println(rollno);
	}
	
	public boolean equals(String name,int rollno,int marks) {
		if(name!=this.name || rollno!=this.rollno || marks!=this.marks) {
			return false;
		}
		else {
			return true;
		}
	}
	
	public int hashcode(){
		return this.rollno;
	}
	
	public void overload(String name,int rollno) {
		System.out.println("name is:"+name+"rollno:"+rollno);
	}
	public void overload(String name,int rollno,int marks) {
		System.out.println("name is:"+name+"rollno:"+rollno+"marks:"+marks);
	}
	
}