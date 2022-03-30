// Interface Item
public interface Item
 {
   public String name();
   public Packing packing();
   public float price();	
}
// Abstract class Burger implements Item
abstract class Burger implements Item {

   @Override
   public Packing packing() {
      return new Wrapper();
   }

   @Override
   public abstract float price();
}
// Concreate Class Chicken Burger 
class ChickenBurger extends Burger {

   public float price() {
      return 259.50f;
   }

   public String name() {
      return "Chicken Burger";
   }
}
// Concreate Class Veg Burger 
class VegBurger extends Burger {

   @Override
   public float price() {
      return 159.0f;
   }

   @Override
   public String name() {
      return "Veg Burger";
   }
}
// Abstract class ColdDrink
abstract class ColdDrink implements Item {

	@Override
	public Packing packing() {
       return new Bottle();
	}

	@Override
	public abstract float price();
}
class Coke extends ColdDrink {

   @Override
   public float price() {
      return 60.0f;
   }

   @Override
   public String name() {
      return "Coke";
   }
}
class Pepsi extends ColdDrink {

   @Override
   public float price() {
      return 60.0f;
   }

   @Override
   public String name() {
      return "Pepsi";
   }
}


