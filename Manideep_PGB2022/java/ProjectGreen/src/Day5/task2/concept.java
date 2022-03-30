package Day5.task2;
import java.util.function.*;
public class concept {
	static void print(String name){  
        System.out.println("Welcome "+name);  
   	 }  
	public static void main(String args[])
	{
		Consumer<String> consumer = concept::print;  //Creating consumer
    	consumer.accept("Manideep");  
	Predicate<String> Validate = msg -> (msg == "manideep"); // Creating predicate  
    	System.out.println(Validate.test("Manideep"));
	Supplier<Double> getrandom = () -> Math.random();// Creating Supplier
	System.out.println(getrandom.get());
	}

}
