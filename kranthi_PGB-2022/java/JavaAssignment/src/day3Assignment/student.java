package day3Assignment;


public class student extends Base implements Sinfo{
	private int rno,age;
	private String name; private String gender;
	private String lastname;

	//constructor without arguments
	 student(){

	}

	// constructer with arguments
	public student(int rno,int age,String name, String gender,String lastname){
	this.rno=rno;
	this.age=age;
	this.name=name;
	this.gender=gender;
	this.lastname=lastname;
	}
	public void setName(String Name){this.name=Name;}
	public String getName() {return name;}
	
	
	public void setRno(int Rno){this.rno=Rno;}
	public int getRno() {return rno;}


	
	public void setAge(int Age){this.age=Age;}
	public int getAge() {return age;}
	
	
	public void setGender(String Gender){this.gender=Gender;}
	public String getGender() {return gender;}
	
	
    public void setLastname(String Lastname){this.lastname=Lastname;}
    public String getLastname() {return lastname;}
    
    public void attend() {
		System.out.println("Yes I have Attended");
	}
	public void submit() {
		System.out.println("Yes I have submitted my home work");
	}
	void fun() {
		System.out.println("Yes the activity is funny");
		
	}
	public static void main(String args[]) {
		student kk=new student();
		kk.attend();
		kk.submit();
		kk.fun();
	}
    
}
