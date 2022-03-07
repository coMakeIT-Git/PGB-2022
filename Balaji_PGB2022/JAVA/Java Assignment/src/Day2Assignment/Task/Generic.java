package Day2Assignment.Task;



public class Generic<T> {
   T value;
   Generic(T value)
   {
	  this.value=value;
   }
   public T display()
   {
	   return(this.value);
   }
   public static void main(String args[])
   {
	   Generic<Integer> iobj=new Generic<>(100);
	   Generic<Boolean> bobj=new Generic<>(true);
	   Generic<String> sobj=new Generic<>("RAM");
	   Generic<Double> dobj=new Generic<>(78.24321);
	   System.out.println("Displaying different types using Generic class");
	   System.out.println(iobj.display());
	   System.out.println(bobj.display());
	   System.out.println(sobj.display());
	   System.out.println(dobj.display());
	   
   }
   
}
