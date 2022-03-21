
public class patientDead extends ambulanceBookings{
	public void purpose(String color) {
		System.out.println("To Hospital"+color);
	}
	public void TakeDetails()
	{
		System.out.println("ENTER YOUR FULL NAME------");
		name = input.nextLine();
		System.out.println("ENTER YOUR MOBILE NUMBER-------");
		PhoneNumber = input.nextLong();
		System.out.println("----BOOKING SUCCESSFUL-----"+count++);
	}
	public void PrintDetails()
	{
		System.out.println("FULL NAME IS-------"+name);
		System.out.println("MOBILE NUMBER IS---------"+PhoneNumber);
	    System.out.println("Happy Journey, You're Dead.");
	}
}
