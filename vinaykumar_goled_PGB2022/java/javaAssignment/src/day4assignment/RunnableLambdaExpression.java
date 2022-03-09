package day4assignment;
import java.lang.Runnable;

public class RunnableLambdaExpression {
	public static void main(String[] args) {
		Runnable r2 = () -> {   // lambda expression
	         System.out.println("Runnable with Lambda Expression");
	      };
	      new Thread(r2).start();
	}
}
