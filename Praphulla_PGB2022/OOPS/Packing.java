public interface Packing {
   public String pack();
}
class Bottle implements Packing {

   @Override
   public String pack() {
      return "Bottle";
   }
}
class Wrapper implements Packing {

   @Override
   public String pack() {
      return "Wrapper";
   }
}
