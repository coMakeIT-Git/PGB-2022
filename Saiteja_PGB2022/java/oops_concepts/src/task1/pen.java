package task1;
//Abstraction
abstract class penbrands
{
 abstract void brand();
}
//inheritance
class pentypes
{
  void types()
	{
		System.out.println("ball point pen");
	}
}
public class pen extends pentypes{
	void brand()
	{
		System.out.println("cello");
	}
	
	public static void main(String args[])
	{
		pen p1=new pen();
		p1.brand();
		p1.types();
	}

}


