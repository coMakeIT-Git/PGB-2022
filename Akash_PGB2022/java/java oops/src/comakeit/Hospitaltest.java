package comakeit;

public class Hospitaltest {
	
	public static void main(String[] args) {
		Apollo a= new Apollo("Varun","ENT",15);
		Yashoda y= new Yashoda("Praveen","surgeon",17);
		
		Patient p=new Patient("kumar",58,"hearing");
		Patient p1=new Patient("kiran",32,"fracture");
		a.appointment();
		a.display(p);
		a.treatment();
		System.out.println("*************");
		y.appointment();
		y.display(p1);
		y.treatment();
			
	}
	
}
