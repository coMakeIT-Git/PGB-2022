package day2;
public class student {
	int id;
	String name;
	
	student(){
	
	}
	student(int id,String name)
	{
		this.id=id;
		this.name=name;
		
	}
	private int number;
	public int getnumber() {
		return number;
	}
	public void setnumber(int n) {
		this.number=n;
	}
	// equals override
	@Override
	public boolean equals(Object obj){
		
		if(this == obj)
			return true;
	if(obj==null || obj.getClass()!=this.getClass())
		return false;
	student stud=(student) obj;
	return(stud.name.equals(this.name)&& stud.id == this.id && stud.getnumber() == this.number);
	}

	public int hashcode()
	{
		return (this.id * this.name.hashCode());
	}
	//method overloading
	void record(int id) {
		System.out.println("Student Id (overloading 1):"+id);
	}
	void record(int id,int number) {
		System.out.println("Student Id (overloading 2):"+id);
		System.out.println("Student number (overloading 2):"+number);
	}
	public static void main(String[]args) {
		student s1= new student (1,"student1");
		s1.setnumber(123);
		System.out.println("Student number using getumber ():"+s1.getnumber());
		student s2= new student(1,"student1");
		s2.setnumber(123);
		//equals check
		System.out.println("Student equals (override):"+s1.equals(s2));
		student s3= new student(1,"student2");
		s3.setnumber(123);
		System.out.println("Student equals (override):"+s1.equals(s3));
		//hash code check
		System.out.println("hashcode of s1:"+s1.hashcode()+"\nhashcode of s2:"+s2.hashcode());
		s1.record(3);
		s1.record(4,145);
	}
}


