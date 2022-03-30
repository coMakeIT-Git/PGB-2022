public class BurgerKing 
{

    // Attributes of bank
    private String name;
 
    // Constructor of this class
    BurgerKing(String name)
    {
      
        this.name = name;
    }
    public String getBranchName()
    {
       
        return this.name;     
    }
}
class Employee {
    
    private String name;
    
    Employee(String name)
    {
        
    }
 
    public String getEmployeeName()
    {
        return this.name;
    }
}

// DEmo class builds meals
public class Demo {
   public static void main(String[] args) {
   
      BurgerKing bk=new BurgerKing("*BURGER KING, branch Madhapur,Hyd*");
      Employee emp = new Employee("Praphulla");
      System.out.println(emp.getEmployeeName()
                           + " is employee of "
                           + bk.getBranchName());
      MealBuilder mealBuilder = new MealBuilder();

      Meal vegMeal = mealBuilder.prepareVegMeal();
      System.out.println("Veg Meal");
      vegMeal.showItems();
      System.out.println("Total Cost: " + vegMeal.getCost());

      Meal nonVegMeal = mealBuilder.prepareNonVegMeal();
      System.out.println("\n\nNon-Veg Meal");
      nonVegMeal.showItems();
      System.out.println("Total Cost: " + nonVegMeal.getCost());
   }
}
