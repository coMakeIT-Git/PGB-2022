package Day2Assignment.Task;
public class Student {
	  private int stid;
	  private String stname;
	  private int stage;
	  Student()
	  {
		  System.out.println("This is Default COnstructor!!!");
	  }
	public Student(int stid, String stname, int stage) {
		System.out.println("This is Parameterized Constructor!!!");
		this.stid = stid;
		this.stname = stname;
		this.stage = stage;
	}
	public int getStid() {
		return stid;
	}
	public void setStid(int stid) {
		this.stid = stid;
	}
	public String getStname() {
		return stname;
	}
	public void setStname(String stname) {
		this.stname = stname;
	}
	public int getStage() {
		return stage;
	}
	public void setStage(int stage) {
		this.stage = stage;
	}
	@Override
	public boolean equals(Object obj)
	{
		if(obj==this) return true;
		if(obj==null || obj.getClass()!=this.getClass()) return false;
		Student sobj=(Student) obj;
		return (sobj.stname.equals(stname) && sobj.stid==stid && sobj.stage==stage);
	}
	public int hashcode()
	{
		return this.stid*this.stname.hashCode();
	}
	public void display(int stid) {
		System.out.println("Student Id is:" +stid);
	}
	public void display(int stid,String stname)
	{
		System.out.println("Student Id is:" +stid +"Student Name is:"+stname);
	}



	public static void main(String args[])
	{
		Student s1=new Student(01,"Akhil",21);
		Student s2=new Student(02,"Nithish",18);
		Student s3=new Student(01,"Akhil",21);
		Student object=new Student();
		System.out.print("Comparing two objects");
		System.out.println("Comparing s1 and s2 objects"+" "+s1.equals(s2));
		System.out.println("Comparing s2 and s3 objects"+" "+s2.equals(s3));
		System.out.println("Comparing s3 and s1 objects"+" "+s3.equals(s1));
		System.out.println("Printing HashCodes Of every Objects");
		System.out.println(s1.hashcode()+" "+s2.hashcode()+" "+ s3.hashcode());
	    object.display(s1.getStid());
	    object.display(s1.getStid(),s1.getStname());
	}
}