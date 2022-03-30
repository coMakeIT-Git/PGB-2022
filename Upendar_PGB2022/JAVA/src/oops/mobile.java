package oops;

abstract  class keymobile{
	
	private String color;
	private int emi;
	abstract  void  type();
	abstract  void  os();
	
	public int getemi() {
		return emi;
	}
	public String getcolor() {
		return color;
	}
	public void setemi(int emi) {
		this.emi=emi;
	}
	public void setcolor(String color) {
		this.color=color;
	}
	}

class nokia extends keymobile {
	void type() {
		System.out.println("this is keypad mobile");
	}
	void os() {
		System.out.println("This is nokia os");
	}
}
public class mobile extends nokia  {
	void os() {
		System.out.println("This is apple ios");
	}
public  static  void  main(String[] args)  {
keymobile mymobile =  new nokia();
mobile myapple=new mobile();
mymobile.type();
mymobile.os();
myapple.os();
mymobile.setemi(133124);
mymobile.setcolor("matte black");
System.out.println("EMI of mobile is :"+mymobile.getemi());
System.out.println("Color of mobile is :"+mymobile.getcolor());
System.out.println("Color of mobile is :"+mymobile.getcolor() +"EMI of mobile is :"+mymobile.getemi()); // asscoiation

}
}
