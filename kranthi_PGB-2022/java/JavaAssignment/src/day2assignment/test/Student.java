package day2assignment.test;

public class Student {
	private int rno,age;
	private String name; private String gender;

	//constructor without arguments
	 Student(){

	}

	// constructer with arguments
	public Student(int rno,int age,String name, String gender){
	this.rno=rno;
	this.age=age;
	this.name=name;
	this.gender=gender;
	}
	public void setName(String Name){this.name=Name;}
	public String getName() {return name;}
	public void setRno(int Rno){this.rno=Rno;}
	public int getRno() {return rno;}
	public void setAge(int Age){this.age=Age;}
	public int getAge() {return age;}
	public void setGender(String Gender){this.gender=Gender;}
	public String getGender() {return gender;}
	
	public boolean equals(String name,int rno,int age) {
		if(name!=this.name||rno!=this.rno||age!=this.age) {
			return false;
		}
		else {return true;}
	}
	public int hashcode() {
		return this.rno;
	}
public static void override(String name,int rno) {
		System.out.println("NAme is:"+name+"Roll no is:"+rno);
	}
	public static void override(String name,int rno,int age) {
		System.out.println("NAme is:"+name+"Roll no is:"+rno+"Age is :"+age);
	}
}