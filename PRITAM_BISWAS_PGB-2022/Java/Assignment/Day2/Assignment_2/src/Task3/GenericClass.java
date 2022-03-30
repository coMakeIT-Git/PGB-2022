package Task3;

//Generic Class
public class GenericClass<T> { 
	
	// attribute 
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
	 GenericClass<Integer> integer = new GenericClass<Integer>(); 
 	
 	// Initialized as String
	 GenericClass<String> string = new GenericClass<String>(); 

 	// Add Data
 	integer.addData(10); 
 	string.addData("This is a String"); 

 	// Print Data Using get method
     System.out.println(integer.getData()); 
     System.out.println(string.getData()); 
 } 
}
