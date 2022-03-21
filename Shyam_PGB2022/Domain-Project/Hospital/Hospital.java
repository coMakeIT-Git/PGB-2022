import java.util.*;
public class Hospital extends doctorsRole{
	public static medicineTypes med;
	public doctorsRole job;	   
    public Hospital(){
        this.offices = null;
		this.job=new doctorsRole();
        job.setSalary(1000L);
        job.setRole("Cardiologist");
	    }
    public long getSalary() {
        return job.getSalary();
    }
    public String getRole() {
        return job.getRole();
    }
    String name;
    private final List<Branches> offices; 
    public Hospital(String name, List<Branches> offices)    
    {    
        this.name = name;  
        this.offices = offices;    
    } 
    public List<Branches> getTotalOfficesOfCompany()     
    {     
        return offices;     
    }     
	public static void main(String[] args) {
	Scanner object = new Scanner(System.in);
	Branches o1 = new Branches("WAHH-Main","F.No: 504, Banglore");     
    Branches o2 = new Branches("WAHH-Cardio","F.No: 1-24-35, Gurgaon");  
    Branches o3 = new Branches("WAHH-Ortho", "F.No: 50-6-76, Hyderabad");  
        List<Branches> offices = new ArrayList<Branches>();     
        offices.add(o1);     
        offices.add(o2);     
        offices.add(o3);    
        Hospital company = new Hospital("We Are Here Hospitals ", offices);   
        System.out.println("//PRINCIPLE OF COMPOSITION IS ACHIEVED HERE "); 
        System.out.println("//If we delete the list of office then the entries of its branch details are also deleted(tightly-packed). ");  
        System.out.println(company.name+"Branches: ");  
        List<Branches> data = company.getTotalOfficesOfCompany();  
 
        for (Branches office : data) {     
   
                System.out.println("Name : " + office.name + " and its "+ " Address : " + office.address);    
        } 
	int choice; int t=1;
	System.out.println("--------------------------------------------------");
	System.out.println("-->>HOSPITAL-->>");
	System.out.println("---------------------------------------------------");
	do {
	System.out.println("---------CHOOSE YOUR SPECIFIC OPERATION (Give Input:[1-6])---------");
	System.out.println("1.) ACCESS THE PATIENT DB-------(PRINCIPLE OF ASSOCIATION IS ACHEIVED HERE)");
	System.out.println("	//ie..,Hospital is associated with all the patients information.");
	System.out.println("2.) ACCESS THE STAFF DB-------(PRINCIPLE OF ABSTRACTION IS ACHIEVED HERE)");
	System.out.println("	//ie..,Staff details are abstracted and implemented in other class. ");
	System.out.println("3.) CHECK FACILITIES------------(PRINICIPLE OF INHERITENCE IS ACHIEVED HERE)");
	System.out.println("	//ie..,Phone Numbers methods is inherited from parent. ");
	System.out.println("4.) BOOK AMBULANCE-------------(PRINCIPLE OF POLYMORPHISM IS ACHIEVED HERE");
	System.out.println("	//ie..,If color is white, the AMBULANCE is to Hospital else to Mortuary. ");
	System.out.println("5.) CHECK FOR NEW JOBS---------(PRINCIPLE OF ENCAPSULATION IS ACHIEVED HERE)");
	System.out.println("	//ie..,The salary is disclosed and viewed to only the active users ");
	System.out.println("6.) MEDICINE DETAILS-----------(PRINCIPLE OF AGGREGATION IS ACHIEVED HERE)");
	System.out.println("	//ie..,Here both the Hospital and the Medicines are independent(loosely-packed) ");
	choice = object.nextInt();
	switch (choice)
	{
	case 1:
	patientDetails d1 = new patientDetails("PRAVEEN",34,23456,"FEVER","DR.KALYAN",4547.32,"11-MAR-2020");
	patientDetails d2 = new patientDetails("SHYAM",45,23457,"PAIN","DR.REVANTH",4589.32,"11-MAR-2020");
	d1.display();
	d2.display();
	break;
	case 2:
	collectDetails t1 = new collectDetails("MR.VAMSHI",21,"MALE",12345,"DOCTOR", 50000.20,"PRESENT");
	collectDetails t2 = new collectDetails("MR.RAKESH",23,"MALE",12349,"SURGEON",60000.20,"PRESENT");
	t1.StaffDetailsDisplay();
	t2.StaffDetailsDisplay();
	break;
	case 3:
	facilitiesAvailable f1 = new facilitiesAvailable("MEDICAL",2000.00,123 );
	f1.display();
	f1.PrintDetails();
	facilitiesAvailable f2 = new facilitiesAvailable("AMBULANCE",1000.00,456);
	f2.display();
	f2.PrintDetails();
	facilitiesAvailable f3 = new facilitiesAvailable("LABORATORY",5000.00,789);
	f3.display();
	f3.PrintDetails();
	facilitiesAvailable f4 = new facilitiesAvailable("CANTEEN",500.00,1022);
	f4.display();
	f4.PrintDetails();
	break;
	case 4:
	String color;
	object.nextLine();
	System.out.println("Enter Vehicle Color (White/Black)");
	color = object.nextLine();
	if (color.equals("White")) {
	ambulanceBookings a1 = new ambulanceBookings();
	a1.TakeDetails();
	a1.PrintDetails();
	}
	else {
		patientDead d = new patientDead();
		d.TakeDetails();
		d.PrintDetails();
		}
	break;
	case 5:
		Hospital person = new Hospital();
		System.out.println("The Available Role is: "+person.getRole());
        System.out.println("Salary: "+person.getSalary());
        break;
	case 6:
		med = new medicineTypes("Homeopathy", "6 years", "Capsules");
		med.display();
		break;
		
        
	default:
	System.out.println("------END-----");
	}
	System.out.println("-----DO YOU WANT TO CONTINUE PRESS 1 FOR YES AND OTHER KEY FOR NO------");
	t = object.nextInt();
	} while (t==1);
	object.close();
	}
}
