package task2;
import java.util.function.Predicate;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Supplier;
/*
 functional interface- have single abstract method
 Types functional interface
 1.Predicate - boolean result
 2.Consumer - modifies data- no result
 3.Function - both input and output
 4.Supplier - no input and output
 */

class employe{
	private String empname;

	public String getName() {
		return empname;
	}

	public void setName(String name) {
		this.empname = name;
	}
	
}
public class funcinterfaceexample {

	
	public static void main (String args[])
	{  // predicate functional interface
		Predicate<String> checklength=str -> str.length()>5;
		System.out.println(checklength.test("saiteja"));
		//consumer functional interface
		employe p =new employe();
		Consumer<employe> setName=t -> t.setName("Play java");
		setName.accept(p);
		System.out.println(p.getName());
		//function functional interface
		
		Function<Integer,String> getInt=t->t*10+" data multiplied by 10";
		System.out.println(getInt.apply(2));
		//supplier functional interface
		Supplier<Double> getRandomDouble=()->Math.random();
		System.out.println(getRandomDouble.get());
		
				
		
		
	}
}