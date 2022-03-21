package office;

import java.util.*;

interface department {
	void ICT_department();
	void HR_department();
	void DEVOPS();
    void SW();
}
abstract class employ implements department {

	// Overriding the methods
	@Override public void ICT_department()
	{
		System.out.println("Hi, this is ICT department");
	}
	@Override public void DEVOPS()
	{
		System.out.println(
			"Hi, this is DEVOPS");
	}
    @Override public void SW(){
        System.out.println(" software development team in employ class");
    }
}

class employee extends employ {
	@Override public void HR_department()
	{
		System.out.println(
			"Hi, this is HR department");
	}
    @Override public void SW(){
        System.out.println("Hi, this is software development team");
    }
}
class details {
    private String office_name;
    private String idNum;
    
    List<dept> departments=new ArrayList<dept>();
 
    public String getName() {
       return office_name;
    }
 
    public String getIdNum() {
       return idNum;
    }
    public void setdepartments(List<dept> l1)
    {
        this.departments=l1;
    }
    public List<dept> getdepartments()
    {
        return this.departments;
    }
      
    public void setName(String newName) {
       office_name = newName;
    }
 
    public void setIdNum( String newId) {
       idNum = newId;
    }
 }
 class dept{
     private String dept_name;
     public String getdept_name(){
         return dept_name;
     }
     public void set_deptname(String newName) {
        dept_name = newName;
     }
 }
public class Office {
	public static void main(String[] args)
	{
	
		employee e = new employee();
        employ em = new employee(); //overriding
		e.ICT_department();
		e.DEVOPS();
		e.HR_department();
        em.SW();
        details d=new details();
        d.setName("coMakeIT");
        d.setIdNum("CMI-T1080");
        dept de1=new dept();
        de1.set_deptname("Software developer");
        dept de2=new dept();
        de2.set_deptname("Software developer");
        List<dept> l=new ArrayList<dept>();
        l.add(de1);
        l.add(de2);
        d.setdepartments(l);
        List<dept> l2=new ArrayList<dept>();
        l2=d.getdepartments();
        System.out.println("NUmber of departments in office is :" + l2.size()); //
        // association in main class using the dept and details classes
        System.out.println("Office Name : " + d.getName() + "    employ id num : " + d.getIdNum() + "    department is : " + de1.getdept_name());
	}
}
