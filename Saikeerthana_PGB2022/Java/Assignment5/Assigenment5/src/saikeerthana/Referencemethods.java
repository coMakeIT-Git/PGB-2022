package saikeerthana;
//import saikeerthana.Messageable.InstanceMethodReference.MethodReference.Message;

interface Sayable{  
    void say();  
}  
interface Messageable{  
    Message getMessage(String msg);  
}  
class Message{  
    Message(String msg){  
        System.out.print(msg);  
    }  
}  
 
class InstanceMethodReference {  
    public void saySomething(){  
        System.out.println("Hello, this is non-static method.");  
    } 
}
 class MethodReference {  
    public static void saySomething(){  
        System.out.println("Hello, this is static method.");  
    }  
 }
    public class Referencemethods{
    public static void main(String[] args) {  
    	// Referring static method  
        Sayable sayable = MethodReference::saySomething;  
        // Calling interface method  
        sayable.say();  
        InstanceMethodReference methodReference = new InstanceMethodReference(); // Creating object  
        // Referring non-static method using reference  
            Sayable sayable3 = methodReference::saySomething;  
        // Calling interface method  
            sayable3.say();  
            // Referring non-static method using anonymous object  
            Sayable sayable2 = new InstanceMethodReference()::saySomething; // You can use anonymous object also  
            // Calling interface method  
            sayable2.say(); 
            Messageable hello = Message::new;  //constructor refernce method
            hello.getMessage("Hello");  
    }  
}  
 
 
     

