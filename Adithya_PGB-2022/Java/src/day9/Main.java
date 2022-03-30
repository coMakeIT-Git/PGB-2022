package day9;
import java.util.*;        
interface currency{
	//Abstraction->methods in interface byfault are abstract methods
	int convertCurrency(int a,String c);
}
interface paperCash extends currency{
	int getPaperCashBalance();
	void setPaperCashBalanace(int a,char c);
}
interface cardCash extends currency{
	int getCardCashBalance();
	void setCardCashBalanace(int a,char c);
}
class cash implements paperCash,cardCash{
	//Inheritance->Multiple inheritance using interfaces
	//Encapsulation->Declaring private to attributes(restricting other classes to change attributes values directly
		private int balance=0;
		private int papercash=0;
		private int cardcash=0;
		//Run-time Polymorphism->Overiding abstract methods
		public int getPaperCashBalance(){
			return this.papercash;
		}
		public int getCardCashBalance(){
			return this.cardcash;
		}
		int getBalance(){
			this.balance=this.papercash+this.cardcash;
			return balance;
		}
		public void setPaperCashBalanace(int amount,char c){
			if(c=='p'){
				this.papercash+=amount;
			}
			else{
				if(amount>this.balance){
					System.out.println("Cannot Perform");
				}
				else{
					this.papercash-=amount;
					System.out.println("Amount Deducted successfully");
				}
			}
		}
		public void setCardCashBalanace(int amount,char c){
			if(c=='p'){
				this.cardcash+=amount;
			}
			else{
				if(amount>this.balance){
					System.out.println("Cannot withdraw");
				}
				else{
					this.cardcash-=amount;
					System.out.println("Amount Deducted successfully");
				}
			}
		}
		void addCash(String modeOfTransaction,int amount){
			if(modeOfTransaction.equals("cash")){
			setPaperCashBalanace(amount,'p');
			}
			else{
				setCardCashBalanace(amount,'p');
			}
		}
		void withDraw(String modeOfTransaction,int amount){
			if(modeOfTransaction.equals("cash")){
			setPaperCashBalanace(amount,'n');
			}
			else{
				setCardCashBalanace(amount,'n');
			}
		}
		public int convertCurrency(int amount,String currency) {
			double ans=0;
			switch (currency){
			case "US":
				ans=amount/70;
			case "UK":
				ans=amount/95;
			}
			return (int)ans;
		}
}
class currency_compare{
	cash first;
	cash second;
	void compare(int a,int b) {
		if(a/70>b/70) {
			System.out.println("first person has higher dollars");
		}
		else {
			System.out.println("second person has higher dollars");
		}
	}
	void add(cash a,cash b) {
		this.first=a;
		this.second=b;
	}
	//Static-Time Polymorphism->method overloading the compare method
	String compare() {
		int first=this.first.convertCurrency(this.first.getBalance(), "UK");
		int second=this.second.convertCurrency(this.second.getBalance(), "UK");
		return " "+(first>second?"deeraj ":"ravi ")+" has higher dollars";
	}
}
class Main{
	public static void main(String[] args) {
		cash adithya=new cash();
		Scanner sc=new Scanner(System.in);
		System.out.println("Number of iterations: ");
		int n=sc.nextInt();
		sc.nextLine();
		while(n-->0) {
			System.out.println("Commands->Adding_Cash With_Draw Check_Balance Convert_Currency Currency_Compare");
			String typeOfTransaction=sc.nextLine();//add,withdraw,check balance,convert currency
			System.out.println("cash or card");
			String modeOfTransaction=sc.nextLine();//cash,card
			if(typeOfTransaction.equals("Check_Balance")) {
				switch(modeOfTransaction){
				case "cash":
					System.out.println(adithya.getPaperCashBalance());
					break;
				case "card":
					System.out.println(adithya.getCardCashBalance());
					break;
				default:
					System.out.println(adithya.getBalance());
				}
			}
			else if(typeOfTransaction.equals("Convert_Currency")) {
				System.out.println("input US for dollar UK for euro");
				String currency=sc.next();
				switch(modeOfTransaction){
				case "cash":
					System.out.println(adithya.convertCurrency(adithya.getPaperCashBalance(), currency));
					break;
				case "card":
					System.out.println(adithya.convertCurrency(adithya.getCardCashBalance(),currency));
					break;
				default:
					System.out.println(adithya.convertCurrency(adithya.getBalance(),currency));
				}
			}
			else if(typeOfTransaction.equals("Currency_Compare")) {
				currency_compare a=new currency_compare();
				cash deeraj=new cash();
				cash ravi=new cash();
				deeraj.setCardCashBalanace(5000, 'p');
				ravi.setCardCashBalanace(6000, 'p');
				a.add(deeraj, ravi);
				//Composition->currency_compare() is dependent of cash... 
				System.out.println(a.compare()+" "+a.first.getBalance());
				//Aggregation->currency_compare() is independent of cash and cash is also independent of currency_compare()
				a.compare(5000,6000);
			}
			else {
				System.out.println("Enter the amount");
				int amount=sc.nextInt();
				sc.nextLine();
				switch(typeOfTransaction){
				case "Adding_Cash":
					adithya.addCash(modeOfTransaction,amount);
					System.out.println("Amount Added successfully ");
					break;
				case "With_Draw":
					adithya.withDraw(modeOfTransaction,amount);
					break;
				default:
					System.out.println("Some Error");
				}
			}
			
		}
	}
}