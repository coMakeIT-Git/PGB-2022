package comakeit;

//Abstraction
abstract class Bank {
	String account_type;
	String ifsccode;
	String branch;
	
	public Bank(String account_type, String ifsccode, String branch) {
		this.account_type = account_type;
		this.ifsccode = ifsccode;
		this.branch = branch;
	}
	
	
	public String getAccount_type() {
		return account_type;
	}


	public void setAccount_type(String account_type) {
		this.account_type = account_type;
	}


	public String getIfsccode() {
		return ifsccode;
	}


	public void setIfsccode(String ifsccode) {
		this.ifsccode = ifsccode;
	}


	public String getBranch() {
		return branch;
	}


	public void setBranch(String branch) {
		this.branch = branch;
	}
	
	void loan() {
		
	}

	void createAccount() {
		
	}
	
}

//Encapsulation
class Customer{
	private String name;
	private int acc_number;
	public Customer(String name, int acc_number) {
		this.name=name;
		this.acc_number = acc_number;

	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAcc_number() {
		return acc_number;
	}
	public void setAcc_number(int acc_number) {
		this.acc_number = acc_number;
	}
	
}

//Inheritence
//IS-A
class SBI extends Bank{
	
	public SBI(String account_type, String ifsccode, String branch) {
		super(account_type, ifsccode, branch);
	}

	@Override
	public void loan() {
		System.out.println("rate of interest:10%");	
	}
	
	@Override
	public void createAccount() {
		
		
		System.out.println("Account created in SBI");
	}
	
	public void display(Customer customer) {
		System.out.println("Customer name is: "+customer.getName());
		System.out.println("Account number is: "+customer.getAcc_number());
		System.out.println("Account type: "+getAccount_type());
		System.out.println("IFSC code: "+ getIfsccode());		
		System.out.println("Branch name: "+ getBranch());
	}
	
}

class HDFC extends Bank{
	public HDFC(String account_type, String ifsccode, String branch) {
		super(account_type, ifsccode, branch);
	}

	@Override
	public void loan() {
		System.out.println("rate of interest:12%");
		
	}

	@Override
	public void createAccount() {
		System.out.println("Account created in HDFC");
		
	}
	
	//HAS-A
	public void display(Customer customer) {
		System.out.println("Customer name is: "+customer.getName());
		System.out.println("Account number is: "+customer.getAcc_number());
		System.out.println("Account type: "+getAccount_type());
		System.out.println("IFSC code: "+ getIfsccode());		
		System.out.println("Branch name: "+ getBranch());
	}
}



