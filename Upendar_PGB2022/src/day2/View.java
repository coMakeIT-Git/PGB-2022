package day2;

//Generic Class
public class View<T> { 
	
	// Attribute 
 private T d; 
 
 // Generic Class add method
 public void addData(T d){ 
     this.d = d; 
 } 

// Generic Class get method
 public T getData(){ 
 	return d;
 } 

 public static void main(String[] args){ 
 	// Initialized as Integer
 	View<Integer> integer = new View<Integer>(); 
 	
 	// Initialized as String
 	View<String> string = new View<String>(); 

 	// Add Data
 	integer.addData(10); 
 	string.addData("This is a String"); 

 	// Print Data Using get method
     System.out.println(integer.getData()); 
     System.out.println(string.getData()); 
 } 
}
