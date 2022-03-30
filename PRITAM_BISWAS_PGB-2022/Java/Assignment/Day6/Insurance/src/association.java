import java.util.*;   
class insurance {    
   private String insurance_no;

public String getInsurance_no() {
	return insurance_no;
}

public void setInsurance_no(String insurance_no) {
	this.insurance_no = insurance_no;
}  
   

}  
class user {       
   private String name;  
   List<insurance> numbers;
public String getName() {
	return name;
}
public void setName(String name) {
	this.name = name;
}
public List<insurance> getNumbers() {
	return numbers;
}
public void setNumbers(List<insurance> numbers) {
	this.numbers = numbers;
}  

}  
public class association {  
     public static void main(String[] args) {  
           user person = new user();  
           person.setName("Shubham Rastogi");  
            
          insurance number1 = new insurance();  
           number1.setInsurance_no("8868");  
           insurance number2 = new insurance();  
           number2.setInsurance_no("8630");  
     
           List<insurance> numberList = new ArrayList<insurance>();  
           numberList.add(number1);  
           numberList.add(number2);  
           person.setNumbers(numberList);  
           System.out.println(person.getNumbers()+" are insurance of the person "+  
           person.getName());  
       }  
       
}

