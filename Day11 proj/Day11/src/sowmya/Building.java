package sowmya;
import java.util.*;

interface planning {
	void Basement();
	void Structure();
	void Roof();
}
abstract class type implements planning{

	// Overriding the methods
	@Override public void Basement()
	{
		System.out.println("Basement designed");
	}
    @Override public void Roof(){
        System.out.println("Roof designed in type class");
    }
}

class buildingtype extends type{
	@Override public void Structure()
	{
		System.out.println("Structure designed");
	}
    @Override public void Roof(){
        System.out.println("roof designed");
    }
}
class details2 {
    private String building_name;
    private String bNum;
    
    List<plan> plannings=new ArrayList<plan>();
 
    public String getName() {
       return building_name;
    }
 
    public String getNum() {
       return bNum;
    }
    public void setplannings(List<plan> l1)
    {
        this.plannings=l1;
    }
    public List<plan> getplannings()
    {
        return this.plannings;
    }
      
    public void setName(String newName) {
       building_name = newName;
    }
 
    public void setNum( String newNum) {
       bNum = newNum;
    }
 }
 class plan{
     private String plan_design;
     public String getplan_design(){
         return plan_design;
     }
     public void set_plandesign(String newName) {
        plan_design = newName;
     }
 }
public class Building{
	public static void main(String[] args)
	{
	
		buildingtype e = new buildingtype();
        type em = new buildingtype(); //overriding
		e.Basement();
		e.Roof();
		e.Structure();
        details2 d=new details2();
        d.setName("Aurobindo Galaxy");
        d.setNum("23");
        plan de1=new plan();
        de1.set_plandesign("coMakeIT");
        plan de2=new plan();
        de2.set_plandesign("vertafore");
        List<plan> l=new ArrayList<plan>();
        l.add(de1);
        l.add(de2);
        d.setplannings(l);
        List<plan> l2=new ArrayList<plan>();
        l2=d.getplannings();
        System.out.println("Number of office's in the building:" + l2.size()); //
        // association in main class using the dept and details classes
        System.out.println("Building Name : " + d.getName() + "    No.of floors: " + d.getNum() + "    company : " + de1.getplan_design());
	}
}


