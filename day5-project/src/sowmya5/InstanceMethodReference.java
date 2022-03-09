package sowmya5;
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
public class InstanceMethodReference {  
        public void saySomething(){  
            System.out.println("Hello, this is non-static method.");  
        }  
        public static void saySome(){  
            System.out.println("Hello, this is static method.");  
        }  
        public static void main(String[] args) {  
            InstanceMethodReference methodReference = new InstanceMethodReference(); // Creating object  
            // Referring non-static method using reference  
                Sayable sayable = methodReference::saySomething;  
            // Calling interface method  
                sayable.say();  
                // Referring non-static method using anonymous object  
                Sayable sayable2 = InstanceMethodReference::saySome;  
                // Calling interface method  
                sayable2.say();    
                Messageable hello = Message::new;  
                hello.getMessage("Hello");  
        }  
    }  
