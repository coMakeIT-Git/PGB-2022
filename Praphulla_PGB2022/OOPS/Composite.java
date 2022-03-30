import java.util.*;
class Components
{
     public String bun;
     public String veggies;
     public String patty;
  
    Components(String bun, String veggies, String patty)
    {
        this.bun= bun;
        this.veggies = veggies;
        this.patty=patty;
    }
}
class Burger {

    private final List<Components> com;
 
  
    Burger(List<Components> com)
    {
 
   
        this.com = com;
    }

    public List<Components> getComponents()
    {
        return com;
    }
}
class Composite{

    public static void main(String[] args)
    {
        Components b1
            = new Components("Plain", "Lettuce-Onions-Tomatoes", "Meat");
        Components b2
            = new Components("Seseme Seeds", "Onions-cheese-Lettuce","Potato-onion");
        Components b3 = new Components("Pretzel",
                           "Lettuce-Onions-Tomatoes","Chicken");
 
        // Creating the list which contains the
        // no. of books.
        List< Components> com = new ArrayList<Components>();
 
        // Adding books to List object
        // using standard add() method
        com.add(b1);
        com.add(b2);
        com.add(b3);

        Burger b = new Burger(Components);
 
        // Calling method of class 2 and storing list of
        // books in List Here List is declared of type
        // Books(user-defined)
        List<Components> com
            = Burger.getComponents();
 
        // Iterating over for each loop
        for (Components bk : com) {
 
            System.out.println("Bun : " + bk.bun
                               + " and "
                               + " Veggies : " + bk.veggies+" Patty"+bk.patty);
        }
    }
}
