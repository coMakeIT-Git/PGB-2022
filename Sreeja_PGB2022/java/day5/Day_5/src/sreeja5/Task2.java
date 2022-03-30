package sreeja5;

import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;
class Multiplication{  
	   public static int multiply(int a, int b){  
		return a*b;  
	   }  
	}  
class Hello{  
    public Hello(String say){  
        System.out.print(say);  
    }  
}  
interface MyInterface{  
    void display();
    //Hello display(String say);  
}  
interface mine{  
    Hello display(String say);  
}  

public class Task2 {
	public void myMethod(){  
		System.out.println("Instance Method");  
	    }  
	public static void main(String args[]) {
		System.out.println("Method reference to a static method");
		BiFunction<Integer, Integer, Integer> product = Multiplication::multiply;  
		int pr = product.apply(11, 5);  
		System.out.println("Product of given number is: "+pr);  
		System.out.println("Method reference to a instance method");
		Task2 obj = new Task2();   
		// Method reference using the object of the class
		MyInterface ref = obj::myMethod;  
		// Calling the method of functional interface  
		ref.display();  
		System.out.println("Method reference to a constructor ");
		   mine x = Hello::new;  
	        x.display("Hello World!");  
	   
		


	}

}
