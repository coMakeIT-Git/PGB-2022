package task4;

interface Sayable{
	void saying();
}

interface Sayable2{
	void saying2();
}

interface Sayable3{
	Sayableinter3 getSayable3(String s3);
}

class Sayableinter3{
	Sayableinter3 (String s3)
	{
		System.out.println(s3);
	}
}
public class MethodReference {

	public static void saysome()
	{
		System.out.println("Hello this is static method reference");
	}
	
	public void saysome2()
	{
		System.out.println("Hello, this is non static method reference");
	}
	
	public static void main(String[] args)
	{
		//Refering static method
		Sayable say = MethodReference::saysome;
		
		//Refering instance method reference
		//MethodReference meref=new MethodReference();
		
		Sayable2 say2= new MethodReference()::saysome2;
		Sayable3 say3 = Sayableinter3::new;
		
		say.saying();
		say2.saying2();
		say3.getSayable3("heloo this is constructor reference");
	}
}
