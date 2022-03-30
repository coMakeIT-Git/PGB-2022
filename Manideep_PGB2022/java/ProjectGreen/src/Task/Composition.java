import java.util.*;
public class Composition{  
    public static void main (String[] args)  
    {  
      Bike1 b1=new Bike1(1,20);
      Bike1 b2=new Bike1(1,0);
      Bike1 b3=new Bike1(2,30);
      List<Bike1> bikes = new ArrayList<Bike1>();  
      bikes.add(b1);  
      bikes.add(b2);  
      bikes.add(b3);  
      Bikestore store = new Bikestore(bikes);  
      List<Bike1> bi = store.getBikesinStore();  
      for(Bike1 mb : bi){  
        System.out.println("Gear of Bike is "+mb.getcurrentgear()+" Speed of Bike is "+mb.getcurrentspeed());  
      }  
    }
  }
  