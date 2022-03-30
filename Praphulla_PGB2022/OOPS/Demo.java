import java.io.*;
import java.util.*;

class Employee {
    
    String empname;
    String name;
    int id;
    String salary;
    private int bonus;
    public int getBonus()
    {
    return this.bonus;
    }
    public void setBonus(int bonus)
    {
    this.bonus=bonus;
    }
    
    Employee(String empname)
    {
    this.empname=empname;
    }
    Employee(String name, int id, String salary)
    {
 
        // This keyword refers to current instance itself
        this.name = name;
        this.id = id;
        this.salary = salary;
        System.out.println("\n BurgerKing Employee's Name: "+name+" ,Id: "+id+" ,Salary:"+salary);
    }
    public String getEmployeeName()
    {
        return this.empname;
    }
    public void displaydetails(String name, int id)
    {
    	System.out.println("\n The details of the employee are"+" EmployeeName:"+name+" Id:"+id);
    }
    public void displaydetails(String name, int id, String salary)
    {
    	System.out.println("\n The details of the employee are"+" EmployeeName:"+name+" Id:"+id+" Salary:"+salary);
    }
}
class Branch
{
   
    String name;
    private List<Employee> employees;
    
    Branch(String name, List<Employee> employees)
    {
       
        this.name = name;
        this.employees = employees;
    }

    public List<Employee> getEmployees()
    {
       
        return employees;
    }
}
class BurgerKing 
{ 
  private String name;
  String burgerKingName;
  private List<Branch>branches;
 
    BurgerKing(String name)
    {
      
        this.name = name;
    }
    public String getBranchName()
    {
       
        return this.name;     
    }

    
    BurgerKing(String burgerKingName,List<Branch>branches)
    {
        // This keyword refers to current instance itself
        this.burgerKingName = burgerKingName;
        this.branches = branches;
    }
    public int getTotalEmployees()
    {
        int total = 0;
        List<Employee> employees;
 
        for (Branch dept : branches) {
            employees = dept.getEmployees();
 
            for (Employee s : employees) {
                total++;
            }
        }
 
        return total;
    }
}
// DEmo class builds meals
public class Demo {
   public static void main(String[] args) {
   
      Employee emp = new Employee("Praphulla");
      emp.setBonus(1000);
      
      BurgerKing bk=new BurgerKing("BURGER KING, Branch Madhapur, Hyderabad");
      System.out.println("\n *All employee details are* :");
      
        Employee s1 = new Employee("Raphy", 35, "20000");
        Employee s2 = new Employee("Praph", 70, "10000");
        Employee s3 = new Employee("Ladoo", 73, "30000");
        Employee s4 = new Employee("Chaitu", 53, "40000");
        emp.displaydetails("Praphulla", 53);
        emp.displaydetails("Raag", 58, "10000");
        System.out.println("\n Bonus Amount recieved is: "+emp.getBonus());
        System.out.println("\n"+emp.getEmployeeName()
                           + " is employee of "+ bk.getBranchName());
  
    
        List<Employee>Branch_Madhapur= new ArrayList<Employee>();
 
        Branch_Madhapur.add(s1);
        Branch_Madhapur.add(s2);

        List<Employee>Branch_Miyapur
            = new ArrayList<Employee>();
 
        Branch_Miyapur.add(s3);
        Branch_Miyapur.add(s4);
  
        Branch b1 = new Branch("Madhapur", Branch_Madhapur);
        Branch b2 = new Branch("Miyapur", Branch_Miyapur);

        List<Branch> branches = new ArrayList<Branch>();
        branches.add(b1);
        branches.add(b2);
        for( Branch  b : branches)
        {
        System.out.println("\n Branch  Names: "+b.name);
        }
        
        System.out.println("\n Employees in Madhapur Branch are:");
        for( Employee  bm : Branch_Madhapur )
        {
        System.out.println("\n"+bm.name);
        }
        
        System.out.println("\n Employees in Miyapur Branch are:"); 
	for( Employee  bm1 : Branch_Miyapur )
        {
        System.out.println("\n"+bm1.name);
        }
        
        Iterator<Branch> i = branches.iterator();  
	while(i.hasNext())   
	{  
	System.out.println("\n Branches :"+i.next());   
	} 
	
        BurgerKing bk1 = new BurgerKing("BurgerKing:", branches);

        System.out.println("\n Total number of Employees  present in all branches of BurgerKing are: "+bk1.getTotalEmployees());

        System.out.println("\n *** Meal Preparation***");
// Meal Builder builds meals
      MealBuilder mealBuilder = new MealBuilder();

      Meal vegMeal = mealBuilder.prepareVegMeal();
      System.out.println("\n ***Veg Meal***");
      vegMeal.showItems();
      System.out.println("\n Total Cost of the order: " + vegMeal.getCost());

      Meal nonVegMeal = mealBuilder.prepareNonVegMeal();
      System.out.println("\n ***Non-Veg Meal***");
      nonVegMeal.showItems();
      System.out.println("\n Total Cost of the order: " + nonVegMeal.getCost());
   }
}
