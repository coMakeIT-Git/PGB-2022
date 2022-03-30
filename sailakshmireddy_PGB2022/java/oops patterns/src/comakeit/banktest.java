package comakeit;

public class banktest {
	public static void main(String[] args) {
		SBI s= new SBI("savings","ifsc1234","hyd");
		HDFC h= new HDFC("current","ifsc5432","sec");
		Customer c= new Customer("kiran",12345);
		s.createAccount();
		s.display(c);
		s.loan();
		System.out.println("************");
		Customer c1= new Customer("kumar",54321);		
		h.createAccount();
		h.display(c1);		
		h.loan();
	}

}
