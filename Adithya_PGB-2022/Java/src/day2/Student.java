package day2;
public class Student {

	int rollno;
	String name;
	int marks;
	int rank;
	Student(int rollno,String name,int marks,int rank){
		this.rollno=rollno;
		this.marks=marks;
		this.rank=rank;
		this.name=name;
	}
	void set(int marks,int rank){
		this.marks=marks;
		this.rank=rank;
	}
	void get(int rollno){
		System.out.println(marks+" "+rank);
	}
	public boolean equals(Object obj){
		if(this==obj){
			return true;
		}
		if(obj==null||obj.getClass()!=this.getClass()){
			return false;
		}
		Student o=(Student)obj; 
		System.out.println(o.rollno+" "+o.name+" "+o.marks+" "+o.rank);
		return (o.rollno==this.rollno)&&(o.name.equals(name))&&(o.marks==this.marks)&&(o.rank==this.rank);
	}
	void print(String name){
		if(this.name==name)
		System.out.println(this.marks+" "+this.rank);
	}
	void print(int rollno){
		if(this.rollno==rollno)
		System.out.println(this.marks+" "+this.rank);
	}
	public int hashCode(){
		return 31*this.rollno*this.name.hashCode();
	}
	public static void main(String[] args) {
		Student a=new Student(5,"adithya",25,1);
		Student b=new Student(14,"srinivas",20,2);
		a.print(5);
		a.print("adithya");
		a.set(31, 1);
		Student c=new Student(5,"adithya",31,1);
		System.out.println("both objects are equal "+a.equals(b));
		System.out.println("both objects are equal "+a.equals(c));
	}

}