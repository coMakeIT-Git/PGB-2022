class Addressclass{
	String city;
	String state;
	String country;
	
	public Addressclass (String city,String state,String country)
	{
		this.city=city;
		this.state=state;
		this.country=country;
		
		
	}
}


public class aggregation {
	
	int policy_no;
	String Policy_name;
	
	Addressclass address;
	
	public aggregation(String Policy_name, int policy_no, Addressclass address) {
		// TODO Auto-generated constructor stub
		
		this.Policy_name = Policy_name;
		this.policy_no = policy_no;
		this.address=address;
	}

	public int getPolicy_no() {
		return policy_no;
	}


	public String getPolicy_name() {
		return Policy_name;
	}


	
	void display()
	{
		System.out.println("Policy Name: "+getPolicy_name()+"Policy Number: "+policy_no);
		System.out.println("State: "+address.state+" city: "+address.city+" country :"+address.country);
	}




	public static void main (String[] args)
	{
	    Addressclass Addressobj=new Addressclass("eee","hhhhh","mmmmm");
		aggregation obj = new aggregation("Abc ",1234,Addressobj);
		obj.display();
	}
		
}
