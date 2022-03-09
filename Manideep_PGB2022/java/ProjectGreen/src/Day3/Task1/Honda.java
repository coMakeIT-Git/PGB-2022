package Day3.Task1;
import Day3.Task1.Bike;
public class Honda extends Bike{
	public void run()
	{
		System.out.println("Honda Bike is Running");
	}
	public static void  main(String args[])
	{
		Honda h=new Honda();
		h.run();
	}
}
