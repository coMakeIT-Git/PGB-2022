
public class collectDetails extends hospitalStaff {
		public collectDetails ( String name, int age, String gender, int id, String
		designation, double salary, String attendence)
		{
			this.name=name; this.age=age; this.gender=gender; this.id=id;
			this.designation=designation; this.salary=salary;
			this.attendence=attendence;
		}
		public void StaffDetailsDisplay()
		{
		System.out.println("FULL NAME OF STAFF IS------"+name);
		System.out.println("AGE OF STAFF IS------------"+age);
		System.out.println("GENDER OF STAFF IS----------"+gender);
		System.out.println("ID OF STAFF IS---------------"+id);
		System.out.println("STAFF DESIGNATION IS ----------"+designation);
		System.out.println("SALARY OF STAFF IS------------------"+salary);
		System.out.println("CURRENT OR TODAY STAFF ATTENDANCE IS---------"+attendence);
		System.out.println("TOTAL COUNT OF STAFF IS-------------------"+StaffCount++);
		
		}
}
