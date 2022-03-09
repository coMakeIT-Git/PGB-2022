package day5Assignment;

interface PrintConstructor{
	Message print(String str);
}
class Message{
	Message(String str){
		System.out.println(str);
	}
}
public class ConstructorReference {
	public static void main(String[] args) {
		PrintConstructor obj=Message::new;
		obj.print("constructor reference");
		
	}
}
