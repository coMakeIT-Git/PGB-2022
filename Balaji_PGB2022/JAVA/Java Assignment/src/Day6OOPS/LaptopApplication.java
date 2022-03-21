package Day6OOPS;
import java.util.*;
abstract class Laptop
{
	private int lappywidth;
	private int lappyheight;
	private String lappycolor;
	//Encapsulation
	//Using Setter and Getter methods	
	public int getLappywidth() {
		return lappywidth;
	}
	public void setLappywidth(int lappywidth) {
		this.lappywidth = lappywidth;
	}
	public int getLappyheight() {
		return lappyheight;
	}
	public void setLappyheight(int lappyheight) {
		this.lappyheight = lappyheight;
	}
	public String getLappycolor() {
		return lappycolor;
	}
	public void setLappycolor(String lappycolor) {
		this.lappycolor = lappycolor;
	}
	
	abstract public void os(char c);
	abstract public void increase_brightness(int brightness);
	abstract public void decrease_brightness(int brightness);
}

class NormalLaptop extends Laptop{
	
	public void is_touchscreen() {
		System.out.println("This Laptop does not have functionality touchscreen!!! ");
	}
	public void os(char c) {
		switch(c) {
			case 'a':
				System.out.println("This laptop is booted with ubuntu!!!");
				break;
			case 'b':
				System.out.println("This laptop is booted with unix!!!");
				break;
			default:
				System.out.println("This laptop is booted with windows!!! ");
		}
	}
	public void os(int c) {
		switch(c) {
			case 1:
				System.out.println("This laptop is booted with ubuntu!!!");
				break;
			case 2:
				System.out.println("This laptop is booted with unix!!!");
					break;
			default:
				System.out.println("This laptop is booted with windows!!! ");
		}
			
	}
	public void increase_brightness(int brightness) {
		if(brightness<100) {
			brightness++;
			System.out.println("Laptop Brightness increased to "+brightness);
		}
	}
	public void decrease_brightness(int brightness) {
		if(brightness!=0) {
			brightness--;
			System.out.println("Laptop Brightness decreased to "+brightness);
		}
	}
	
	
}
//Inheritance
class TouchLaptop extends NormalLaptop{
	String name;
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	

	//Method Overriding
	@Override
	public void is_touchscreen() {
		System.out.println("This Laptop Has Functionality Of TouchScreen!!! ");
	}
	
	
}
class LaptopBag{
	String bagname;
	String bagcolor;
	TouchLaptop tchlap;
	LaptopBag(String bagname,String bagcolor,TouchLaptop tchlap)
	{
		this.bagname=bagname;
		this.bagcolor=bagcolor;
		this.tchlap=tchlap;
	}
}
class LaptopCover{
	String cover_color;
	int coverId;
	List<TouchLaptop> names;
	LaptopCover(List<TouchLaptop> names)
	{
		this.names=names;
	}
	public String getCover_color() {
		return cover_color;
	}
	public void setCover_color(String cover_color) {
		this.cover_color = cover_color;
	}
	public int getCoverId() {
		return coverId;
	}
	public void setCoverId(int coverId) {
		this.coverId = coverId;
	}
    public List<TouchLaptop> getTotalnames(){        
        return names;   
     } 
	
}
public class LaptopApplication extends TouchLaptop{

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TouchLaptop lapobj=new TouchLaptop();
		lapobj.setLappywidth(30);
		lapobj.setLappyheight(40);
		lapobj.setLappycolor("BLACK");
		System.out.println("Width of the laptop is: "+lapobj.getLappywidth());
		System.out.println("Height of the laptop is: "+lapobj.getLappyheight());
		System.out.println("Colour of the laptop is: "+lapobj.getLappycolor());
		//Polymorphism
		//Method Overloading
		lapobj.os(2);
		lapobj.os('a');
		//To access default value
	    lapobj.os(' ');
		//Method Overriding
		lapobj.is_touchscreen();
		lapobj.increase_brightness(68);
		lapobj.decrease_brightness(89);
		TouchLaptop t1=new TouchLaptop();
		TouchLaptop t2=new TouchLaptop();
		t1.setName("Dell");
		t2.setName("HP");
        List<TouchLaptop> names = new ArrayList<>(); 
        names.add(t1); 
        names.add(t2); 
		LaptopCover lapcov=new LaptopCover(names);
		List<TouchLaptop> nms = lapcov.getTotalnames();
		lapcov.setCover_color("Orange");
		lapcov.setCoverId(1);
		lapobj.setName("ASUS");
		//Association
		System.out.println("Laptop Name is "+lapobj.getName()+" and laptop color Id is "+lapcov.getCoverId()+
		" and color name is :"+lapcov.getCover_color());
		//Composition
		for(TouchLaptop ns:nms)
		{
			System.out.println("Names are: "+ ns.name);
		}
		
		//Aggregation
		LaptopBag lapbag=new LaptopBag("Samsonite","Blue",t1);
		System.out.println("Laptop bagname is:"+lapbag.bagname);
		System.out.println("Laptop bagcolor is:"+lapbag.bagcolor);
		System.out.println("Laptop name is:"+lapbag.tchlap.name);
		

	}

}

