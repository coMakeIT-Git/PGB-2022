import java.util.Scanner;

class Life extends Insurance {

	public Life(String insuranceType) {
		super(insuranceType);
		setCost();
	}

	@Override
	public void setCost() {
		this.monthlyPrice = 36;
	}

	@Override
	public void display() {
		System.out.printf("InsuranceType : %s\n Monthly Price : %.2f\n", insuranceType, monthlyPrice);
	}
	
} 
class Health extends Insurance {

	public Health(String insuranceType) {
		super(insuranceType);
		setCost();
	}

	@Override
	public void setCost() {
		this.monthlyPrice = 196;
	}

	@Override
	public void display() {
		System.out.printf("InsuranceType : %s\nMonthly Price : %.2f\n", insuranceType, monthlyPrice);
	}
	
}

abstract class Insurance {
	
	public String insuranceType;
	public double monthlyPrice;
	
	public Insurance(String insuranceType) {
		this.insuranceType = insuranceType;
	}
	
	public abstract void setCost();
	
	public abstract void display();

	public String getInsuranceType() {
		return insuranceType;
	}

	public double getMonthlyPrice() {
		return monthlyPrice;
	}

}

public class useInsaurance {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		System.out.println("----Insurance Management System----\n Please select the insurance type \n 1. Health Insurance \n 2. Life Insurance \n Enter your choice : ");
		
		Insurance insurance;
		Scanner input = new Scanner(System.in);
		
		String str = input.next();
		if(str.equals("1")){
			insurance = new Health("Health Insurance");
			insurance.display();
		} else if(str.equals("2")){
			insurance = new Life("Life Insurance");
			insurance.display();
		} else {
			System.out.println("Invalid insurance type input should be either 1 or 2");
		}
	}

}