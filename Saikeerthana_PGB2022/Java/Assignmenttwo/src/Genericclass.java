package saikeerthana;

public class Genericclass<T> {
	
		   private T t;

		   public void add(T t) {
		      this.t = t;
		   }

		   public T get() {
		      return t;
		   }

		   public static void main(String[] args) {
		      Genericclass<Integer> num = new Genericclass<Integer>();
		      Genericclass<String> str = new Genericclass<String>();
		    
		      num.add(10);
		      str.add("Hello World");

		      System.out.println("Integer Value :\n"+ num.get());
		      System.out.println("String Value :\n"+ str.get());
		   }
		

	

}
