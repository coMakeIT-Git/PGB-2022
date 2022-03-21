public class patientDetails {
	String name, disease, doctorname, admissiondate;
	int age, registrationid;
	double fees; 
	public static int count = 1 ;
	
	public patientDetails(String name,int age,int registrationid,String disease,String dname,double fees,String date)
	{
		this.name = name; this.age=age; this.registrationid=registrationid;
		this.disease=disease; this.doctorname=dname;
		this.fees=fees; this.admissiondate=date;
	}
	
	public void display()
	{
	System.out.println("-------->>GIVEN DETAILS ARE SHOWN BELOW--------->>");
	System.out.println("NAME OF PATIENT IS--------"+name);
	System.out.println("AGE OF PATIENT IS--------"+age);
	System.out.println("REGISTRATION ID OF PATIENT IS--------"+registrationid);
	System.out.println("DISEASE OF PATIENT IS--------"+disease);
	System.out.println("DOCTOR APPOINTED TO PATIENT IS--------"+doctorname);
	System.out.println("TOTAL FEES OF PATIENT IS--------"+fees);
	System.out.println("DATE OF ADMISSION IS--------"+admissiondate);
	System.out.println("TOTAL PATIENT COUNT IS------->>"+count++);
	System.out.println("----------------------------------------------------------------");
	}
}
