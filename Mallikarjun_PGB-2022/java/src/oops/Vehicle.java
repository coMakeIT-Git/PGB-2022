package oops;
import java.util.*;
abstract class Car
{
	private int carmileage;
	private int carspeed;
	private String carbrand;
	public int getcarmileage() {
		return carmileage;
	}
	public void setcarmileage(int carmileage) {
		this.carmileage = carmileage;
	}
	public int getcarspeed() {
		return carspeed;
	}
	public void setcarspeed(int carspeed) {
		this.carspeed = carspeed;
	}
	public String getcarbrand() {
		return carbrand;
	}
	public void setcarbrand(String carbrand) {
		this.carbrand = carbrand;
	}
	
	abstract public void features(char c);
	abstract public void increase_speed(int speed);
	abstract public void decrease_speed(int speed);
}

class FuelCar extends Car{
	public void is_sedan() {
		System.out.println("It is a Sedan Car ");
	}
	public void features(char c) {
		switch(c) {
			case 'a':
				System.out.println("Car consists AirBags");
				break;
			case 'b':
				System.out.println("Car has 360Camera");
				break;
			default:
				System.out.println("It,s a 2 Seater");
		}
	}
	public void features(int c) {
		switch(c) {
			case 1:
				System.out.println("Car consists AirBags");
				break;
			case 2:
				System.out.println("Car has 360Camera");
					break;
			default:
				System.out.println("It,s a 2 Seater");
		}
			
	}
	public void increase_speed(int speed) {
		if(speed<300) {
			speed++;
			System.out.println("Car speed increased to "+speed);
		}
	}
	public void decrease_speed(int speed) {
		if(speed!=0) {
			speed--;
			System.out.println("Car speed decreased to "+speed);
		}
	}
	
	
}
class ElectricCar extends FuelCar{
	String name;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	
	public void is_sedan() {
		System.out.println("It is a Sedan Car");
	}

		
}
class OwnerDetails{
	String name;
	String address;
	ElectricCar electric;
	OwnerDetails(String name,String address,ElectricCar electric)
	{
		this.name=name;
		this.address=address;
		this.electric=electric;
	}
}
class CarColor{
	String car_color;
	int carId;
	List<ElectricCar> names;
	CarColor(List<ElectricCar> names)
	{
		this.names=names;
	}
	public String getar_color() {
		return car_color;
	}
	public void setcar_color(String car_color) {
		this.car_color = car_color;
	}
	public void setname(String name){
	}
		
		

	public int getCarId() {
		return carId;
	}
	public void setCarId(int carId) {
		this.carId = carId;
	}
    public List<ElectricCar> getTotalnames(){        
        return names;   
     }
	
	
	
} 
public class Vehicle extends ElectricCar{

	public static void main(String[] args) {
		ElectricCar objcar=new ElectricCar();
		
		objcar.setcarmileage(10);
		objcar.setcarspeed(400);
		objcar.setcarbrand("Ferrari");
		System.out.println("Mileage of the Car is: "+objcar.getcarmileage());
		System.out.println("Speed of the Car is: "+objcar.getcarspeed());
		System.out.println("Brand of the Car is: "+objcar.getcarbrand());
		objcar.features(1);
		objcar.features('c');
		objcar.features(' ');
		objcar.is_sedan();
		objcar.increase_speed(210);
		objcar.decrease_speed(110);
		
		ElectricCar ec1= new ElectricCar();
		ElectricCar ec2= new ElectricCar();
		
		ec1.setName("Tata");
		ec2.setName("Tesla");
		List<ElectricCar> names = new ArrayList<>();
		names.add(ec1); 
        names.add(ec2); 
        CarColor obj=new CarColor(names);
		List<ElectricCar> nms = obj.getTotalnames();
		obj.setcar_color("White");
		obj.setCarId(320);
		obj.setname("Bmw");
		System.out.println("Vehicle Name is "+objcar.getName());
		System.out.println("Vehicle BrandId is "+obj.getCarId());
		System.out.println("Vehicle Color is "+obj.getar_color());
		
		for(ElectricCar ec:nms) {
			System.out.println("Names are : "+ ec.name);
			
		}
		
		OwnerDetails od = new OwnerDetails("Arjun","Hyderabad", ec2);
		System.out.println("Owner name is "+ od.name);
		System.out.println("Owner Address is "+ od.address);
		System.out.println("Electric car name is "+ od.electric.name);

	}

}

