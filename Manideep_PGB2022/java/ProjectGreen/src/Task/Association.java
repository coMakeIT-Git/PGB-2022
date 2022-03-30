import java.util.*;
public class Association {  
    public static void main(String[] args) {  
          Person person = new Person();  
          person.setName("Manideep");  
           
         Bike1 b1 = new Bike1();  
          b1.speedUp(10);
          Bike1 b2 = new Bike1();  
          b2.speedUp(20);  
    
          List<Bike1> BikesList = new ArrayList<Bike1>();  
          BikesList.add(b1);  
          BikesList.add(b2);  
          person.setbikes(BikesList);  
          System.out.println(person.getNumbers());  
          System.out.println(person.getName());  
      }  
      
}  